import json


def to_json(diff):
    return json.dumps(diff, indent=2, ensure_ascii=False)
