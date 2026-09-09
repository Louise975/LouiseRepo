"""
Week 7: Data Serialization - Convert Network compare_configs
============================================================

Your task: Convert a network device config between JSON and YAML

FILL IN THE BLANKS marked with ____ 
Run this script when done: python3 exercise_week7.python3
"""

import json
import yaml

#--------------------------------------------------------------
# This is a network device configuration in pythonn (dictionary)
#---------------------------------------------------------------

router_config = {
    "hostname": "Router-1",
    "vendor": "Cisco",
    "interfaces": [
        {"name": "GigabitEthernet1", "ip": "192.168.1.1", "Status": "up"},
        {"name": "GigabitEthernet2", "ip": "10.0.0.1", "Status": "up"},
        {"name": "GigabitEthernet3", "ip": "172.16.0.1", "Status": "down"},
    ]
}

#---------------------------------------------------------------
# EXERCISE 1: Convert Python dict -> JSON
#---------------------------------------------------------------
#HINT: Converts a python dict to a JSON string

print("=== EXERCISE 1: Convert to JSON ===")

#FILL IN THE BLANK: use to convert router_config to JSON
json_output = json.dumps(router_config, indent=2)

print(json_output)
print()

#---------------------------------------------------------------
# EXERCISE 2: Convert Python dict -> YAML
#---------------------------------------------------------------
#HINT: Converts a python dict to a YAML string

print("=== EXERCISE : Convert to YAML ===")

#FILL IN THE BLANK: use to convert router_config to JSON
yaml_output = yaml.dump(router_config, default_flow_style=False)

print(yaml_output)
print()

#---------------------------------------------------------------
# EXERCISE 2: Read JSON from a file
#---------------------------------------------------------------

