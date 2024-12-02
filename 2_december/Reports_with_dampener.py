def is_safe(report):
    is_ascending = report[0] < report[1]
    return all(1 <= abs(report[i+1] - report[i]) <= 3 and ((is_ascending and report[i+1] > report[i]) or (not is_ascending and report[i+1] < report[i])) for i in range(len(report)-1))

def can_be_safe(report):
    if is_safe(report):
        return True
    else:
        return any(is_safe(report[:i] + report[i+1:]) for i in range(len(report)))

with open('2_december/input.txt', 'r') as inputFile:
    reports = [list(map(int, line.strip().split())) for line in inputFile]

total_safe = sum(can_be_safe(report) for report in reports)

print(total_safe)


