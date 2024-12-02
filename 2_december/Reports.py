with open('2_december/input.txt', 'r') as inputFile:
    reports = [line.strip().split() for line in inputFile]

total_safe = 0
for report in reports:
    safe = True
    for i in range(len(report)-1):
        distance = abs(int(report[i+1]) - int(report[i]))
        if distance < 1 or distance > 3:
            safe = False
        if int(report[0]) > int(report[1]):
            if int(report[i+1]) >= int(report[i]):
                safe = False
        else:
            if int(report[i+1]) <= int(report[i]):
                safe = False
    if safe:
        total_safe += 1
        

print(total_safe)


