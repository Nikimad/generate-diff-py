from gendiff.formater.to_json import to_json
from gendiff.formater.to_plain import to_plain
from gendiff.formater.to_stylish import to_stylish

FORMATERS = {"json": to_json, "plain": to_plain, "stylish": to_stylish}

ERROR_MESSAGES = {
    "unsupported": "unsupported output format",
}


def format_diff(diff, format):
    if format not in FORMATERS:
        raise ValueError(f"{ERROR_MESSAGES['unsupported']}: {format}")

    formater = FORMATERS[format]

    return formater(diff)
