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
        "device_type": "cisco_ios_telnet",
        "ip": "192.168.1.150",
        "username": "cisco",
        "password": "cisco",
        "fast_cli": False,
    },
]

# Create an Excel Workbook (Equivalent to creating a Excel file)
wb = xlsxwriter.Workbook(f"Devices-Facts_{date.today()}.xlsx")
# Create a worksheet (Equivalent to creating a sheet within the Excel file)
ws = wb.add_worksheet("Device Facts")

# define a header line in the worksheet
header = {
    "A1": "Device Hostname",  # 0
    "B1": "MGMT IP Address",  # 1
    "C1": "Serial Number",  # 2
    "D1": "Device Model",  # 3
    "E1": "Software Version",  # 4
    "F1": "Last Reload Reason",  # 5
    "G1": "Uptime",  # 6
    "H1": "Config Register",  # 7
}

# write the header line in the worksheet
for cell, val in header.items():
    ws.write(cell, val)

for device in devices:
    # Create a connection instance to each network device
    print(f"Trying {device['ip']}...", end="\r")
    with ConnectHandler(**device) as conn:
        print(f"Connected to {conn.host}:{conn.host}")
        facts = conn.send_command("show version", use_textfsm=True)

    print(f"Collected facts of {conn.host} successfully & closed connection")

    # Save parsed output of show version command of each device in the same
    # Excel sheet

    row, col = 1, 0

    print(f"Writing data of {device['ip']} in the Excel sheet...")
    for fact in facts:
        ws.write(row, col + 0, fact["hostname"])
        ws.write(row, col + 1, device["ip"])  # Notice device['ip']!
        # str() is needed to convert the list to str
        ws.write(row, col + 2, str(fact["serial"]))
        # str() is needed to convert the list to str
        ws.write(row, col + 3, str(fact["hardware"]))
        ws.write(row, col + 4, fact["version"])
        ws.write(row, col + 5, fact["reload_reason"])
        ws.write(row, col + 6, fact["uptime"])
        ws.write(row, col + 7, fact["config_register"])

        # Jump to the next row
        row += 1

    print(f"Data of {device['ip']} written successfully")

# Close the Excel file (Save the file)
wb.close()
print("SUCCESS")

