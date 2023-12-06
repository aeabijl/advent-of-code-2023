from collections import defaultdict

def is_within_bounds(row,adj_row,rows,col,adj_col,columns):
    return 0<=row+adj_row<rows and 0<=col+adj_col<columns

def get_gears_with_parts(grid, rows, columns):
    gears = defaultdict(list)

    for row in range(rows):
        gear_positions = set()
        part_number = 0

        for column in range(columns+1):
            if column<columns and grid[row][column].isdigit():
                part_number = part_number*10+int(grid[row][column])
                for adjacent_row in [-1,0,1]:
                    for adjacent_column in [-1,0,1]:
                        if is_within_bounds(row,adjacent_row,rows,column,adjacent_column,columns):
                            char = grid[row+adjacent_row][column+adjacent_column]
                            if char == '*':
                                gear_positions.add((row+adjacent_row, column+adjacent_column))
            elif part_number>0:
                for gear in gear_positions:
                    gears[gear].append(part_number)
                part_number = 0
                gear_positions = set()    

    return gears    

def get_sum_of_gear_ratios(gears):
    total = 0
    for key,value in gears.items():
        if len(value)==2:
            total += value[0]*value[1]
    return total

def solve(filepath):
    data = open(filepath).read().strip()
    lines = data.split('\n')
    grid = [[char for char in line] for line in lines]
    rows = len(grid)
    columns = len(grid[0])

    gears = get_gears_with_parts(grid, rows, columns)
    return get_sum_of_gear_ratios(gears)

print(solve("test_input.txt"))
print(solve("input.txt"))