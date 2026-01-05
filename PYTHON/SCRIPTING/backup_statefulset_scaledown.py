#12. Create Python Script to back up Kubernetes StatefulSets and then Scale down all StatefulSets in every namespace 0 replicas.

# The script automates two operations across the entire Kubernetes cluster:
#     Backup every StatefulSet (as YAML files)
#     Scale down every StatefulSet to 0 replicas
# It does this by:
#     Connecting to the Kubernetes API
#     Looping through all namespaces
#     Handling each StatefulSet one by one



#Scales a given StatefulSet down to 0 replicas, meaning all Pods managed by that StatefulSet are stopped, but the StatefulSet object itself remains.
import os
import yaml
from kubernetes import client, config
from datetime import datetime

# ---------------- CONFIG ----------------
BACKUP_DIR = "statefulset_backups"
DRY_RUN = False  # actually scales StatefulSets to 0
# ---------------------------------------

def load_kube_config():
    try:
        config.load_kube_config() #For running the script on your laptop
        print("Loaded local kubeconfig")
    except:
        config.load_incluster_config() #Inside a pod-> use service account credentials.
        print("Loaded in-cluster kubeconfig")


def backup_statefulset(api, sts): #kubernetes api client and 1 stateful set passed
    namespace = sts.metadata.namespace #fetch namespace
    name = sts.metadata.name #name

    ns_dir = os.path.join(BACKUP_DIR, namespace)
    os.makedirs(ns_dir, exist_ok=True)
    #BACKUP_DIR/
            #└── namespace/
            #    └── statefulset.yaml


    backup_file = os.path.join(ns_dir, f"{name}.yaml")

    # Clean up runtime-only fields
    sts_dict = api.api_client.sanitize_for_serialization(sts) #Converts the Kubernetes StatefulSet object into a plain Python dictionary, Required before dumping to YAML
    #These fields are cluster-generated and must NOT be restored:
    sts_dict["metadata"].pop("managedFields", None)
    sts_dict["metadata"].pop("resourceVersion", None)
    sts_dict["metadata"].pop("uid", None)
    sts_dict["metadata"].pop("creationTimestamp", None)
    sts_dict["status"] = None

#Writes the cleaned StatefulSet definition to disk as YAML
    with open(backup_file, "w") as f:
        yaml.safe_dump(sts_dict, f)

    print(f"✔ Backed up {namespace}/{name}")


def scale_statefulset_to_zero(api, sts):
    namespace = sts.metadata.namespace
    name = sts.metadata.name

    if DRY_RUN: # if dry_run=true .. safe zone ..nthg happens,no scaling happnes, only prints it.
        #if dryrun is false, python skips this and move to code api.patch_namespaced_stateful_set_scale(...)

        print(f"[DRY-RUN] Would scale {namespace}/{name} to 0 replicas")
        return # return is needed to stop the function immediately
    #So when DRY_RUN = True, the script stops before scaling.


#This is the request message sent to Kubernetes.“Change the StatefulSet’s desired number of Pods to 0.”
    body = {
        "spec": {
            "replicas": 0
        }
    }


#This line talks to the Kubernetes API server.“For this StatefulSet (name + namespace), update ONLY the scale (replicas).”
    api.patch_namespaced_stateful_set_scale(
        name=name,
        namespace=namespace,
        body=body
    )

    print(f"⬇ Scaled {namespace}/{name} to 0 replicas")


#After this call what kubernetes does internally
        # Kubernetes terminates all Pods of the StatefulSet
        # Pods shut down gracefully
        # Volumes (PVCs) are NOT deleted
        # StatefulSet object still exists

def main():
    load_kube_config()
    apps_api = client.AppsV1Api()

    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    os.makedirs(BACKUP_DIR, exist_ok=True)
    print(f"Backup directory: {BACKUP_DIR}")
    print(f"Timestamp: {timestamp}")

    statefulsets = apps_api.list_stateful_set_for_all_namespaces().items

    if not statefulsets:
        print("No StatefulSets found.")
        return

    print(f"Found {len(statefulsets)} StatefulSets")

    for sts in statefulsets:
        backup_statefulset(apps_api, sts)
        scale_statefulset_to_zero(apps_api, sts)

    print("✅ Backup and scale-down completed.")


if __name__ == "__main__":
    main()



#run the script
#apt update
# apt install -y python3-pip
# pip3 --version

#pip3 install pyyaml
# pip3 install kubernetes
# python3 statefulset.py




#Doubts:
#if dry_run: checks both condition 
#condition 1: True
# if DRY_RUN:   # if True
        #     Condition is true
        #     ✔ Code inside runs
        #     ✔ return stops the function
        #     No scaling.

#condition2: False
#if DRY_RUN:   # if False
        # Condition is false
        # ❌ Code inside is skipped
        # Python does not enter this block and continues to:
        # api.patch_namespaced_stateful_set_scale(...)
        # Scaling Happens

#visual flow:
# Start function
#       |
#       v
# Is DRY_RUN True?
#      / \
#    Yes  No
#    |     |
#  Print   Scale StatefulSet
#  Return
