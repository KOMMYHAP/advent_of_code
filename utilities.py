from os import path


def get_input(filename: str):
    with open(path.join('data', filename), encoding="utf-8") as f:
        return f.read()
