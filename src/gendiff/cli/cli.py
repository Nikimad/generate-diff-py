import sys

from gendiff.cli.get_config import get_config
from gendiff.diff.generate_diff import generate_diff


def main():
    config = get_config()

    try:
        print(generate_diff(*config["paths"], config["format"]))
    except ValueError as error:
        sys.exit(f"Error: {error}")