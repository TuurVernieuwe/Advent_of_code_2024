with open('1_december/input.txt', 'r') as input_file:
    values1 = []
    values2 = []

    for line in input_file:
        values = line.strip().split()
        values1.append(values[0])
        values2.append(values[1])
    
sorted_1 = sorted(values1)
sorted_2 = sorted(values2)

total_distance = 0
for i in range(len(sorted_1)):
    distance = abs(int(sorted_1[i]) - int(sorted_2[i]))
    total_distance += distance

print(total_distance)

