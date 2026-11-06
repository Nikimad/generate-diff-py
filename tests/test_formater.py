import json

import pytest

from gendiff.formater import ERROR_MESSAGES, FORMATERS, format_diff

EXPECTED = {
    "stylish": "expected_stylish.txt",
    "plain": "expected_plain.txt",
    "json": "expected_diff.json",
}


@pytest.fixture
def diff(read_fixture):
    return json.loads(read_fixture("expected_diff.json"))


@pytest.mark.parametrize("fmt", FORMATERS.keys())
def test_format_diff(diff, read_fixture, fmt):
    result = format_diff(diff, fmt)
    expected = read_fixture(EXPECTED[fmt])

    if fmt == "json":
        result, expected = json.loads(result), json.loads(expected)

    assert result == expected


def test_format_diff_unexpected_format(diff):
    with pytest.raises(ValueError, match=ERROR_MESSAGES["unsupported"]):
        format_diff(diff, "unknown")
