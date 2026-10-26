import xml.etree.ElementTree as ET

tree = ET.parse('inventory.xml')
root_data = tree.getroot()

print(root_data.tag)

for child in root_data:
    print(child.tag, child.attrib)
    
for serial in root_data.iter('{https://www.cisco.com/ns/routers/prod}serial'):
    print(serial.text)

print()

for device in root_data.findall('{https://www.cisco.com/ns/routers/prod}device'):
    name = device.attrib['name']
    serial = device.find('{https://www.cisco.com/ns/routers/prod}serial').text
    print(name, serial)