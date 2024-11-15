from requests.auth import HTTPBasicAuth
import json
from flask import Flask
import requests

app = Flask(__name__)

# Define a route that handles GET requests
@app.route('/createJira', methods=['POST'])
def createJira():
    
    
    url = "https://raghul-tech.atlassian.net/rest/api/3/issue"

    API_TOKEN="YOUR TOKEN"

    
    auth = HTTPBasicAuth("Your mail id", API_TOKEN)

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
                            "text": "Order entry fails when selecting supplier.",
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
        "summary": "JIRA Ticket",
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
    

    if output["body"] == "/jira" 
    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)