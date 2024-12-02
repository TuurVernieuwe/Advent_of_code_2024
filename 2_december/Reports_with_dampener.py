def is_safe(report):
    is_ascending = report[0] < report[1]
    for i in range(len(report)-1):
        distance = abs(report[i+1] - report[i])
        if distance < 1 or distance > 3:
            return False
        if (is_ascending and report[i+1] <= report[i]) or (not is_ascending and report[i+1] >= report[i]):
            return False
    return True


with open('2_december/input.txt', 'r') as inputFile:
    reports = [list(map(int, line.strip().split())) for line in inputFile]

total_safe = 0
for report in reports:
    #check if initially safe
    if is_safe(report):
        total_safe += 1

    #check if it becomes safe by removing any number
    else:
        for i in range(len(report)):
            copy_report = report.copy()
            copy_report.pop(i)
            if is_safe(copy_report):
                total_safe += 1
                break
        
    

    

print(total_safe)


