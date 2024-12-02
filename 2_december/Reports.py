def is_safe(report):
    is_ascending = report[0] < report[1]
    return all(1 <= abs(report[i+1] - report[i]) <= 3 and ((is_ascending and report[i+1] > report[i]) or (not is_ascending and report[i+1] < report[i])) for i in range(len(report)-1))


with open('2_december/input.txt', 'r') as inputFile:
    reports = [list(map(int, line.strip().split())) for line in inputFile]

total_safe = sum(1 for report in reports if is_safe(report))  

print(total_safe)


