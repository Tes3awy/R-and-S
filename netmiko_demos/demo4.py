# imports

from datetime import date

from netmiko import ConnectHandler

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
# one by one
for device in devices:
    with ConnectHandler(**device) as net_conn:
        print(f"Connected to {device['ip']}")
        hostname = net_conn.send_command("show version", use_textfsm=True)[0][
            "hostname"
        ]
        run_cfg = net_conn.send_command("show running-config")

    print(f"Disconnected from {device['ip']}")

    # Save output of show running-config command of each device to a text file
    # with the ip of the device (Inside for loop to save each show run of each device)
    with open(f"{device['ip']}_{date.today()}.txt", "w") as f:
        f.write(run_cfg)
    print(f"Saved output of {hostname} ({device['ip']})")

print("SUCCESS")
