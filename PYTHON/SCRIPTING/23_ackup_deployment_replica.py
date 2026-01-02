#Create Python Script to back up deployment replica counts and then scale down all Kubernetes Deployments in every namespace to 0 replicas.


# You must do TWO things (in order)
# 1. Backup current state
#     For every namespace
#     For every Deployment
#     Save:
#         Namespace name
#         Deployment name
#         Current replica count
#     Store it safely (JSON or YAML file)

# 2. Scale down
#     Change replicas = 0
#     For all Deployments
#     Across all namespaces

# IMP in real life:
#     Cluster maintenance
#     Cost-saving shutdowns
#     Disaster recovery preparation
#     Safe rollback after outages



from kubernetes import client, config# client=Used to talk to the Kubernetes API (get deployments, update them, etc.), config=Loads your Kubernetes configuration so Python knows which cluster to connect to
import json#Used to save backup data into a .json file
from datetime import datetime #Used to record when the backup was taken

# 1. Load Kubernetes configuration
config.load_kube_config()   # Use load_incluster_config() if running inside cluster
#Reads your local kubeconfig file (usually ~/.kube/config),Allows the script to authenticate and connect to the Kubernetes cluster,If this script runs inside a pod, you’d use:config.load_incluster_config()


#create API client...AppsV1Api is the Kubernetes API that manages:Deployments,StatefulSets,Daemonsets.
apps_v1 = client.AppsV1Api()

# 2. Get all deployments in all namespaces
deployments = apps_v1.list_deployment_for_all_namespaces()#Fetches every deployment in every namespace
#Returns a list-like object:
#deployments.items
#Each item = one Deployment




backup_data = {
    "backup_time": datetime.utcnow().isoformat(),#records when the backup was taken (UTC time)
    "deployments": [] #empty list where deployment info will be stored
}

# 3. Backup replica counts
for dep in deployments.items: #This loops through every deployment in the cluster.
    namespace = dep.metadata.namespace #which namespace the deployment is in
    name = dep.metadata.name#deployment name
    replicas = dep.spec.replicas#number of pods currently running

    backup_data["deployments"].append({
        "namespace": namespace,
        "deployment": name,
        "replicas": replicas
    }) #Each deployment’s data is added to the backup list.

# Save backup to file
with open("deployment_replica_backup.json", "w") as f:
    json.dump(backup_data, f, indent=4)

print("Backup completed successfully.")

# 4. Scale all deployments to 0 replicas
for dep in deployments.items:
    namespace = dep.metadata.namespace
    name = dep.metadata.name

    body = {
        "spec": {
            "replicas": 0
        }
    }
#Apply the scale-down
    apps_v1.patch_namespaced_deployment( #patch_namespaced_deployment updates only part of the deployment
        name=name,
        namespace=namespace,
        body=body
    )

    print(f"Scaled deployment {name} in namespace {namespace} to 0 replicas")

print("All deployments scaled down successfully.")



#DOUBT:
# What u mean by inside the cluster and outside the cluster?
    #if the code is running inside the pod is considered as inside the cluster
    #It uses a ServiceAccount for authentication.
    #outside the cluster:
    #     if u think u have kubernetes and u are running ur script in a node(master/worker) where kubernetes is installed
    #     kubernetes is completely pod based not node based.
    # So here the script is running outside the cluster means outside the pod.
    #SSH into master/worker is not inside cluster
