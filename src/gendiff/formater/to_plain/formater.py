from gendiff.formater.to_plain.build_lines import build_lines


def to_plain(diff):
    return "\n".join(build_lines(diff))
