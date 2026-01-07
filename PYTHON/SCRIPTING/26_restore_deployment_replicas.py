#25_backup_deployment_replica.py = backup and scaledown code 
#run this first and run this


#14. Create Python Script to scale up the deployment replicas to the original replica counts for all Kubernetes Deployments using backup

# Steps:
#     before scaledown backup of deployment saved
#     after scaledown deployment will be 0
#     Then scale up the deployment using backup file.

from kubernetes import client, config #client=Api connection, Config = Making knw python to connect to which cluster.
import json  

# Load kubeconfig (outside cluster)
config.load_kube_config()

apps_v1 = client.AppsV1Api() # kubernetes API

# Load backup file
with open("deployment_replica_backup.json", "r") as f:
    backup = json.load(f)

print("\n🔄 Restoring deployments to original replica counts...\n")

for item in backup["deployments"]:
    namespace = item["namespace"]
    name = item["deployment"]
    replicas = item["replicas"]

    body = {
        "spec": {
            "replicas": replicas
        }
    }

    apps_v1.patch_namespaced_deployment(
        name=name,
        namespace=namespace,
        body=body #applied the backup data here
    )

    print(f"Restored {name} in {namespace} to {replicas} replicas")

print("\n✅ All deployments restored successfully")

