def count_xmas(grid):
    sequence = "MAS"
    rows = len(grid)
    cols = len(grid[0])
    seq_len = len(sequence)
    patterns = [
        ["M", "M", "A", "S", "S"],
        ["M", "S", "A", "M", "S"],
        ["S", "M", "A", "S", "M"],
        ["S", "S", "A", "M", "M"]
    ]

    count = 0

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols
    
    def check_mas_x(x, y, pattern): 
        if is_valid(x, y) and is_valid(x+2, y+2):
            if (
                grid[x][y] == pattern[0] and
                grid[x+1][y+1] == pattern[2] and
                grid[x+2][y+2] == pattern[4]
            ):
                if (
                    grid[x+2][y] == pattern[1] and
                    grid[x][y+2] == pattern[3]
                ):
                    return True
        return False
    
    for x in range(rows):
        for y in range(cols):
            for pattern in patterns:
                if check_mas_x(x, y, pattern):
                    count += 1

    return count

with open('4_december/input.txt', 'r') as inputFile:
    grid = [list(line.strip()) for line in inputFile]
        

result = count_xmas(grid)
print(result)