# Imports
from datetime import date

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

for device in devices:
    # create a connection instance to each network device
    print(f"Trying {device['ip']}...", end="\r")
    with ConnectHandler(**device) as conn:
        print(f"Connected to {conn.host}:{conn.port}")
        # Get the hostname of the device
        hostname = conn.send_command("show version", use_textfsm=True)[0][
            "hostname"
        ]
        run_cfg = conn.send_command("show running-config")

    print(f"Disconnected from {conn.host}")

    # Save output of show running-config command of each device to a text file
    # with the ip of the device (Inside for loop to save each show run of each device)
    with open(f"{device['ip']}_{date.today()}.txt", "wt") as f:
        f.write(run_cfg.strip())
    print(f"Saved output of running config of {hostname} ({device['ip']})", end="\n\n")

print("SUCCESS")

