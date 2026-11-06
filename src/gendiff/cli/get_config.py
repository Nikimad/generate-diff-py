from gendiff.cli.build_parser import build_parser


def get_config():
    args = build_parser().parse_args()
    return {
        "paths": [args.first_file_path, args.second_file_path],
        "format": args.format,
    }
