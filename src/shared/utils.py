# Functions for general purpose

# This function needs a tuple or list of dictionaries.
# Is assumed these dictionaries has exactly the same keys.
import os, sys

def get_assets_path():
    if getattr(sys, 'frozen', False):
        # Compiled executable location
        base_path = os.path.dirname(sys.executable)
    else:
        # Python script location
        base_path = os.path.dirname(os.path.abspath(__file__))

    a_path = os.path.join(base_path, '..', '..', 'assets')
    a_path = os.path.abspath(a_path)
    
    return a_path

def get_ordered_data(array_of_dict):
    # Taking keys from the first dictionary
    keys = array_of_dict[0].keys()
    data = []
    for dict in array_of_dict:
        temp_list = []
        for key in keys:
            temp_list.append(dict[key])
        data.append(tuple(temp_list))
    
    # Output both keys and data as a tuple of tuples.
    return tuple(keys), data

def read_text_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    return text
