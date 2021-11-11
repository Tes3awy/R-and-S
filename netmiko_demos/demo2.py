# imports

from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",
    "ip": "sandbox-iosxe-latest-1.cisco.com",
    "username": "developer",
    "password": "C1sco12345",
    "secret": "",
    "fast_cli": False,
}

# create a connection instance to the network device
# using context manager method (with function() as variable_name:)
with ConnectHandler(**device) as net_conn:
    facts = net_conn.send_command("show version")
# no need to close the connection, it will be closed automatically
print(facts)
print("SUCCESS")
