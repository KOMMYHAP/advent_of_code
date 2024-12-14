from bisect import bisect_left, bisect_right

from utilities import get_input


def parse_input(data: str):
    columns = ([], [])
    for row in data.split('\n')[:-1]:
        (left, right) = row.split('   ')
        columns[0].append(int(left))
        columns[1].append(int(right))
    return columns


def task_2():
    columns = parse_input(get_input('input_1'))
    columns[0].sort()
    columns[1].sort()

    similarity_scores = 0
    left_index_from = 0
    right_index_to = 0

    while left_index_from != len(columns[0]):
        location_id = columns[0][left_index_from]
        left_index_to = bisect_right(columns[0], location_id, left_index_from)
        left_count = left_index_to - left_index_from
        left_index_from = left_index_to

        right_index_from = bisect_left(columns[1], location_id, right_index_to)
        right_index_to = bisect_right(columns[1], location_id, right_index_from)
        right_count = right_index_to - right_index_from

        similarity_scores += location_id * left_count * right_count

    print(f'similarity scores = {similarity_scores}')
