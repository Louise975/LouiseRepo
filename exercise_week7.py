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
# EXERCISE 3: Read JSON from a file
#---------------------------------------------------------------

print("=== EXERCISE 3: Read JSON from file ===")

#first, lets save our config as a JSON file
with open("router_config.json", "w") as f:
    json.dump(router_config, f, indent=2)

#Now read it back
#FILL IN THE BLANK: use to read from the file
with open("router_config.json", "r")as f:
    loaded_config = json.load(f)

print(f"Loaded hostname: {loaded_config['hostname']}")
print(f"Number of interfaces: {"len(loaded_config['interfaces])"}")
print()

#---------------------------------------------------------------
# EXERCISE 4: Save YAML to a file 
#---------------------------------------------------------------

print("=== EXERCISE 4: Save YAML to file ===")

#FILL IN THE BLANK: open "router_config" for writing 
with open("router_config.yaml", "w")as f:
    yaml.dump(router_config, f, default_flow_style=False)

print("saved to router_config.yaml")
print()

#---------------------------------------------------------------
# EXERCISE 5: CHALLENGE - Modify and save 
#---------------------------------------------------------------
#Add a new interface  to the config, then save both JSON and YAML

print("=== EXERCISE 5: CHALLENGE ===")

#Add a new interface (Loopback0)
new_interface = {"name": "loopback0", "ip": "1.1.1.1", "status": "up"}

#FILL IN THE BLANK: append the new interface to the list
router_config["interfaces"].append(new_interface)

#save updated config
with open("updated_config.json", "w"):
    json.dump(router_config, f, indent=2)

print(f"Added interface: (new_interface['name'])")
print(f"total interfaces now: {len(router_config['interfaces'])}")
print()

print("=" * 50)
print("Exercise Complete! Check your files:")
print(" - router_config.json")
print(" - router_config.yaml")
print(" - updated_config.json")
print("=" * 50)