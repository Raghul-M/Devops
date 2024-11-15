from requests.auth import HTTPBasicAuth
import json
from flask import Flask, request
import requests

app = Flask(__name__)

# Define a route that handles POST requests
@app.route('/createJira', methods=['POST'])
def createJira():
    # Get the JSON payload from the GitHub webhook
    payload = request.json

    # Access the "comment" object and its "body" field
    comment_body = payload.get("comment", {}).get("body", "")

    # Print the comment body
    print("Comment Body:", comment_body)

    # Check if the payload contains the desired condition (e.g., "/jira" in the body)
    if "/jira" in comment_body:
        url = "https://raghul-tech.atlassian.net/rest/api/3/issue"
        API_TOKEN="YOUR TOKEN"

    
        auth = HTTPBasicAuth("Your mail id", API_TOKEN)

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        jira_payload = {
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
        }

        response = requests.request(
            "POST",
            url,
            data=json.dumps(jira_payload),
            headers=headers,
            auth=auth
        )

        return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

    # If the condition is not met, return a response
    return "No JIRA issue created"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
