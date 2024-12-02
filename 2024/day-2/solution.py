def solution_1(input_):
    reports = [[int(level) for level in full_level] for full_level in [report.split(" ") for report in input_.split("\n")[:-1]]]
    number_of_safe_reports = 0
    for report in reports:
        increasing = report[0] < report[1]
        for idx, level in enumerate(report):
            if idx == len(report) - 1:
                number_of_safe_reports +=1
                break
            if 1 <= abs(level - report[idx + 1]) <= 3:
                if increasing and level > report[idx + 1]:
                    break
                elif not increasing and level < report[idx + 1]:
                    break
            else:
                break

    print(number_of_safe_reports)

def check_if_valid(report, report_idx):
    increasing = report[0] < report[1]
    for idx, level in enumerate(report):
        if idx == len(report) - 1:
            return "True"
        if 1 <= abs(level - report[idx + 1]) <= 3:
            if (increasing and level > report[idx + 1]) or (not increasing and level < report[idx + 1]):
                return idx
        else:
            return idx

def solution_2(input_):
    reports = [[int(level) for level in full_level] for full_level in [report.split(" ") for report in input_.split("\n")[:-1]]]
    number_of_safe_reports = 0
    for report_idx, report in enumerate(reports):
        valid = check_if_valid(report, report_idx)
        if valid == "True":
            number_of_safe_reports += 1
            continue
        new_valid = check_if_valid(report[:valid] + report[valid + 1:], report_idx)
        if new_valid == "True":
            number_of_safe_reports += 1
            continue

    print(number_of_safe_reports)

debug_input = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""

# solution_1(debug_input)
# solution_2(debug_input)
full_input = open("input").read()
# solution_1(full_input)
solution_2(full_input)
