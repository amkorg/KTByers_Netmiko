from netmiko import Netmiko
from getpass import getpass

net_conn = Netmiko(host = 'puntr201',username = 'admin_punakorg', password = getpass(),device_type='cisco_ios')
print(net_conn.find_prompt())

#puntr201#