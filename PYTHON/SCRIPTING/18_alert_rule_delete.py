#Create Python Script to Retrieve and Delete All Alert Rules from Grafana via Grafana API

#Retrieves all alert rules from Grafana
#Deletes all alert rules using Grafana’s API

#logic
# Call Grafana API to fetch all alert rules
# Loop through:
    # folders
    # rule groups
    # rules
# Extract each rule’s UID
# Call the delete API for each rule UID
# Print confirmation for every deletion

import os
import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# ================= CONFIGURATION =================
GRAFANA_URL = os.getenv("GRAFANA_URL")
API_TOKEN = os.getenv("GRAFANA_TOKEN")
# =================================================

HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

def get_all_alert_rules(): #returns all alert rules in a nested dictionary format.
    """
    Fetch all alert rule folders, groups, and rules from Grafana
    """
    url = f"{GRAFANA_URL}/api/ruler/grafana/api/v1/rules"
    response = requests.get(url, headers=HEADERS, verify=False)
    response.raise_for_status()  # Raise error if request fails
    return response.json()

def delete_alert_rule(rule_uid, rule_name):
    """
    Delete a single alert rule using its UID
    """
    url = f"{GRAFANA_URL}/api/v1/provisioning/alert-rules/{rule_uid}"
    response = requests.delete(url, headers=HEADERS, verify=False)

    if response.status_code in (200, 204):
        print(f"Deleted alert rule: '{rule_name}' (UID: {rule_uid})")
    else:
        print(f"Failed to delete alert rule: '{rule_name}' (UID: {rule_uid}) | Status: {response.status_code}")

def delete_all_alert_rules():
    """
    Retrieve all alert rules and delete them one by one
    """
    rule_data = get_all_alert_rules()

    for folder, groups in rule_data.items():
        for group in groups:#Loops through each rule group in the current folder.
            for rule in group.get("rules", []):#ensures that if the "rules" key doesn’t exist, it will return an empty list instead of causing an error.
                grafana_alert = rule.get("grafana_alert", {})
                rule_uid = grafana_alert.get("uid")
                rule_name = rule_name = grafana_alert.get("title", "<no-name>")  # it search for name .. if there is no name it will return <no-name>

                if rule_uid:
                    delete_alert_rule(rule_uid, rule_name)
                else:
                    print(f"Skipping rule without UID: '{rule_name}'")

if __name__ == "__main__":
    delete_all_alert_rules()
    # rule_data = get_all_alert_rules()   
    # print(json.dumps(rule_data, indent=4))  #To check the json .how it is 
