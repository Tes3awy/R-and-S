from pprint import pprint

from netmiko import ConnectHandler

# imports


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
        "device_type": "cisco_ios_telnet",
        "ip": "192.168.1.150",
        "username": "cisco",
        "password": "cisco",
        "secret": "",
        "fast_cli": False,
    },
]

# create a connection instance to each network device
for device in devices:
    with ConnectHandler(**device) as net_conn:
        print(f"Connected to {device['ip']}")
        facts = net_conn.send_command("show version", use_textfsm=True)
    print(f"Disconnected from {device['ip']}")
    # pretty print the output
    pprint(facts)

print("SUCCESS")
