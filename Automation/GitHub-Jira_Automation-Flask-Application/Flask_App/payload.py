import json

# Define a JSON string
json_string = '''

   Load your Github Weebhook request 

'''

# Parse the JSON string into a Python dictionary
json_data = json.loads(json_string)


# Access the "body" field within the "comment" object
comment_body = json_data.get("comment", {}).get("body", "")

# Print the "body" field
print("Comment Body:", comment_body)




