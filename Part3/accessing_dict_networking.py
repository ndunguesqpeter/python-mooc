network = {
    "site": "Doha-DC1",
    "devices": {
        "csr1kv1": {
            "os": "ios-xe",
            "version": "16.09.03",
            "interfaces": [
                {"name": "Gi0/1", "state": "shutdown", "ip": None},
                {"name": "Gi0/2", "state": "up", "ip": "10.0.0.1"},
                {"name": "Gi0/3", "state": "up", "ip": "10.0.1.1"},
            ],
        },
        "csr1kv2": {
            "os": "ios-xe",
            "version": "17.03.01",
            "interfaces": [
                {"name": "Gi0/1", "state": "up", "ip": "10.0.0.2"},
                {"name": "Gi0/2", "state": "shutdown", "ip": None},
            ],
        },
        "nxos1": {
            "os": "nx-os",
            "version": "9.3.5",
            "interfaces": [
                {"name": "Eth1/1", "state": "up", "ip": "10.0.2.1"},
            ],
        },
    },
}
#Exercise
#1. Print the OS of csr1kv2.
print(f"1.{network["devices"]["csr1kv1"]["os"]}")

#2. Print the IP address of the second interface on csr1kv1.
print(f"2.{network["devices"]["csr1kv1"]["interfaces"][1]["ip"]}")

#3. Print every device name together with its number of interfaces, like csr1kv1: 3
print("3.")
# 3. loop over .items() of the devices dict
for name, data in network["devices"].items():
    print(f"->.{name}:{len(data["interfaces"])}")
    
#Build a list of all interfaces in the shutdown state across all devices, 
# formatted as "device:interface", for example "csr1kv1:Gi0/1"
down = []
for name, data in  network["devices"].items():
    for intf in data["interfaces"]:
        if intf["state"] == "shutdown":
            down.append(f"{name}:{intf["name"]}")
print("4.", down)
# 5. dict comprehension with a nested list comprehension
ips = {
    name: [i["ip"] for i in data["interfaces"] if i["ip"] is not None]
    for name, data in network["devices"].items()
}
print("5.", ips)

    