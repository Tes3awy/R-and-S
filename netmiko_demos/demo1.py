# imports
from netmiko import ConnectHandler

# inputs
device = {
    "device_type": "cisco_ios",
    "ip": "sandbox-iosxe-latest-1.cisco.com",
    "username": "developer",
    "password": "C1sco12345",
    "secret": "",
    "fast_cli": False,
}

# processing

# create a connection instance to the network device
net_conn = ConnectHandler(**device)
# send a command to the network device
facts = net_conn.send_command("show version")
# disconnect from the network device
net_conn.disconnect()

# output

# print the output of the command
print(facts)
