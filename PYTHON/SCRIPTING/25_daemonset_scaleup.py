#13. Create Python Script to scale up Kubernetes DaemonSets that were previously scaled down by removing the artificial nodeSelector key that prevented them from scheduling pods using the backup
#“DaemonSets don’t need a backup because the fake nodeSelector is reversible — removing it restores the original scheduling automatically.”

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

    restored = 0

    if args.namespace:
        daemonsets = apps_api.list_namespaced_daemon_set(args.namespace).items
        namespaces = [(args.namespace, daemonsets)]
    else:
        namespaces = [
            (ns.metadata.name,
             apps_api.list_namespaced_daemon_set(ns.metadata.name).items)
            for ns in client.CoreV1Api().list_namespace().items
        ]

    for namespace, daemonsets in namespaces:
        for ds in daemonsets:
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
