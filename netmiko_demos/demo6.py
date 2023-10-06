# Imports
from datetime import date

import xlsxwriter
from netmiko import ConnectHandler

# Inputs
devices = [
    {
        "device_type": "cisco_ios",
        "ip": "sandbox-iosxe-latest-1.cisco.com",
        "username": "admin",
        "password": "C1sco12345",
        "fast_cli": False,
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.150",
        "username": "cisco",
        "password": "cisco",
        "fast_cli": False,
    },
]

# Create a Workbook (Equivalent to creating a Excel file)
wb = xlsxwriter.Workbook(f"Devices-Interface-Brief_{date.today()}.xlsx")

# define a header line in the worksheet
header = {
    "A1": "Interface Name",  # 0
    "B1": "IP Address",  # 1
    "C1": "Status (L1 Status)",  # 2
    "D1": "Protocol (L2 Status)",  # 3
}

# Processing

# Create a connection instance to each network device
# one by one
for device in devices:
    print(f"Trying {device['ip']}...", end="\r")
    with ConnectHandler(**device) as conn:
        print(f"Connected to {conn.host}:{conn.port}")
        intfs_brief = conn.send_command("show ip interface brief", use_textfsm=True)

    print(f"Collected interfaces brief of {device['ip']} & closed connection")

    # Create seperate sheet of show ip interface brief command
    # for each device in the same Excel file
    ws = wb.add_worksheet(device["ip"][:31])  # Max sheet name is 31 chars

    # Write the header line in the worksheet
    for cell, val in header.items():
        ws.write(cell, val)

    # add fine tunings to the worksheet
    ws.autofilter("A1:D1")
    ws.freeze_panes(1, 1)

    row, col = 1, 0

    print(f"Writing data of {device['ip']} in the Excel sheet...")
    for intf in intfs_brief:
        ws.write(row, col + 0, intf["intf"])  # Column A
        ws.write(row, col + 1, intf["ipaddr"])  # Column B
        ws.write(row, col + 2, intf["status"])  # Column C
        ws.write(row, col + 3, intf["proto"])  # Column D

        # Jump to the next row
        row += 1

    print(f"Data of {device['ip']} written successfully")

# close the Excel file (Save the file)
wb.close()
print("SUCCESS")

