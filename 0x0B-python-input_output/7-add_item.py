import sys
import json
from os import path


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using JSON format"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)

def load_from_json_file(filename):
    """Creates a Python object from a given JSON file"""
    with open(filename) as f:
        return json.load(f)

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
  
