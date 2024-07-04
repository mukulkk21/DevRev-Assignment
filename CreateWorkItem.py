import requests
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Define your DevRev API endpoint and token
api_endpoint = 'https://api.devrev.ai/works.create'
api_token = os.getenv('PAT')

# Define the payload for the work item
payload = {
    "type": "issue",
    "applies_to_part": "PROD-1",
    "owned_by": ["don:identity:dvrv-in-1:devo/2okdMmZBbb:devu/1"],
    "title": "Creation of issue"
}

# Set up the headers
headers = {
    "Authorization": f"Bearer {api_token}",
    "Content-Type": "application/json"
}

# Make the request to create the work item
response = requests.post(api_endpoint, json=payload, headers=headers)

if response.status_code == 200:
    print('Work item created successfully.')
    print('Response:', response.json())
else:
    print('Failed to create work item.')
    print('Error:', response.json() if response.content else response.reason)
