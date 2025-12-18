#administration->users and access -> service account -> create ->viewer
#add service acc token -> generate ->token will get generated
#script-token 


# # In PowerShell
# $env:GRAFANA_URL = "https://observabilityust.grafana.net"
# $env:GRAFANA_TOKEN = "#put ur token here in this quotes"

#verify
# echo $env:GRAFANA_URL
# echo $env:GRAFANA_TOKEN



#printing token and url
import os
grafana_url=os.getenv("GRAFANA_URL")
grafana_token=os.getenv("GRAFANA_TOKEN")

print("grafana url is: ",grafana_url)
print("grafana_token is: ",grafana_token)
