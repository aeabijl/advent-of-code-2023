from itertools import combinations

def map_universe(grid):
    empty_rows = set()
    empty_columns = set()
    stars = set()
    for y, x in enumerate(grid):
        if len(set(x)) == 1:
            empty_rows.add(y)
        for index, char in enumerate(grid[y]):
            if char == "#":
                stars.add((y, index))
    for char in range(len(grid[0])):
        if len(set([x[char] for x in grid])) == 1:
            empty_columns.add(char)
    return empty_rows, empty_columns, stars

def calculate_shortest_path(star, expand_level, empty_rows, empty_columns):
    start_star_y, start_star_x = star[0]
    end_star_y, end_star_x = star[1]
    y, x = abs(start_star_y - end_star_y), abs(start_star_x - end_star_x)
    for row in empty_rows:
        if row in range(*sorted((start_star_y, end_star_y))):
            y += expand_level
    for column in empty_columns:
        if column in range(*sorted((start_star_x, end_star_x))):
            x += expand_level
    return y + x

def solve(filepath):
    grid = open(filepath).read().strip().split('\n')
    empty_rows, empty_columns, stars = map_universe(grid)
    star_combinations = set(combinations(stars, 2))
    ten_times_larger_shortest = sum(calculate_shortest_path(star, 10 - 1, empty_rows, empty_columns) for star in star_combinations)
    print(ten_times_larger_shortest)
    hundred_times_larger_shortest = sum(calculate_shortest_path(star, 100 - 1, empty_rows, empty_columns) for star in star_combinations)
    print(hundred_times_larger_shortest)
    million_times_larger_shortest = sum(calculate_shortest_path(star, 1000000 - 1, empty_rows, empty_columns) for star in star_combinations)
    print(million_times_larger_shortest)

solve("test_input.txt")
solve("input.txt")