# Imports
from pprint import pprint

import requests
from requests.auth import HTTPBasicAuth as BasicAuth
from requests.exceptions import HTTPError

# Inputs
URL = "https://sandboxdnac2.cisco.com/dna/system/api/v1/auth/token"
username = "devnetuser"
password = "Cisco123!"
HEADERS = {"Content-Type": "application/json", "Accept": "application/json"}

# Processing
try:
    r = requests.post(URL, headers=HEADERS, auth=BasicAuth(username, password))
    r.raise_for_status()
# handle errors
except HTTPError as e:
    raise SystemExit(e) from e  # Stop execution if POST request fails to get a token
# print results only if not errors found
else:
    # Output
    token = r.json()["Token"]
    pprint(token)
