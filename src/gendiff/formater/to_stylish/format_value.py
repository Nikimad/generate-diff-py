import json


def format_scalar(value):
    if isinstance(value, str):
        return value

    return json.dumps(value, ensure_ascii=False)


def format_dict(value, depth):
    indent = " " * ((depth + 1) * 4)
    closing = " " * (depth * 4)
    lines = [
        f"{indent}{key}: {format_value(item, depth + 1)}" for key, item in value.items()
    ]

    return "\n".join(["{", *lines, f"{closing}}}"])


def format_value(value, depth):
    if isinstance(value, dict):
        return format_dict(value, depth)

    return format_scalar(value)
