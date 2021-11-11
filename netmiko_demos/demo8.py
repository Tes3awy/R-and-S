from datetime import date
from getpass import getpass

from netmiko import ConnectHandler

username = input("Username: ").strip()
password = getpass("Password: ")
# You can press enter to leave enable password empty
enable_pass = getpass("Enable password: ")

with open("iplist.txt", "r") as f:
    iplist = f.read().splitlines()

devices = []
for ip in iplist:
    if ip.strip():
        devices.append(
            {
                "device_type": "cisco_ios",
                "ip": ip.strip(),
                "username": username,
                "password": password,
                "secret": enable_pass,
                "fast_cli": False,
            }
        )

for device in devices:
    try:
        with ConnectHandler(**device) as net_conn:
            print(f"Connected to {device['ip']}")
            hostname = net_conn.send_command("show version", use_textfsm=True)[0][
                "hostname"
            ]
            run_cfg = net_conn.send_command("show running-config")
    except Exception as e:
        print(f"Failed to connect to {device['ip']} due to {e}")
    else:
        with open(f"{hostname}_{date.today()}.txt", "w") as f:
            f.write(run_cfg)
        print(f"{device['ip']} output saved to {hostname}_{date.today()}.txt")
