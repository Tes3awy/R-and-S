# Imports
from netmiko import ConnectHandler

# Inputs
device = {
    "device_type": "cisco_ios",
    "ip": "sandbox-iosxe-latest-1.cisco.com",
    "username": "admin",
    "password": "C1sco12345",
    "fast_cli": False,
}

# Create a connection instance to the network device
# Using context manager method (with function() as variable_name:)
with ConnectHandler(**device) as conn:
    facts = conn.send_command("show version")
# no need to close the connection, it will be closed automatically
print(facts)
print("SUCCESS")

