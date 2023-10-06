# Imports
from pprint import pprint

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
        "ip": "sandbox-iosxe-recomm-1.cisco.com",
        "username": "developer",
        "password": "",
        "fast_cli": False,
    },
]

# Iterate over devices list of dictionaries
for device in devices:
    print(f"Trying {device['ip']}...", end="\r")
    # Create a connection instance to each network device
    with ConnectHandler(**device) as conn:
        print(f"Connected to {conn.host}:{conn.port}")
        # Added use_textfsm = True to parse the show version output
        facts = conn.send_command("show version", use_textfsm=True)
    print(f"Disconnected from {conn.host}")
    # Use pprint (pretty print) to print the output
    pprint(facts, indent=4)

print("SUCCESS")

