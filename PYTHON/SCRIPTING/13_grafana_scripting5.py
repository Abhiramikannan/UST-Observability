# Python Script to Fetch Dashboards Using Metadata File
# and store the full dashboard JSON locally via Grafana API inside 'dashboards' folder

import os
import requests
import json
import urllib3

# -------------------------------
# Configuration
# -------------------------------

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

GRAFANA_URL = os.getenv("GRAFANA_URL")  # e.g., "https://grafana.example.com"
TOKEN = os.getenv("GRAFANA_TOKEN")      # Grafana API token

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

DASHBOARD_FOLDER = "./dashboards"  # Folder to save fetched dashboards

# -------------------------------
# Ensure folder exists
# -------------------------------
if not os.path.exists(DASHBOARD_FOLDER):
    os.makedirs(DASHBOARD_FOLDER)
    print(f"Folder '{DASHBOARD_FOLDER}' created.")

# -------------------------------
# Metadata file creation (example)
# -------------------------------
uids = [
    "obcx2qt",
    "obnmgjl",
    "obvxcmk",
    "obnjvxq"
]

# Save metadata file (if not already exists)
metadata_file = "metadata.txt"
with open(metadata_file, "w") as f:
    for uid in uids:
        f.write(uid + "\n")
print(f"Metadata file '{metadata_file}' written successfully.")

# -------------------------------
# Functions
# -------------------------------
def read_metadata():
    """Read UIDs from metadata file."""
    with open(metadata_file, "r") as f:
        return [line.strip() for line in f.readlines()]

def fetch_dashboard(uid):
    """Fetch dashboard JSON from Grafana API using UID."""
    url = f"{GRAFANA_URL}/api/dashboards/uid/{uid}"
    response = requests.get(url, headers=HEADERS, verify=False)

    if response.status_code != 200:
        print(f"❌ Failed: {uid} | Status: {response.status_code}")
        return None

    print(f"✔ Fetched dashboard: {uid}")
    return response.json()

def save_dashboard(uid, data):
    """Save dashboard JSON inside dashboards folder."""
    filename = os.path.join(DASHBOARD_FOLDER, f"{uid}.json")
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    print(f"📁 Saved: {filename}")

# -------------------------------
# Main
# -------------------------------
def main():
    uids = read_metadata()
    print(f"Found {len(uids)} dashboards in metadata file.")

    for uid in uids:
        data = fetch_dashboard(uid)
        if data:
            save_dashboard(uid, data)

# -------------------------------
# Run Script
# -------------------------------
if __name__ == "__main__":
    main()
