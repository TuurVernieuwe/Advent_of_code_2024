def out_of_bounds(pos, grid):
    return pos[0] < 0 or pos[1] < 0 or pos[0] >= len(grid[0]) or pos[1] >= len(grid)

def allowed(pos, grid):
    return grid[pos[1]][pos[0]] != '#'

def turn(direction):
    turns = {(0, -1): (1, 0), (1, 0): (0, 1), (0, 1): (-1, 0), (-1, 0): (0, -1)}
    return turns[direction]

def move(position, direction, grid):
    while True:
        if grid[position[1]][position[0]] == '.' or grid[position[1]][position[0]] == '^':
            grid[position[1]][position[0]] = 'X'
        
        next_pos = [position[0] + direction[0], position[1] + direction[1]]
        
        if out_of_bounds(next_pos, grid):
            return sum(mapSpace == 'X' for row in grid for mapSpace in row)
        
        if allowed(next_pos, grid):
            position = next_pos
        else:
            direction = turn(direction)


with open("6_december/input.txt", "r") as inputFile:
    grid = [list(line.strip()) for line in inputFile]

start_position = next([row.index('^'), column] for column, row in enumerate(grid) if '^' in row)
print(move(start_position, (0, -1), grid))



