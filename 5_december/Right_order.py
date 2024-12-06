from itertools import combinations

def checkUpdate(update, rules):
    for pair in combinations(update, 2):
        if (pair[1], pair[0]) in rules:
            return False
    return True

with open("5_december/input.txt", "r") as inputFile:
    lines = inputFile.readlines()

rules = [tuple(line.strip().split('|')) for line in lines if '|' in line]
updates = [list(line.strip().split(',')) for line in lines if ',' in line]

correct_updates = [update for update in updates if checkUpdate(update, rules)]
result = sum(int(update[int((len(update)-1)/2)]) for update in correct_updates)

print(result)
    
