def build_diff(file1, file2):
    all_keys = file1.keys() | file2.keys()
    remove_keys = file1.keys() - file2.keys()
    add_keys = file2.keys() - file1.keys()
    all_keys_sorted = sorted(list(all_keys))
    diff = {}
    for key in all_keys_sorted:
        if key in remove_keys:
            diff[key] = ('remove', file1[key])
        elif key in add_keys:
            diff[key] = ('add', file2[key])
        elif isinstance(file1[key], dict) and isinstance(file2[key], dict):
            diff[key] = ('child', build_diff(file1[key], file2[key]))
        else:
            if file1[key] == file2[key]:
                diff[key] = ('unchange', file1[key])
            else:
                diff[key] = ('change', file1[key], file2[key])

    return diff