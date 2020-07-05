# Find a package in the Python standard library for dealing with
# JSON. Import the library module and inspect the attributes of the
# module. Use the help function to learn more about how to use the
# module. Serialize a dictionary mapping 'name' to your name and 'age'
# to your age, to a JSON string. Deserialize the JSON back into
# Python.

import json
data = {
    'detail': 'person',
    'name': 'Nirvay Chaudhary',
    'age': '19 Years'
}

with open("json_file.json", "w") as write_file:
    json.dump(data, write_file, indent=4)

json_string_serialize = json.dumps(data, indent=4)

print(type(json_string_serialize))
print(json_string_serialize)

with open("json_file.json", "r") as read_file:
    data = json.load(read_file)

json_string_deserialize = json.loads(json_string_serialize)

print(type(json_string_deserialize))
print(json_string_deserialize)

