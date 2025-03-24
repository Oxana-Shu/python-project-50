from gendiff.generate_diff import generate_diff


def test_simple_json():
    result = {
        '- follow': False,
        '  host': 'hexlet.io',
        '- proxy': '123.234.53.22',
        '- timeout': 50,
        '+ timeout': 20,
        '+ verbose': True
    }
    path1 = 'gendiff/tests/test_data/file1.json'
    path2 = 'gendiff/tests/test_data/file2.json'

    assert generate_diff(path1, path2) == result


def test_simple_yaml():
    result = {
        '- follow': False,
        '  host': 'hexlet.io',
        '- proxy': '123.234.53.22',
        '- timeout': 50,
        '+ timeout': 20,
        '+ verbose': True
    }
    path1 = 'gendiff/tests/test_data/file3.yaml'
    path2 = 'gendiff/tests/test_data/file4.yaml'
    path3 = 'gendiff/tests/test_data/file5.yml'
    path4 = 'gendiff/tests/test_data/file6.yml'

    assert generate_diff(path1, path2) == result
    assert generate_diff(path3, path4) == result