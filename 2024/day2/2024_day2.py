def parse_input():
    reports = []

    with open("input.txt") as file:
        for line in file:
            if(line):
                levels = line.split(" ")
                for index in range(len(levels)):
                    levels[index] = int(levels[index].strip())
                reports.append(levels)
    return reports  # Count the number of lights that are on

def is_valid_level(level1, level2, is_increasing):
    safe_set = [1, 2, 3]
    # print(f"Checking {level1} and {level2}: IsIncreasing = {is_increasing}  ----Test 1: diff = {abs(level1-level2)} -> {safe_set.count(abs(level1 - level2)) == 0} \tTest2: {((level2 > level1) != is_increasing)}")
    if((safe_set.count(abs(level1 - level2)) == 0)):
        return False
    if(((level2 > level1) != is_increasing)):
        return False
    return True

def count_safe_reports(reports):
    num_safe = 0
    is_increasing = False

    for report in reports:
        if(check_report(report)): num_safe += 1
    return num_safe
 
def count_safe_reports_with_dampener(reports):
    num_safe = 0
    for report in reports:
        if(check_report(report)): num_safe += 1 
        else:
            for levels in range(len(report)):
                report_copy = report.copy()
                report_copy.pop(levels)
                if(check_report(report_copy)):
                    num_safe += 1
                    break
    return num_safe

def check_report(report, num_removable=0):
    is_increasing = False
    if(report[0] < report[1]): is_increasing = True
    else: is_increasing = False

    # print(f"REPORT: {report}: is_increasing = {is_increasing}")
    for level in range(len(report)-1):
        if(not is_valid_level(report[level], report[level+1], is_increasing)):
            if(num_removable > 0):
                report.pop(level + 1)
                num_removable -= 1
                return check_report(report, num_removable)
            else:
                return False
    return True

reports = parse_input()
print(f"The number of safe reports is: {count_safe_reports(reports)}")
print(f"The number of safe reports with dampener is: {count_safe_reports_with_dampener(reports)}")

# print(f"The total similarity is: {calculate_similarity(id_list1, id_list2)}")
