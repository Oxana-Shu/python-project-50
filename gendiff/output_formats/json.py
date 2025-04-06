from itertools import chain

from gendiff.build_diff import build_diff
from gendiff.constants import NUM_OF_INDENTS, SPACE


def json(file1, file2):
    diff = build_diff(file1, file2)
    result = '{'
    depth = 1
    result += (pars_diff(diff, depth))
    result += '\n}'
    return result


def current_indent(depth):
    return NUM_OF_INDENTS * SPACE * depth


def pars_diff(diff, d):
    current_result = []
    for key, content in diff.items():
        status_value = content['status']
        c_i = current_indent
        if status_value != 'child' and status_value != 'change':
            line = (
                f'\n{c_i(d)}"{key}": {{\n{c_i(d + 1)}"status": '
                f'"{status_value}", \n{c_i(d + 1)}"value": '
                f'{check_value(content["value"], d + 2)}\n{c_i(d)}}},'
            )
            current_result.append(line)
        elif status_value == 'change':
            line = (
                f'\n{c_i(d)}"{key}": {{\n{c_i(d + 1)}"status": '
                f'"{status_value}", \n{c_i(d + 1)}"value": {{\n{c_i(d + 2)}'
                f'"old_value": '
                f'{check_value(content["value"]["old_value"], d + 3)}, '
                f'\n{c_i(d + 2)}"new_value": '
                f'{check_value(content["value"]["new_value"], d + 3)}'
                f'\n{c_i(d + 2)}}}\n{c_i(d + 1)}}},'
            )
            current_result.append(line)
        elif status_value == 'child':
            line = (
                f'\n{c_i(d)}"{key}": {{\n{c_i(d + 1)}"status": '
                f'"{status_value}", \n{c_i(d + 1)}"value": '
                f'{{ {pars_diff(content["value"], d + 2)}\n'
                f'{c_i(d + 1)}}}\n{c_i(d)}}},'
            )
            current_result.append(line)
    current_result[-1] = current_result[-1][:-1]
    return "".join(current_result)


def check_value(value, depth):
    if not isinstance(value, dict):
        if isinstance(value, bool):
            if value:
                return 'true'
            return 'false'
        elif value is None:
            return 'null'
        elif isinstance(value, int) or isinstance(value, float):
            return value
        return f'"{value}"'
    else:
        current_value = ['{']
        for k, v in value.items():
            current_value.append(
                f'\n{current_indent(depth)}"{k}": {check_value(v, depth + 1)},'
            )
        current_value[-1] = current_value[-1][:-1]
        current_value.append(f'\n{current_indent(depth - 1)}}}')
    return "".join(list(chain.from_iterable(current_value)))
