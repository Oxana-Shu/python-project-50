from itertools import chain

from gendiff.build_diff import build_diff
from gendiff.constants import NUM_OF_INDENTS, SPACE


def stylish(file1, file2):
    diff = build_diff(file1, file2)

    result = ['{']
    depth = 0
    result.append(pars_diff(diff, depth))
    result.append('}')
    return "\n".join(list(chain.from_iterable(result)))


def current_indent(depth):
    return NUM_OF_INDENTS * SPACE * depth


def pars_diff(diff, depth):
    current_result = []
    for key, content in diff.items():
        status_value = content['status']
        if status_value == 'remove':
            current_result.append(
                f'{current_indent(depth)}  - {key}: {
                    check_value(content['value'], depth + 2)
                }'
            )
        elif status_value == 'add':
            current_result.append(
                f'{current_indent(depth)}  + {key}: {
                    check_value(content['value'], depth + 2)
                }'
            )
        elif status_value == 'unchange':
            current_result.append(
                f'{current_indent(depth)}    {key}: {
                    check_value(content['value'], depth + 2)
                }'
            )
        elif status_value == 'change':
            current_result.append(
                f'{current_indent(depth)}  - {key}: {
                    check_value(content['value']['old_value'], depth + 2)
                }'
            )
            current_result.append(
                f'{current_indent(depth)}  + {key}: {
                    check_value(content['value']['new_value'], depth + 2)
                }'
            )
        elif status_value == 'child':
            current_result.append(f"{current_indent(depth)}    {key}: {{")
            current_result.extend(pars_diff(content['value'], depth + 1))
            current_result.append(f"{current_indent(depth + 1)}}}")
    return current_result


def check_value(value, depth):
    if not isinstance(value, dict):
        if isinstance(value, bool):
            if value:
                return 'true'
            return 'false'
        elif value is None:
            return 'null'
        return value
    else:
        current_value = ['{\n']
        for k, v in value.items():
            current_value.append(
                f'{current_indent(depth)}{k}: {
                    check_value(v, depth + 1)
                }\n'
            )
        current_value.append(f'{current_indent(depth - 1)}}}')
    return "".join(list(chain.from_iterable(current_value)))