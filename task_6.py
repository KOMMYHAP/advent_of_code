import re

from utilities import get_input


def task_6():
    data = get_input('input_3')
    pattern = re.compile(r"(do\(\))|(don't\(\))|(mul\((\d+),(\d+)\))")
    total = 0
    enabled = True
    for match in pattern.finditer(data):
        groups = match.groups()
        if groups[0] is not None:
            enabled = True
            continue
        elif groups[1] is not None:
            enabled = False
            continue

        if not enabled:
            continue

        (lhs, rhs) = map(int, groups[-2:])
        total += lhs * rhs

    print(f'sum of all valid \'mul\' {total}')
