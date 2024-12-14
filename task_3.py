from functools import reduce

from utilities import get_input


def parse_input(data: str):
    reports = []
    for row in data.split('\n')[:-1]:
        reports.append(list(map(int, row.split(' '))))
    return reports


def is_safe_report(report: list[int]) -> bool:
    prev_number = report[0]
    number = report[1]
    ascending = number > prev_number
    for number in report[1:]:
        if ascending:
            diff = number - prev_number
        else:
            diff = prev_number - number

        if 1 <= diff <= 3:
            prev_number = number
            continue

        return False

    return True


def task_3():
    reports = parse_input(get_input('input_2'))
    safe_reports = reduce(lambda x, y: x + int(is_safe_report(y)), reports, 0)
    print(f'safe reports count {safe_reports}')
