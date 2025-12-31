# Create Python Script to scale down Kubernetes DaemonSets by patching them with a nodeSelector that matches no actual node

from kubernetes import client, config #config-->loads kubeconfig or in-cluster config,client → Kubernetes API objects
from kubernetes.client.rest import ApiException #ApiException → catches Kubernetes API errors

# Load Kubernetes configuration
# Use load_incluster_config() if running inside a pod
config.load_kube_config() #Reads ~/.kube/config, Uses the same cluster & credentials as kubectl
#If this script ran inside a Pod, you’d use: config.load_incluster_config()


#Creating the Kubernetes API client
apps_v1 = client.AppsV1Api() #Why AppsV1Api? DaemonSets belong to:apps/v1
# This client lets you:
            # List DaemonSets
            # Patch DaemonSets
            # Delete DaemonSets

# Namespace to target (use "all" for every namespace)
TARGET_NAMESPACE = "kube-system" #only system DaemonSets

# Fake nodeSelector that should match no nodes
FAKE_NODE_SELECTOR = {
    "nodeSelector": {
        "non-existent-node-label": "true"
    }
}

def scale_down_daemonsets(namespace):
    try:
        if namespace == "all":
            daemonsets = apps_v1.list_daemon_set_for_all_namespaces().items #gets every DaemonSet in the cluster
        else:
            daemonsets = apps_v1.list_namespaced_daemon_set(namespace).items #gets DaemonSets only in one namespace
            #.items gives you a Python list of DaemonSet objects.

        for ds in daemonsets: #ds contain name, namespace,spec, label, status we extract name and namespaces which are needed to patch
            name = ds.metadata.name
            ns = ds.metadata.namespace
    #Building the patch payload
            patch_body = {
                "spec": {
                    "template": {
                        "spec": FAKE_NODE_SELECTOR
                    }
                }
            }
#daemonset path now look like:
# DaemonSet
#  └─ spec
#     └─ template
#        └─ spec
#           └─ nodeSelector
# We are patching, not replacing, so:
            # Existing fields stay untouched
            # Only nodeSelector is added/overwritten


    #Patching the DaemonSet
            apps_v1.patch_namespaced_daemon_set( #Sends a PATCH request to the Kubernetes API
                name=name, #Updates the DaemonSet spec
                namespace=ns, #Triggers Kubernetes to: Kill existing Pods,Stop scheduling new ones
                body=patch_body
            )

            print(f"Scaled down DaemonSet: {name} (namespace: {ns})")

    except ApiException as e:
        print(f"API error: {e}")

if __name__ == "__main__":
    scale_down_daemonsets(TARGET_NAMESPACE)



#python3 -m pip install kubernetes
# apt-get update
# apt-get install -y python3-pip
# python3 -m pip --version
# python3 -m pip install kubernetes
# python3 filename.py

# kubectl get ds -n kube-system
# kubectl get pods -n kube-system



#theory
# A DaemonSet ensures that one Pod runs on every node (or every matching node).
# Common DaemonSets:
#         kube-proxy
#         coredns (sometimes)
#         log collectors
#         monitoring agents

#How do we “scale down” a DaemonSet?
# Since DaemonSets don’t use replicas, the trick is:
# Make the DaemonSet match zero nodes
# We do this by adding a nodeSelector that no node has.
# eg:
# nodeSelector:
#   non-existent-node-label: "true"
# Because no node has this label, Kubernetes:
# Deletes all DaemonSet Pods
# Keeps the DaemonSet object itself

# This is a safe and reversible way to stop DaemonSets.


#what script does

# Connects to a Kubernetes cluster
# Lists DaemonSets (in one namespace or all)
# Patches each DaemonSet
# Adds a fake nodeSelector
# Kubernetes removes all DaemonSet Pods automatically
