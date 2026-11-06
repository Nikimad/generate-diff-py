from gendiff.formater.to_plain.format_value import format_value


def get_line(path, node):
    line_start = f"Property '{path}' was"

    match node["type"]:
        case "added":
            return f"{line_start} added with value: {format_value(node['value'])}"
        case "removed":
            return f"{line_start} removed"
        case "changed":
            old = format_value(node["old_value"])
            new = format_value(node["new_value"])
            return f"{line_start} updated. From {old} to {new}"
        case _:
            return ""
