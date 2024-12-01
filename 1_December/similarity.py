with open('1_december/input.txt', 'r') as input_file:
    values1 = []
    values2 = []

    for line in input_file:
        values = line.strip().split()
        values1.append(values[0])
        values2.append(values[1])

similarity = 0
for i in range(len(values1)):
    mult = values2.count(values1[i])
    similarity += int(values1[i])*mult

print(similarity)

