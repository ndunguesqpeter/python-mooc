import yaml
yaml_data = open('inventory.yml', 'r')
data = yaml.safe_load(yaml_data)
print(data)
print(type(data))
print(data['inventory']['device'][0]['uptime'])

import json
print(json.dumps(data, indent=4))