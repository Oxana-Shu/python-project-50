from gendiff.generate_diff import generate_diff


def test_stylish():
    path1 = 'gendiff/tests/test_data/file1.json'
    path2 = 'gendiff/tests/test_data/file2.json'
    path_assert = 'gendiff/tests/test_data/expected_stylish.txt'
    expected = open(path_assert, 'r').read()

    assert generate_diff(path1, path2) == expected


def test_plain():
    path1 = 'gendiff/tests/test_data/file1.json'
    path2 = 'gendiff/tests/test_data/file2.json'
    path_assert = 'gendiff/tests/test_data/expected_plain.txt'
    expected = open(path_assert, 'r').read()

    assert generate_diff(path1, path2, format_name='plain') == expected