import json


def format_scalar(value):
    if isinstance(value, str):
        return f"'{value}'"

    return json.dumps(value)


def format_value(value):
    if isinstance(value, (dict, list)):
        return "[complex value]"

    return format_scalar(value)
