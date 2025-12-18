#fetch 1 dashboard using uid
#uid=open ur dashboard u will see a number b/w /d/

import os
import requests
import json

GRAFANA_URL = os.getenv("GRAFANA_URL")
TOKEN = os.getenv("GRAFANA_TOKEN")

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

uid = "obcx2qt"   # put test UID here

url = f"{GRAFANA_URL}/api/dashboards/uid/{uid}"

response = requests.get(url, headers=headers,verify=False)

if response.status_code == 200:
    data = response.json()
    with open(f"{uid}.json", "w") as f:
        json.dump(data, f, indent=4)
    print(f"Saved dashboard {uid}.json")
else:
    print("Error:", response.status_code, response.text)
