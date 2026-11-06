from gendiff.formater.to_stylish.get_line import get_line


def build_lines(diff, depth=1):
    lines = []

    for node in diff:
        if node["type"] == "nested":
            indent = " " * (depth * 4)
            lines.append(f"{indent}{node['key']}: {{")
            lines.extend(build_lines(node["children"], depth + 1))
            lines.append(f"{indent}}}")
        else:
            lines.extend(get_line(depth, node))

    return lines
