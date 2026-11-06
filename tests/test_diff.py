import json

from gendiff.diff import build_diff


def test_build_diff(read_fixture):
    first = json.loads(read_fixture("file1.json"))
    second = json.loads(read_fixture("file2.json"))
    expected = json.loads(read_fixture("expected_diff.json"))

    assert build_diff(first, second) == expected
