#list all dashboard and uids
import os
import requests

GRAFANA_URL = os.getenv("GRAFANA_URL")
TOKEN = os.getenv("GRAFANA_TOKEN")

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

url = f"{GRAFANA_URL}/api/search"

response = requests.get(url, headers=headers, verify=False)

if response.status_code == 200:
    dashboards = response.json()
    for d in dashboards:
        print(f"Title: {d['title']}, UID: {d['uid']}")
else:
    print("Error:", response.status_code, response.text)
