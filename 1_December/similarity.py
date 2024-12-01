with open('1_december/input.txt', 'r') as input_file:
    values1, values2 = zip(*(line.strip().split() for line in input_file))

similarity = sum(int(value) * values2.count(value) for value in values1)

print(similarity)

