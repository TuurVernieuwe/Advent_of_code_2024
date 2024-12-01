with open('1_december/input.txt', 'r') as input_file:
    values1, values2 = zip(*(line.strip().split() for line in input_file))
    
sorted_1 = sorted(map(int, values1))
sorted_2 = sorted(map(int, values2))

total_distance = sum(abs(a - b) for a,b in zip(sorted_1, sorted_2))

print(total_distance)