import re

total_product = 0
mul_pattern = r"mul\((\d+),\s*(\d+)\)"
enabled = True
with open('3_december/input.txt', 'r') as inputFile:
    for line in inputFile:
        tokens = re.split(r"(do\(\)|don't\(\)|mul\(\d+,\s*\d+\))", line)

        for token in tokens:
            token = token.strip()  # Remove extra spaces
            
            if token == "do()":
                enabled = True  # Enable mul operations
            elif token == "don't()":
                enabled = False  # Disable mul operations
            elif enabled and re.match(mul_pattern, token):
                # If enabled, process mul(x, y)
                x, y = map(int, re.findall(r"\d+", token))
                total_product += x * y

            

print(total_product)
        