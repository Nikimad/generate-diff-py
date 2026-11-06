import argparse


def build_parser():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file_path", help="path to the first file")
    parser.add_argument("second_file_path", help="path to the second file")
    parser.add_argument(
        "-f",
        "--format",
        default="stylish",
        choices=["stylish", "plain", "json"],
        help="output format (default: %(default)s)",
    )
    return parser
