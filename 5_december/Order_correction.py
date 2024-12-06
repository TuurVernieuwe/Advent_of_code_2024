from itertools import combinations

def checkUpdate(update, rules):
    rule_set = set(rules)
    return all((pair[1], pair[0]) not in rule_set for pair in combinations(update, 2))

def correct_order(update, rules):
    rule_set = set(rules)
    swapped = True
    while swapped:
        swapped = False
        for i, j in combinations(range(len(update)), 2):
            if (update[j], update[i]) in rule_set:
                update[i], update[j] = update[j], update[i]
                swapped = True
                break
    return update

with open("5_december/input.txt", "r") as inputFile:
    lines = inputFile.readlines()

rules = [tuple(line.strip().split('|')) for line in lines if '|' in line]
updates = [list(line.strip().split(',')) for line in lines if ',' in line]

updated_updates = [correct_order(update, rules) for update in updates if not checkUpdate(update, rules)]

result = sum(int(update[int((len(update)-1)/2)]) for update in updated_updates)



print(result)
    
