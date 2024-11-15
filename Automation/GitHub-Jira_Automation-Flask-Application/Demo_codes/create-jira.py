import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://raghul-tech.atlassian.net/rest/api/3/issue"

API_TOKEN="Your Api token"

auth = HTTPBasicAuth("Your email ID", API_TOKEN)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "My first jira ticket",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    "project": {
      "key": "RAG"
    },
    "issuetype": {
      "id": "10001"
    },
    "summary": "First JIRA Ticket",
  },
  "update": {}
} )
  
   

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))