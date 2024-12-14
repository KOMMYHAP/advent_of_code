from utilities import get_input


def parse_input(data: str):
    columns = ([], [])
    for row in data.split('\n')[:-1]:
        (left, right) = row.split('   ')
        columns[0].append(int(left))
        columns[1].append(int(right))
    return columns


def task_1():
    columns = parse_input(get_input('input_1'))
    columns[0].sort()
    columns[1].sort()
    distance = 0
    for (left, right) in zip(columns[0], columns[1]):
        distance += abs(left - right)

    print(f'total distance = {distance}')
