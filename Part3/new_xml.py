print("-------------------------------------------------")
# Convert XML to JSON
print("Convert XML to JSON")
print("-------------------------------------------------")
import json
import xmltodict
print("Method 1")
with open('inventory.xml') as xml_file:
    xml = xmltodict.parse(xml_file.read())

print(json.dumps(xml, indent=4))
print("-------------------------------------------------")
print(json.dumps(xml, indent=4).replace("@", ""))
print("Method 2")
print("-------------------------------------------------")
with open('inventory.xml') as xml_file:
    xml1 = xmltodict.parse(xml_file.read(), attr_prefix='')
print(json.dumps(xml1, indent=4))


print(xml['inventory']['prod:device'][0]['@name'])             # csr1kv1
print(xml['inventory']['prod:device'][1]['prod:serial'])       # XB587381

print("")
print("-------------------------------------------------")
print("Interact with XML in Python")
print("-------------------------------------------------")
# Interact with XML in Python
import xml.etree.ElementTree as ET

tree = ET.parse('inventory.xml')
root_data = tree.getroot()

print(root_data.tag)

# To find all serial numbers that are part of prod namespace, use iter() with root_data 
for child in root_data:
    print(child.tag, child.attrib)
  
   
for serial in root_data.iter('{https://www.cisco.com/ns/routers/prod}serial'):
    print(serial.text)

print()
# To find which serial number belonging to which device use findall() and find() methods
for device in root_data.findall('{https://www.cisco.com/ns/routers/prod}device'):
    name = device.attrib['name']
    serial = device.find('{https://www.cisco.com/ns/routers/prod}serial').text
    print(name, serial)

print()
    
    # print all attributes related to SNMP element iter()
    
for snmp in root_data.iter('{https://www.cisco.com/ns/routers/dev}snmp'):
    print(snmp.attrib)