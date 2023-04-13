import sys
import json
from os import path
from 5-save_to_json_file.py import save_to_json_file
from 6-load_from_json_file.py import load_from_json_file

# Get arguments from command line
args = sys.argv[1:]

# Create list if file doesn't exist, otherwise load list from file
filename = "add_item.json"
if not path.exists(filename):
    my_list = []
else:
    my_list = load_from_json_file(filename)

# Add arguments to list
my_list.extend(args)

# Save list to file
save_to_json_file(my_list, filename)
  
