#!/usr/bin/python3
import json
from sys import argv
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

a_file = "add_item.json"

try:
    a_list = load_from_json_file(a_file)
    a_list += argv[1:]
except:
    a_list = []

save_to_json_file(a_list, a_file)
