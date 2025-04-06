def build_diff(file1, file2):
    all_keys = file1.keys() | file2.keys()
    remove_keys = file1.keys() - file2.keys()
    add_keys = file2.keys() - file1.keys()
    all_keys_sorted = sorted(list(all_keys))
    diff = {}
    for key in all_keys_sorted:
        if key in remove_keys:
            diff[key] = {'status': 'remove', 'value': file1[key]}
        elif key in add_keys:
            diff[key] = {'status': 'add', 'value': file2[key]}
        elif isinstance(file1[key], dict) and isinstance(file2[key], dict):
            diff[key] = {
                'status': 'child', 'value': build_diff(file1[key], file2[key])
            }
        else:
            if file1[key] == file2[key]:
                diff[key] = {'status': 'unchange', 'value': file1[key]}
            else:
                diff[key] = {
                    'status': 'change', 'value': {
                        'old_value': file1[key], 'new_value': file2[key]
                    }
                }

    return diff