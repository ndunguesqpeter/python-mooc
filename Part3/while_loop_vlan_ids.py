vlan_ids = []
#Add 5 vlans to the list with while-loops

vlan = 100

while 5 > len(vlan_ids):
    vlan_ids.append(vlan)
    vlan += 100

print(vlan_ids)
print(len(vlan_ids))