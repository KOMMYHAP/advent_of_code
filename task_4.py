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


def is_safe_report_error_tolerant(report: list[int]) -> bool:
    if is_safe_report(report):
        return True

    def generate_new_report(skip_index: int) -> list[int]:
        return report[0:skip_index] + report[skip_index + 1:]

    for index in range(len(report)):
        fixed_report = generate_new_report(index)
        if is_safe_report(fixed_report):
            return True

    return False


def task_4():
    reports = parse_input(get_input('input_2'))
    safe_reports = reduce(lambda x, y: x + int(is_safe_report_error_tolerant(y)), reports, 0)
    print(f'safe reports count {safe_reports}')
