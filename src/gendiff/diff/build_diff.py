def build_node(key, first, second):
    if key not in second:
        return {"key": key, "type": "removed", "value": first[key]}
    if key not in first:
        return {"key": key, "type": "added", "value": second[key]}

    old, new = first[key], second[key]

    if isinstance(old, dict) and isinstance(new, dict):
        return {"key": key, "type": "nested", "children": build_diff(old, new)}
    if type(old) is type(new) and old == new:
        return {"key": key, "type": "unchanged", "value": old}
    return {"key": key, "type": "changed", "old_value": old, "new_value": new}


def build_diff(first_file_data, second_file_data):
    keys = sorted(first_file_data.keys() | second_file_data.keys())
    return [build_node(key, first_file_data, second_file_data) for key in keys]
