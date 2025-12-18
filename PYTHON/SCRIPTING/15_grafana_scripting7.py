#fetch the dashboard json files from grafana without using a file to store uid manually and doing
#fetch directly from grafana
import os
import requests
import json
import urllib3
import re

# -------------------------------
# Configuration
# -------------------------------

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

GRAFANA_URL = os.getenv("GRAFANA_URL")     # example: "https://grafana.example.com"
TOKEN = os.getenv("GRAFANA_TOKEN")         # Grafana API token

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

DASHBOARD_FOLDER = "./dashboards"

# -------------------------------
# Ensure folder exists
# -------------------------------
if not os.path.exists(DASHBOARD_FOLDER):
    os.makedirs(DASHBOARD_FOLDER)
    print(f"Folder '{DASHBOARD_FOLDER}' created.")

# -------------------------------
# Helper Functions
# -------------------------------

def sanitize_filename(name):
    """Remove invalid filesystem characters."""
    return re.sub(r'[\\/*?:"<>|]', "_", name)

def get_all_dashboards():
    """Fetch list of all dashboards from Grafana."""
    url = f"{GRAFANA_URL}/api/search?type=dash-db"
    response = requests.get(url, headers=HEADERS, verify=False)

    if response.status_code != 200:
        print(f"❌ Failed to list dashboards. Status: {response.status_code}")
        return []

    dashboards = response.json()
    print(f"✔ Found {len(dashboards)} dashboards.")
    return dashboards

def fetch_dashboard(uid):
    """Fetch full dashboard JSON using UID."""
    url = f"{GRAFANA_URL}/api/dashboards/uid/{uid}"
    response = requests.get(url, headers=HEADERS, verify=False)

    if response.status_code != 200:
        print(f"❌ Failed to fetch dashboard {uid}. Status: {response.status_code}")
        return None

    return response.json()

def save_dashboard(title, uid, data):
    """Save dashboard JSON using title as filename."""
    safe_title = sanitize_filename(title)
    filename = os.path.join(DASHBOARD_FOLDER, f"{safe_title}.json")

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print(f"📁 Saved: {filename}")

# -------------------------------
# Main Script
# -------------------------------
def main():
    dashboards = get_all_dashboards()

    for item in dashboards:
        uid = item.get("uid")
        title = item.get("title")

        if not uid or not title:
            continue

        print(f"Fetching: {title} ({uid})")

        data = fetch_dashboard(uid)
        if data:
            save_dashboard(title, uid, data)

# -------------------------------
# Run Script
# -------------------------------
if __name__ == "__main__":
    main()
