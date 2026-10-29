vlan_ids = []
#Add 5 vlans to the list with while-loops

vlan = 100

while len(vlan_ids) < 5:
    vlan_ids.append(vlan)
    vlan += 100

print(vlan_ids)
print(len(vlan_ids))