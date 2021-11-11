from datetime import date

import xlsxwriter
from netmiko import ConnectHandler

# inputs

devices = [
    {
        "device_type": "cisco_ios",
        "ip": "sandbox-iosxe-latest-1.cisco.com",
        "username": "developer",
        "password": "C1sco12345",
        "secret": "",
        "fast_cli": False,
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.150",
        "username": "cisco",
        "password": "cisco",
        "secret": "",
        "fast_cli": False,
    },
]

# create a Workbook (Equivalent to creating a Excel file)
wb = xlsxwriter.Workbook(f"Devices-Interface-Brief_{date.today()}.xlsx")

# define a header line in the worksheet
header = {
    "A1": "Interface Name",  # 0
    "B1": "IP Address",  # 1
    "C1": "Status (L1)",  # 2
    "D1": "Protocol (L2)",  # 3
}

# processing

# create a connection instance to each network device
# one by one
for device in devices:
    with ConnectHandler(**device) as net_conn:
        print(f"Connected to {device['ip']}")
        intfs_brief = net_conn.send_command("show ip interface brief", use_textfsm=True)

    print(f"Collected interfaces brief of {device['ip']} & closed connection")

    # create seperate sheet of show ip interface brief command
    # for each device in the same Excel file
    ws = wb.add_worksheet(device["ip"][:31])

    # write the header line in the worksheet
    for cell, value in header.items():
        ws.write(cell, value)

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
