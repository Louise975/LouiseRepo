import json
import yaml
import os

try:
    import xmltodict
    HAS_XML_TODICT = True
except importError
HAS_XML_TODICT = False
print("Note: xmltodict not installed, Run: pip install xmltodict")
