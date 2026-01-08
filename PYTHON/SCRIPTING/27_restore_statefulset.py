#15. Create Python Script to scale up the Kubernetes StatefulSets to the original replica counts using backup

import os #Work with folders & files
import yaml #Read backup YAML files
from kubernetes import client, config #client=Talk to Kubernetes API, config=Load kubeconfig
from kubernetes.client.exceptions import ApiException #ApiException=Catch Kubernetes API errors

# ------------- CONFIG ----------------
BACKUP_DIR = "statefulset_backups"
DRY_RUN = False   # True = no scaling, only print #false=Actually scales StatefulSets
# ------------------------------------

def load_kube_config():
    try:
        config.load_kube_config()
        print("Loaded local kubeconfig")
    except:
        config.load_incluster_config()
        print("Loaded in-cluster kubeconfig")


def restore_statefulset(api, sts_yaml): #Restores one StatefulSet at a time
    metadata = sts_yaml.get("metadata", {}) #Read Metadata 
    spec = sts_yaml.get("spec", {}) #read spec


#Extract Name, Namespace & Replicas
    name = metadata.get("name")
    namespace = metadata.get("namespace")
    replicas = spec.get("replicas")

    if replicas is None: #safety check=Prevents crashes, Skips broken / incomplete backups
        print(f"⚠ Skipping {namespace}/{name} (no replicas found)")
        return

    if DRY_RUN:  # checks if DRY_RUN is True, enters the if condition and prints the statement
        print(f"[DRY-RUN] Would scale {namespace}/{name} to {replicas}")
        return  # return exits the function, so no scaling happens
#if false, exit the if statement and save the body and patching happens, Then scales
#python does= Check once → if True run block → otherwise skip block and continue


    body = {
        "spec": {
            "replicas": replicas #replicas is taken directly from the backup YAML file.line 30
        }
    }

    try:
        api.patch_namespaced_stateful_set_scale( #patching the body
            name=name,
            namespace=namespace,
            body=body
        )
        print(f"⬆ Restored {namespace}/{name} to {replicas} replicas")

    except ApiException as e:
        print(f"❌ Failed to restore {namespace}/{name}: {e}")


def main():
    load_kube_config()
    apps_api = client.AppsV1Api() #creates an API client to manage statefulsets

    if not os.path.exists(BACKUP_DIR): # Ensures backups exist before restore(check backup code)
        print("Backup directory not found!")
        return

    for namespace in os.listdir(BACKUP_DIR): # loop hrough all namespace directory inside the  backup folder
        ns_path = os.path.join(BACKUP_DIR, namespace) #creating a path

        if not os.path.isdir(ns_path):
            continue

        for file in os.listdir(ns_path): #looping through each file in namespace directory
            if not file.endswith(".yaml"):
                continue

            file_path = os.path.join(ns_path, file) #if ends with yaml..join the path

            with open(file_path, "r") as f:
                sts_yaml = yaml.safe_load(f) #read the yaml file

            restore_statefulset(apps_api, sts_yaml) # # Restores the StatefulSet to its original replica count

    print("✅ StatefulSet restore completed.")


if __name__ == "__main__":
    main()


#doubts?
    #1. why DRY_RUN = False  #false=Actually scales StatefulSets ## True = no scaling, only print?

#DRY_RUN is a safety flag that allows the script to simulate scaling without making changes when set to True, and perform real scaling when set to False.
