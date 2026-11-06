import pytest

from gendiff.parser import ERROR_MESSAGES, LOADERS, parse_file

DATA = {"key": "value"}

# (json, yaml, yml)
SUPPORTED_EXTENSIONS = tuple(ext.lstrip(".") for ext in LOADERS)

VALID_CONTENT = {
    "json": '{"key": "value"}',
    "yaml": "key: value",
    "yml": "key: value",
}

INVALID_CONTENT = {
    "json": '{"key": }',
    "yaml": "key: [value",
    "yml": "key: [value",
}

VALID_FILES = [
    pytest.param(ext, VALID_CONTENT[ext], id=ext) for ext in SUPPORTED_EXTENSIONS
]

INVALID_FILES = [
    pytest.param(ext, INVALID_CONTENT[ext], id=f"invalid-{ext}")
    for ext in SUPPORTED_EXTENSIONS
]


@pytest.mark.parametrize("ext, content", VALID_FILES)
def test_parse_file(tmp_path, ext, content):
    file = tmp_path / f"test.{ext}"
    file.write_text(content, encoding="utf-8")

    assert parse_file(file) == DATA


@pytest.mark.parametrize("ext", SUPPORTED_EXTENSIONS)
def test_parse_missing_file(tmp_path, ext):
    with pytest.raises(ValueError, match=ERROR_MESSAGES["missing"]):
        parse_file(tmp_path / f"nope.{ext}")


def test_parse_unsupported_extension(tmp_path):
    file = tmp_path / "test.txt"
    file.write_text("some text", encoding="utf-8")

    with pytest.raises(ValueError, match=ERROR_MESSAGES["unsupported"]):
        parse_file(file)


@pytest.mark.parametrize("ext, content", INVALID_FILES)
def test_parse_invalid_file(tmp_path, ext, content):
    file = tmp_path / f"invalid.{ext}"
    file.write_text(content, encoding="utf-8")

    with pytest.raises(ValueError, match=ERROR_MESSAGES["invalid"]):
        parse_file(file)
