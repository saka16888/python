__author__ = 'mihung'



'Display a PyATS configuration in YAML, in pretty-printed Python, and in JSON for comparison and contrast'

import yaml, json
from pprint import pprint

print('Display as YAML')
with open('notes/example_topology.yaml') as f:
    data = f.read()
    print(data)

print('Display as Native Python objects')
with open('notes/example_topology.yaml') as f:
    data = yaml.load(f)
    pprint(data)

print('Display with pretty printed JSON')
print(json.dumps(data, indent=4))

