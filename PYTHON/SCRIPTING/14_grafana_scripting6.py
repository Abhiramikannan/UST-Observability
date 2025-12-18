#upload all the json files to grafana


# upload_grafana_dashboards.py
import os
import json
import requests
import urllib3

# -------------------------------
# Configuration
# -------------------------------

# Disable SSL warnings (useful for self-signed certs)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Grafana API URL and token
GRAFANA_URL = os.getenv("GRAFANA_URL")  # e.g., "https://grafana.example.com"
TOKEN = os.getenv("GRAFANA_TOKEN")     

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

DASHBOARD_FOLDER = "./dashboards"  # Folder containing JSON dashboard files

# -------------------------------
# Ensure dashboard folder exists
# -------------------------------
if not os.path.exists(DASHBOARD_FOLDER):
    os.makedirs(DASHBOARD_FOLDER)
    print(f"Folder '{DASHBOARD_FOLDER}' created. Place your JSON dashboard files here and re-run the script.")
    exit(0)

# -------------------------------
# Functions
# -------------------------------
def load_dashboard_file(file_path):
    """Load JSON dashboard from a file."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        print(f"❌ Failed to parse JSON '{file_path}': {e}")
        return None

def upload_dashboard(dashboard_json):
    """Upload a dashboard to Grafana API."""
    url = f"{GRAFANA_URL}/api/dashboards/db"

    # Handle exported dashboards with nested 'dashboard' key
    if "dashboard" in dashboard_json:
        dashboard = dashboard_json["dashboard"]
    else:
        dashboard = dashboard_json

    # Ensure dashboard has a title
    if "title" not in dashboard or not dashboard["title"]:
        dashboard["title"] = dashboard.get("uid", "Untitled Dashboard")

    payload = {
        "dashboard": dashboard,
        "overwrite": True
    }

    try:
        response = requests.post(url, headers=HEADERS, json=payload, verify=False)
        if response.status_code in [200, 201]:
            print(f"✔ Uploaded: {dashboard['title']}")
        else:
            print(f"❌ Failed ({response.status_code}): {dashboard['title']}")
            print(response.text)
    except requests.RequestException as e:
        print(f"❌ Error uploading dashboard '{dashboard.get('title', 'Unknown')}': {e}")

def main():
    # List all JSON files in dashboard folder
    files = [f for f in os.listdir(DASHBOARD_FOLDER) if f.endswith(".json")]
    if not files:
        print(f"No JSON files found in '{DASHBOARD_FOLDER}'. Add your dashboard JSON files and re-run the script.")
        return

    print(f"Found {len(files)} dashboard JSON file(s) to upload.")

    # Upload each dashboard
    for file_name in files:
        file_path = os.path.join(DASHBOARD_FOLDER, file_name)
        dashboard_json = load_dashboard_file(file_path)
        if dashboard_json:
            upload_dashboard(dashboard_json)

# -------------------------------
# Run Script
# -------------------------------
if __name__ == "__main__":
    main()
