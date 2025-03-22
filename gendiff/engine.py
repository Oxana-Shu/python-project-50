import json

def read_json(name_of_file, path='gendiff/files'):
    path_to_file = f'{path}/{name_of_file}'
    with open(path_to_file, 'r') as file:
        loaded_data = json.load(file)
    return loaded_data