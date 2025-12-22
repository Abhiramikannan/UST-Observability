#fetch alert rules from grafana.


import os
import json
import requests

# ================= CONFIGURATION =================
GRAFANA_URL = "https://observabilityust.grafana.net"
API_TOKEN = "YOUR_API_TOKEN_HERE"

OUTPUT_DIR = "grafana_alert_rules"
# =================================================

HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

def sanitize_name(name: str) -> str:
    """Make safe filenames"""
    return name.replace("/", "_").replace(" ", "_")

def get_alert_rule_groups():
    url = f"{GRAFANA_URL}/api/ruler/grafana/api/v1/rules"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json()

def export_rules():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    rule_groups = get_alert_rule_groups()

    for folder, groups in rule_groups.items():
        folder_name = sanitize_name(folder)
        folder_path = os.path.join(OUTPUT_DIR, folder_name)
        os.makedirs(folder_path, exist_ok=True)

        for group in groups:
            group_name = sanitize_name(group["name"])
            group_path = os.path.join(folder_path, group_name)
            os.makedirs(group_path, exist_ok=True)

            for rule in group.get("rules", []):
                rule_name = sanitize_name(rule.get("title", "unnamed_rule"))
                file_path = os.path.join(group_path, f"{rule_name}.json")

                with open(file_path, "w", encoding="utf-8") as f:
                    json.dump(rule, f, indent=2)

                print(f"Exported: {file_path}")

if __name__ == "__main__":
    export_rules()
