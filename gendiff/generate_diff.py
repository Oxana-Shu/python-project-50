from gendiff.engine import pars_file
from gendiff.output_formats.json import json
from gendiff.output_formats.plain import plain
from gendiff.output_formats.stylish import stylish


def generate_diff(file_path1, file_path2, format_name='stylish'):
    file1 = pars_file(file_path1)
    file2 = pars_file(file_path2)
    select_format = {
        'stylish': stylish(file1, file2),
        'plain': plain(file1, file2),
        'json': json(file1, file2),
    }
    return select_format[format_name]