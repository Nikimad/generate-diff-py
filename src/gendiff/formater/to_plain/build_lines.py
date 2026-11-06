from gendiff.formater.to_plain.get_line import get_line
from gendiff.formater.to_plain.get_path import get_path


def build_lines(diff, parent=""):
    lines = []

    for node in diff:
        path = get_path(node["key"], parent)

        if node["type"] == "nested":
            lines.extend(build_lines(node["children"], path))
        elif node["type"] != "unchanged":
            lines.append(get_line(path, node))

    return lines
