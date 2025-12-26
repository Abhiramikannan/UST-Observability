#Create Python Script to fetch dashboards, folders, and datasources metadata from Grafana and store them in structured JSON files

import requests
import json
import os
from datetime import datetime, timezone

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# ==========================
# CONFIGURATION
# ==========================
GRAFANA_URL = os.getenv("GRAFANA_URL")
API_TOKEN = os.getenv("GRAFANA_TOKEN")

OUTPUT_DIR = "grafana_metadata"

HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

# ==========================
# UTILITY FUNCTIONS
# ==========================
def make_request(endpoint):
    url = f"{GRAFANA_URL}{endpoint}"
    response = requests.get(url, headers=HEADERS, verify=False)
    if response.status_code != 200:
        print("ERROR URL:", url)
        print("STATUS:", response.status_code)
        print("RESPONSE:", response.text)

    response.raise_for_status()
    return response.json()

def save_json(filename, data):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    filepath = os.path.join(OUTPUT_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"Saved: {filepath}")

# ==========================
# FETCH FUNCTIONS
# ==========================
def fetch_folders():
    print("Fetching folders...")
    return make_request("/api/folders")

def fetch_datasources():
    print("Fetching datasources...")
    return make_request("/api/datasources")

def fetch_dashboards():
    print("Fetching dashboards metadata...")
    dashboards = [] #emptybox,I will put dashboard information here one by one.

    # Search all dashboards
    search_results = make_request("/api/search?type=dash-db")#his calls Grafana’s API, shows list of dashboards.

    for item in search_results:#Loop through each dashboard,item is one dashboard summary.
        uid = item.get("uid") #getting uid, .get is used because it is more safer,Won’t crash if key is missing
        if not uid:
            continue #if uid missing, skip the dashboard and move to next one.

        dashboard_detail = make_request(f"/api/dashboards/uid/{uid}") #Fetch full dashboard details(metadata,actual dashboard json)
        dashboards.append({ #You create a clean dictionary with only needed fields.
            "id": item.get("id"),
            "uid": uid,
            "title": item.get("title"),
            "folderId": item.get("folderId"),
            "folderTitle": item.get("folderTitle"),
            "url": item.get("url"),
            "tags": item.get("tags"),
            "isStarred": item.get("isStarred"),
            "created": dashboard_detail["meta"].get("created"),
            "updated": dashboard_detail["meta"].get("updated"),
            "createdBy": dashboard_detail["meta"].get("createdBy"),
            "updatedBy": dashboard_detail["meta"].get("updatedBy"),
            "version": dashboard_detail["dashboard"].get("version"),
            "schemaVersion": dashboard_detail["dashboard"].get("schemaVersion")
        }) #Then this dictionary is added to the list:

    return dashboards #Sends the full list back to whoever called the function.

# ==========================
# MAIN EXECUTION
# ==========================
def main(): #Runs everything in the correct order
    metadata = {
        "exported_at": datetime.now(timezone.utc).isoformat(), #when export happened
        "grafana_url": GRAFANA_URL #which grafana instance
    }

    folders = fetch_folders()
    datasources = fetch_datasources()
    dashboards = fetch_dashboards()
    #Each returns Python lists.

    save_json("folders.json", {
        **metadata,#**metadata means:Insert exported_at and grafana_url here
        "folders": folders
    })

    save_json("datasources.json", {
        **metadata,
        "datasources": datasources
    })

    save_json("dashboards.json", {
        **metadata,
        "dashboards": dashboards
    })

    print("Grafana metadata export completed successfully.")

if __name__ == "__main__":#Run main() only when this file is executed directly.
    main()
