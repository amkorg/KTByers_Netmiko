from netmiko import Netmiko
from getpass import getpass


my_device = {'host' : 'puntr201',
'username': 'admin_punakorg',
'password' : getpass(),
'device_type':'cisco_ios'}
net_conn = Netmiko(**my_device)
print(net_conn.find_prompt())

#puntr201#