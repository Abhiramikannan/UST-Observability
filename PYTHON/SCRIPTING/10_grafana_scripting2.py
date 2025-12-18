#Call Grafana API Using Token
#to test ur authentication
# Bearer <TOKEN>
#Bearer is a standard keyword used in HTTP to say:“This request contains a token.
# means your token is being used as a form of authentication.

import os
import requests

GRAFANA_URL = os.getenv("GRAFANA_URL")
GRAFANA_TOKEN = os.getenv("GRAFANA_TOKEN")


#we will tell grafana we are an authorized user enn
headers = {
    "Authorization": f"Bearer {GRAFANA_TOKEN}",
    "Content-Type": "application/json" #Any data I send you will be in JSON format.”
}

url = f"{GRAFANA_URL}/api/search" #Grafana API endpoint to list dashboards

# Disable SSL verification (temporary)
response = requests.get(url, headers=headers, verify=False)

print("Status Code:", response.status_code)
print("Response:", response.json())




