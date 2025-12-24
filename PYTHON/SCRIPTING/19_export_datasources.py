#Create Python Script to Fetch and Store Grafana Data Sources as JSON Files via Grafana API

import os
import json
import re
import requests

# ================= CONFIGURATION =================
GRAFANA_URL = os.getenv("GRAFANA_URL")
API_TOKEN = os.getenv("GRAFANA_TOKEN")
OUTPUT_DIR = "grafana_datasources"
# =================================================

if not GRAFANA_URL or not API_TOKEN:
    raise SystemExit("GRAFANA_URL and GRAFANA_TOKEN must be set")

HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

def sanitize_name(name: str) -> str:
    """Make filesystem-safe filenames"""
    return re.sub(r'[^a-zA-Z0-9_.-]', '_', name) #Any character that is NOT one of those in a-zA-Z0-9_.- will be replaced by _

def get_datasources():
    """Fetch all Grafana data sources"""
    url = f"{GRAFANA_URL}/api/datasources"
    response = requests.get(url, headers=HEADERS, timeout=30, verify=False)
    response.raise_for_status()
    return response.json()

def export_datasources():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    datasources = get_datasources() 

    for ds in datasources: #Loop through each datasource
        ds_name = sanitize_name(ds.get("name", "unnamed_datasource")) #If "name" doesn’t exist, uses "unnamed_datasource",sanitize_name() replaces unsafe characters so it can be used as a filename
        file_path = os.path.join(OUTPUT_DIR, f"{ds_name}.json")

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(ds, f, indent=2)

        print(f"Exported: {file_path}")

if __name__ == "__main__":
    export_datasources()
    print("\n Grafana data sources export completed.")
