import json


def read_json(path_to_file):
    with open(path_to_file, 'r') as file:
        loaded_data = json.load(file)
    return loaded_data