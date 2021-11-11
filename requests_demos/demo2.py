# imports
import requests
from requests.auth import HTTPBasicAuth as BasicAuth

# inputs
url = "https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"
username = "devnetuser"
password = "Cisco123!"
headers = {"Content-Type": "application/json", "Accept": "application/json"}

# processing
try:
    r = requests.post(url, headers=headers, auth=BasicAuth(username, password))
    r.raise_for_status()
# handle errors
except Exception as e:
    raise SystemExit(e)
# print results only if not errors found
else:
    # output
    token = r.json()["Token"]
    print(token)
