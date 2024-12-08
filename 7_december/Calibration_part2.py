from itertools import product

def evaluate_expression(numbers, operators):
    result = int(numbers[0])
    for i in range(len(operators)):
        if operators[i] == '+':
            result += int(numbers[i + 1])
        elif operators[i] == '*':
            result *= int(numbers[i + 1])
        elif operators[i] == '||':
            result = int(str(result) + numbers[i + 1])
    return result

def can_form_target(test_value, numbers):
    num_operators = len(numbers) - 1
    for operators in product(['+', '*', '||'], repeat=num_operators):
        if evaluate_expression(numbers, operators) == int(test_value):
            return True
    return False

with open("7_december/input.txt", "r") as inputFile:
    lines = inputFile.readlines()

result = 0
for line in lines:
    test_value = line.strip().split(':')[0]
    values = list(line.strip().split(':')[1].strip().split())
    if can_form_target(test_value, values):
        result += int(test_value)

print(result)