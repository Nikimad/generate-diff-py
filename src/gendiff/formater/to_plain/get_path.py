def get_path(key, parent):
    if parent:
        return f"{parent}.{key}"

    return key
