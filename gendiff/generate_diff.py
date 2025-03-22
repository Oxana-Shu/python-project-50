from gendiff.engine import read_json


def generate_diff(file_path1, file_path2):
    file1 = read_json(file_path1)
    file2 = read_json(file_path2)
    all_keys = file1.keys() | file2.keys()
    remove_keys = file1.keys() - file2.keys()
    add_keys = file2.keys() - file1.keys()
    all_keys_sorted = sorted(list(all_keys))
    diff = {}
    for key in all_keys_sorted:
        if key in remove_keys:
            diff[f'- {key}'] = file1[key]
        elif key in add_keys:
            diff[f'+ {key}'] = file2[key]
        else:
            if file1[key] == file2[key]:
                diff[f'  {key}'] = file1[key]
            else:
                diff[f'- {key}'] = file1[key]
                diff[f'+ {key}'] = file2[key]
    return diff