#Find crashing pods and restart it.


import subprocess #lets Python run terminal commands
import json#lets Python read Kubernetes output (which is in JSON)

NAMESPACE = "default" #Only look at pods inside the default namespace.

def get_pods(namespace):#Get a list of all pods in a namespace.
    cmd = [
        "kubectl", "get", "pods",
        "-n", namespace,
        "-o", "json"
    ]
    result = subprocess.run(cmd, capture_output=True, text=True) #saves the output instead of printing it
    return json.loads(result.stdout)["items"] #Kubernetes returns JSON text,json.loads() converts text → Python data,"items" is the list of pods
#This function returns a list of pods

def is_crashing(pod):
    statuses = pod["status"].get("containerStatuses", [])
    for c in statuses:
        state = c.get("state", {})
        if "waiting" in state and state["waiting"].get("reason") == "CrashLoopBackOff":
            return True
    return False

def delete_pod(name, namespace):
    subprocess.run([
        "kubectl", "delete", "pod",
        name, "-n", namespace
    ])

pods = get_pods(NAMESPACE)

for pod in pods:
    name = pod["metadata"]["name"]
    if is_crashing(pod):
        print(f"Deleting crashing pod: {name}")
        delete_pod(name, NAMESPACE)




# apiVersion: apps/v1
# kind: Deployment
# metadata:
#   name: crash-deployment
#   labels:
#     app: crash-test
# spec:
#   replicas: 1
#   selector:
#     matchLabels:
#       app: crash-test
#   template:
#     metadata:
#       labels:
#         app: crash-test
#     spec:
#       containers:
#         - name: crash-container
#           image: busybox
#           command: ["/bin/sh", "-c", "echo Crashing... && sleep 2 && exit 1"]

#kubectl apply -f deployment.yaml
