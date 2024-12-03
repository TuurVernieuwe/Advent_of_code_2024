import re

total_product = 0
pattern = r"mul\((\d+),\s*(\d+)\)"
with open('3_december/input.txt', 'r') as inputFile:
    for line in inputFile:
        matches = re.findall(pattern, line)
        total_product += sum(int(x)*int(y) for x, y in matches)

print(total_product)
        