from gendiff.formater.to_stylish.format_value import format_value

LINE_TEMPLATES = {
    "unchanged": "  ",
    "added": "+ ",
    "removed": "- ",
}


def make_line(depth, sign, key, value):
    indent = " " * (depth * 4 - 2)
    return f"{indent}{sign}{key}: {format_value(value, depth)}"


def get_line(depth, node):
    key = node["key"]

    if node["type"] == "changed":
        return [
            make_line(depth, LINE_TEMPLATES["removed"], key, node["old_value"]),
            make_line(depth, LINE_TEMPLATES["added"], key, node["new_value"]),
        ]

    return [make_line(depth, LINE_TEMPLATES[node["type"]], key, node["value"])]
