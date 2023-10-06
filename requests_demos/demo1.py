# Imports
from pprint import pprint

import requests
from requests.auth import HTTPBasicAuth as BasicAuth

# Inputs
url = "https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"
username = "devnetuser"
password = "Cisco123!"
headers = {"Content-Type": "application/json", "Accept": "application/json"}

# Processing
r = requests.post(url, headers=headers, auth=BasicAuth(username, password))

# Output
token = r.json()["Token"]
pprint(token, indent=4)

