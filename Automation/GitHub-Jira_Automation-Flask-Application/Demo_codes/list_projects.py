# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://raghul-tech.atlassian.net/rest/api/3/project"

API_TOKEN="Your Api token"

auth = HTTPBasicAuth("Your email ID", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

output = json.loads(response.text)

for i in range(0,3):
    name= output[i]["name"]
    key=  output[i]["key"]
    print(f"Name of Project {i}: ",name)
    print(f"key of Project  {i}: ",key)
    print("******")



# print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))