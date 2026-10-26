import json

facts = { 
	"inventory":{
		"device":[ 
			{ 
				"name": "csr1kv1",
				"version": "16.09", 
				"vendor": "cisco", 
				"uptime": "2 days", 
				"serial": "XB96861", 
				"snmp": [ 
					{"name": "public", "permission": "ro"}, 
					{"name": "private", "permission": "rw"} 
				]
			}
		]
	}
}
print(json.dumps(facts))

facts_str = json.dumps(facts)
print(type(facts_str))
print("")
print(json.dumps(facts, indent=3))

vlan_ids = '{"name": "HR", "id": 100}'
interfaces = '["GigabitEthernet1", "GigabitEthernet2", "GigabitEthernet3","GigabitEthernet4"]'

print(type(vlan_ids))
print(type(interfaces))

vlan_nums = json.loads(vlan_ids)
interface_names = json.loads(interfaces)

print(vlan_nums['id'])
print(interface_names[2])

print(type(vlan_nums))
print(type(interface_names))