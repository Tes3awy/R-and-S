# imports
import requests
from requests.auth import HTTPBasicAuth as BasicAuth

# inputs
url = "https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"
username = "devnetuser"
password = "Cisco123!"
headers = {"Content-Type": "application/json", "Accept": "application/json"}

# processing
r = requests.post(url, headers=headers, auth=BasicAuth(username, password))

# output
token = r.json()["Token"]
print(token)
