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