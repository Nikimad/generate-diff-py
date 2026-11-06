import json
from pathlib import Path

import yaml

LOADERS = {
    ".json": json.load,
    ".yaml": yaml.safe_load,
    ".yml": yaml.safe_load,
}

ERROR_MESSAGES = {
    "missing": "file not found",
    "unsupported": "unsupported file format",
    "invalid": "invalid",
}


def parse_file(file_path):
    path = Path(file_path)
    ext = path.suffix.lower()
    name = ext.lstrip(".").upper()

    if ext not in LOADERS:
        raise ValueError(f"{ERROR_MESSAGES['unsupported']}: {ext}")

    try:
        with path.open("r", encoding="utf-8") as file:
            return LOADERS[ext](file)
    except FileNotFoundError:
        raise ValueError(f"{ERROR_MESSAGES['missing']}: {path}") from None
    except (json.JSONDecodeError, yaml.YAMLError) as error:
        raise ValueError(
            f"{ERROR_MESSAGES['invalid']} {name} in {path}: {error}"
        ) from error
