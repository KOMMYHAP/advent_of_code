import re

from utilities import get_input


def task_5():
    data = get_input('input_3')
    pattern = re.compile(r'mul\((\d+),(\d+)\)')
    total = 0
    for match in pattern.finditer(data):
        (lhs, rhs) = map(int, match.groups())
        total += lhs * rhs

    print(f'sum of all valid \'mul\' {total}')
