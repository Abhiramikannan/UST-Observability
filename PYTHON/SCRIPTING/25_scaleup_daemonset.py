#13. Create Python Script to scale up Kubernetes DaemonSets that were previously scaled down by removing the artificial nodeSelector key that prevented them from scheduling pods using the backup

#!/usr/bin/env python3


#what the code does?
    # Finds DaemonSets
    # Checks if they contain a specific nodeSelector key
    # Removes that key
    # Patches the DaemonSet so pods start running again


import argparse # can pass command line arguments -> using --dry-run or --namespace in python run command.
from kubernetes import client, config
from kubernetes.client.rest import ApiException


def load_kube_config():
    try:
        config.load_kube_config() #local machine
    except Exception:
        config.load_incluster_config() # inside pod


def process_daemonset(ds, namespace, key_to_remove, apps_api, dry_run=False): #ds=daemonset object
    node_selector = (
        ds.spec.template.spec.node_selector or {} #fetches nodeselector , If it’s None, uses an empty dictionary
    )

    if key_to_remove not in node_selector:
        return False

    print(f"✔ Restoring DaemonSet: {namespace}/{ds.metadata.name}")

    # Remove artificial selector
    node_selector.pop(key_to_remove) #Remove artificial selector

    patch_body = {
        "spec": {
            "template": {
                "spec": {
                    "nodeSelector": node_selector if node_selector else None
                }
            }
        }
    }

    if dry_run:
        print("  ↳ Dry run: no changes applied")
        return True

    apps_api.patch_namespaced_daemon_set(
        name=ds.metadata.name,
        namespace=namespace,
        body=patch_body,
    )

    return True


def main():
    parser = argparse.ArgumentParser(
        description="Restore DaemonSets by removing an artificial nodeSelector key" #read the command line
    )
    #These all required in the command line .
    parser.add_argument(
        "--node-selector-key",
        required=True,
        help="NodeSelector key to remove (e.g. backup-disabled)",
    )
    parser.add_argument(
        "--namespace",
        default=None,
        help="Namespace to target (default: all namespaces)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would change without applying patches",
    )

#Read arguments from command line
    args = parser.parse_args()

    load_kube_config()
    apps_api = client.AppsV1Api()

    restored = 0 #This is just a counter., How many daemon sets were succesfully restored.

    if args.namespace:
        daemonsets = apps_api.list_namespaced_daemon_set(args.namespace).items #“Give me all DaemonSets in kube-system” namespace .
        #daemonsets = [kube-proxy, coredns, metrics-server]

        namespaces = [(args.namespace, daemonsets)] #namespaces = [("kube-system", daemonsets)]
#         #namespace will become:
# [
#    ("kube-system", [ds1, ds2, ds3])
# ]
#This is done so the next loop can treat both single-namespace and all-namespaces in the same way.


#if user didnt give namespace , args.namespace = None

    else:
        namespaces = [
            (ns.metadata.name,
             apps_api.list_namespaced_daemon_set(ns.metadata.name).items)
            for ns in client.CoreV1Api().list_namespace().items
        ]
#explanation of else condition:
#client.CoreV1Api().list_namespace().items
        #ask kubernetes to “Give me all namespaces in the cluster”

    #output:
            # [
            #   Namespace(default),
            #   Namespace(kube-system),
            #   Namespace(monitoring)
            # ]
#what is ns.metadata.name?
# | Namespace object       | ns.metadata.name |
# | ---------------------- | ---------------- |
# | Namespace(default)     | "default"        |
# | Namespace(kube-system) | "kube-system"    |
# | Namespace(monitoring)  | "monitoring"     |


#apps_api.list_namespaced_daemon_set(ns.metadata.name).items
        #give all daemonsets in the namespace.
    #output:
        # | Namespace   | Result                |
        # | ----------- | --------------------- |
        # | default     | [ds1, ds2]            |
        # | kube-system | [kube-proxy, coredns] |
        # | monitoring  | [node-exporter]       |


#why tuple is created?
        # (ns.metadata.name,
        #  apps_api.list_namespaced_daemon_set(ns.metadata.name).items)
        #Builds a pair like this:
            # ("default", [ds1, ds2])
            # ("kube-system", [kube-proxy, coredns])
            # ("monitoring", [node-exporter])


#Final result of list comprehension:
        # namespaces = [
        #    ("default", [ds1, ds2]),
        #    ("kube-system", [kube-proxy, coredns]),
        #    ("monitoring", [node-exporter])
        # ]

#(namespace_name, list_of_daemonsets)

    for namespace, daemonsets in namespaces:#This means: namespace → "default",daemonsets → [ds1, ds2],Then next iteration:namespace → "kube-system", daemonsets → [ds3, ds4].So we are processing one namespace at a time.
        for ds in daemonsets: #Now we go DaemonSet by DaemonSet inside that namespace.
#execution order becomes:
# default/ds1
# default/ds2
# kube-system/ds3
# kube-system/ds4
# monitoring/ds5

            try:
                if process_daemonset(
                    ds,
                    namespace,
                    args.node_selector_key,
                    apps_api,
                    args.dry_run,
                ):
                    restored += 1
            except ApiException as e:
                print(
                    f"✖ Failed to update {namespace}/{ds.metadata.name}: {e.reason}"
                )

    print(f"\nDone. Restored {restored} DaemonSet(s).")


if __name__ == "__main__":
    main()




#RUN
# sudo apt update
# sudo apt install -y python3-pip
# python3 -m pip --version
# python3 -m pip install kubernetes

#python3 27_scaleup_daemonset.py.py --node-selector-key fake-key --namespace kube-system


#Explanation:
# What process_daemonset() does:
# Checks if the DaemonSet has the fake nodeSelector key
# If not present → returns False
# If present:
# Removes the key
# Patches the DaemonSet
# Returns True
