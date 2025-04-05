from gendiff.generate_diff import generate_diff


def test_json():
    path1 = 'gendiff/tests/test_data/file1.json'
    path2 = 'gendiff/tests/test_data/file2.json'
    path_assert = 'gendiff/tests/test_data/expected_stylish.txt'
    expected = open(path_assert, 'r').read()

    assert generate_diff(path1, path2) == expected
