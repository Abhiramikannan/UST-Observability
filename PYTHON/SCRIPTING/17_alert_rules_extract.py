#fetch alert rules from grafana.


import os
import json
import requests

# ================= CONFIGURATION =================
GRAFANA_URL = os.getenv("GRAFANA_URL")
API_TOKEN = os.getenv("GRAFANA_TOKEN")

OUTPUT_DIR = "grafana_alert_rules"
# =================================================

HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

def sanitize_name(name: str) -> str:
    """Make safe filenames"""
    return name.replace("/", "_").replace(" ", "_")

def get_alert_rule_groups(): #returns foldernames, rule groups inside it, alert rules inside each grp
    url = f"{GRAFANA_URL}/api/ruler/grafana/api/v1/rules"
    response = requests.get(url, headers=HEADERS,verify=False)
    response.raise_for_status()
    return response.json()

def export_rules():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    rule_groups = get_alert_rule_groups() #getting that folder area..getting all alert rule folders, groups, and rules”..Folder names,Rule groups inside each folder,Alert rules inside each group

    for folder, groups in rule_groups.items():  
    # folder  -> Grafana folder name (string)
    # groups  -> list of rule groups inside that folder

        folder_name = sanitize_name(folder)  
        # makes the Grafana folder name safe for filesystem (replaces / and spaces)

        folder_path = os.path.join(OUTPUT_DIR, folder_name)  
        # builds the full path: grafana_alert_rules/<folder_name>

        os.makedirs(folder_path, exist_ok=True)  
        # creates the folder directory if it does not exist


        for group in groups:
            # group -> one rule group inside the current Grafana folder

            group_name = sanitize_name(group["name"])
            # takes the rule group name and makes it safe for filesystem
            # (replaces / and spaces with _)

            group_path = os.path.join(folder_path, group_name)
            # builds path: grafana_alert_rules/<folder_name>/<group_name>

            os.makedirs(group_path, exist_ok=True)
            # creates the rule group directory if it does not exist


            for rule in group.get("rules", []): #Tries to get the list of alert rule.. from each group
                    #If "rules" does not exist, returns an empty list []
                    #  Prevents the script from crashing
                rule_name = sanitize_name(rule.get("title", "unnamed_rule")) #rule.get("title", "unnamed_rule")
                        # Gets the alert rule’s title
                        # If missing → uses "unnamed_rule"
                file_path = os.path.join(group_path, f"{rule_name}.json") # creates a file with that rule name.json in that path

                with open(file_path, "w", encoding="utf-8") as f:
                    json.dump(rule, f, indent=2)  #Writes the entire alert rule dictionary

                print(f"Exported: {file_path}")

if __name__ == "__main__":
    export_rules()
