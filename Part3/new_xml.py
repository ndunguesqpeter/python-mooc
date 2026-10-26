import xml.etree.ElementTree as ET

tree = ET.parse('inventory.xml')
root_data = tree.getroot()

print(root_data.tag)