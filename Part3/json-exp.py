import json

json_data = '{"name": "John", "age": 30, "city": "California"}'

test = json.loads(json_data)
print(test['name'])   # John
print(test['age'])    # 30
print(test['city'])   # California
print(test)