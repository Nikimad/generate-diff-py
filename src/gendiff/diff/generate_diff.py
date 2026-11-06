from gendiff.diff import build_diff
from gendiff.formater import format_diff
from gendiff.parser import parse_file


def generate_diff(first_path, second_path, format_name="stylish"):
    first_data = parse_file(first_path)
    second_data = parse_file(second_path)

    return format_diff(build_diff(first_data, second_data), format_name)