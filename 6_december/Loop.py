def out_of_bounds(pos, grid):
    return pos[0] < 0 or pos[1] < 0 or pos[0] >= len(grid[0]) or pos[1] >= len(grid)

def allowed(pos, grid):
    return grid[pos[1]][pos[0]] != '#'

def turn(direction):
    turns = {(0, -1): (1, 0), (1, 0): (0, 1), (0, 1): (-1, 0), (-1, 0): (0, -1)}
    return turns[direction]

def move(position, direction, grid):
    visited = set()
    while True:    

        state = (position[0], position[1], direction[0], direction[1])
        
        if state in visited:
            return True
        visited.add(state)

        next_pos = [position[0] + direction[0], position[1] + direction[1]]
        if out_of_bounds(next_pos, grid):
            return False
        if allowed(next_pos, grid):
            position = next_pos
        else:
            direction = turn(direction)

def check_all_placements(start_position, grid):
    counter = 0
    for i, row in enumerate(grid):
        print(i)
        for j, place in enumerate(row):
            if place == '.':
                grid[i][j] = '#'
                stuck = move(start_position, (0, -1), grid)
                grid[i][j] = '.'
                if stuck:
                    counter += 1
    return counter


with open("6_december/input.txt", "r") as inputFile:
    grid = [list(line.strip()) for line in inputFile]

start_position = next([row.index('^'), column] for column, row in enumerate(grid) if '^' in row)
print(check_all_placements(start_position, grid))



