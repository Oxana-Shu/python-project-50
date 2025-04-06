from itertools import chain

from gendiff.build_diff import build_diff


def plain(file1, file2):
    diff = build_diff(file1, file2)

    result = []
    buff_properties = []
    result.append(pars_diff(diff, buff_properties))
    return "\n".join(list(chain.from_iterable(result)))


def pars_diff(diff, buff_properties):
    current_result = []
    for key, content in diff.items():
        status_value = content['status']
        if status_value == 'unchange' and isinstance(content['value'], dict):
            buff_properties.append(key)
        elif status_value == 'remove':
            buff_properties.append(key)
            current_result.append(
                f"Property '{".".join(buff_properties)}' was removed"
            )
            buff_properties.pop()
        elif status_value == 'add':
            buff_properties.append(key)
            current_result.append(
                f"Property '{".".join(buff_properties)}' was added with value: {
                    check_value(content['value'])
                }"
            )
            buff_properties.pop()
        elif status_value == 'change':
            buff_properties.append(key)
            current_result.append(
                f"Property '{".".join(buff_properties)}' was updated. From {
                    check_value(content['value']['old_value'])
                } to {check_value(content['value']['new_value'])}"
            )
            buff_properties.pop()
        elif status_value == 'child':
            buff_properties.append(key)
            current_result.extend(pars_diff(content['value'], buff_properties))
            buff_properties.pop()
    return current_result


def check_value(value):
    if not isinstance(value, dict):
        if isinstance(value, bool):
            if value:
                return 'true'
            return 'false'
        elif value is None:
            return 'null'
        elif isinstance(value, int) or isinstance(value, float):
            return value
        return f"'{value}'"
    else:
        return '[complex value]'