import json

import yaml


def pars_file(file_path):
    path_split = file_path.split(".")
    if path_split[-1] == 'json':
        return read_json(file_path)
    elif path_split[-1] == 'yaml' or path_split[-1] == 'yml':
        return read_yaml(file_path)


def read_json(path_to_file):
    with open(path_to_file, 'r') as file:
        loaded_data = json.load(file)
    return loaded_data


def read_yaml(path_to_file):
    with open(path_to_file, 'r') as file:
        loaded_data = yaml.safe_load(file)
    return loaded_data
