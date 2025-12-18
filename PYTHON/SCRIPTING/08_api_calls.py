#get
import requests
response = requests.get("https://api.restful-api.dev/objects?id=3&id=5&id=10", verify=False)
print(response.status_code, response.text)




url = "https://api.github.com"
response = requests.get(url,verify=False)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())
