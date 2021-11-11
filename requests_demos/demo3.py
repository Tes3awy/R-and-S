# imports
from datetime import date

import requests
import xlsxwriter
from requests.auth import HTTPBasicAuth as BasicAuth

# inputs
url = "https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"
username = "devnetuser"
password = "Cisco123!"
headers = {"Content-Type": "application/json", "Accept": "application/json"}

# processing
try:
    r = requests.post(url, headers=headers, auth=BasicAuth(username, password))
    r.raise_for_status()  # raise the exception if HTTP Status Code is NOT 200
except Exception as e:
    raise SystemExit(e)
else:
    print("Successfully authenticated and generated a token")
    # output
    token = r.json()["Token"]

    # inputs
    url = "https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device"
    headers = {"X-Auth-Token": token, **headers}

    # processing
    r = requests.get(url, headers=headers)

    print("Received the device list facts from DNA")

    # output
    facts = r.json()["response"]

    # the header row
    header = {
        "A1": "Device Hostname",
        "B1": "MGMT IP Address",
        "C1": "Serial Number",
        "D1": "Software Version",
        "E1": "Device Model",
        "F1": "Device Role",
    }

    # create a workbook and add a worksheet
    wb = xlsxwriter.Workbook(f"DNA-Devices-Facts_{date.today()}.xlsx")
    ws = wb.add_worksheet("DNA Devices Facts")

    # write the header in the worksheet
    for cell, value in header.items():
        ws.write(cell, value)

    # fine tune the worksheet
    ws.autofilter("A1:F1")
    ws.freeze_panes(1, 2)

    row, col = 1, 0

    # write the facts in the worksheet
    for fact in facts:
        ws.write(row, col + 0, fact["hostname"])
        ws.write(row, col + 1, fact["managementIpAddress"])
        ws.write(row, col + 2, fact["serialNumber"])
        ws.write(row, col + 3, fact["softwareVersion"])
        ws.write(row, col + 4, fact["platformId"])
        ws.write(row, col + 5, fact["role"])

        # jump to next row
        row += 1

    # save the workbook
    wb.close()
    print("Successfully created the workbook")

    print("SUCCESS")
