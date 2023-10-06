# Imports
from netmiko import ConnectHandler

# Inputs
device = {
    "device_type": "cisco_ios",
    "ip": "sandbox-iosxe-latest-1.cisco.com",
    "username": "admin",
    "password": "C1sco12345",
    "secret": "",  # secret is used if enable password is set
    "fast_cli": False,
}

# Processing

# create a connection instance to the network device
net_conn = ConnectHandler(**device)
# send a command to the network device
facts = net_conn.send_command(command_string="show version")
# disconnect from the network device
net_conn.disconnect()

# Output

# print the output of the command
print(facts)

