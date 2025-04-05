from gendiff.engine import pars_file
from gendiff.output_formats.stylish import stylish


def generate_diff(file_path1, file_path2, format_name='stylish'):
    file1 = pars_file(file_path1)
    file2 = pars_file(file_path2)
    if format_name == 'stylish':
        return stylish(file1, file2)
    



