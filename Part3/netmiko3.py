#!/usr/bin/env python

from netmiko import ConnectHandler

iosv_l2_s1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.42.83',
    'username': 'peter',
    'password': 'cisco',
}

iosv_l2_s2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.42.84',
    'username': 'peter',
    'password': 'cisco',
}

iosv_l2_s3 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.42.85',
    'username': 'peter',
    'password': 'cisco',
}

iosv_l2_s4 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.42.86',
    'username': 'peter',
    'password': 'cisco',
}

iosv_l2_s5 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.42.87',
    'username': 'peter',
    'password': 'cisco',
}


with open('iosv_l2_access') as f:
    lines = f.read().splitlines()
print(lines)


all_devices = [iosv_l2_s5, iosv_l2_s4, iosv_l2_s3, iosv_l2_s2, iosv_l2_s1]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print(output)


with open('iosv_l2_core') as f:
    lines = f.read().splitlines()
print(lines)


all_devices = [iosv_l2_s2, iosv_l2_s1]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print(output)