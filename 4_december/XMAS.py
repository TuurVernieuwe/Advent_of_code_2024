def count_xmas(grid):
    sequence = "XMAS"
    rows = len(grid)
    cols = len(grid[0])
    seq_len = len(sequence)
    directions = [
        (0, 1),     #right
        (0, -1),    #left
        (1, 0),     #up
        (-1, 0),    #down
        (1, 1),     #diagonal up-right
        (1, -1),    #diagonal up-left
        (-1, 1),    #diagonal down-right
        (-1, -1)    #diagonal down-left
    ]

    count = 0

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols
    
    def check_directions(x, y, dx, dy):
        for i in range(seq_len):
            nx, ny = x + i*dx, y + i*dy
            if not is_valid(nx, ny) or grid[nx][ny] != sequence[i]:
                return False
        return True
    
    for x in range(rows):
        for y in range(cols):
            for dx, dy in directions:
                if check_directions(x, y, dx, dy):
                    count += 1

    return count

with open('4_december/test_input.txt', 'r') as inputFile:
    grid = [list(line.strip()) for line in inputFile]
        

result = count_xmas(grid)
print(result)