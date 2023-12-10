PIPE_MAP = {
    "|": ["n", "s"],
    "-": ["w", "e"],
    "L": ["n", "e"],
    "J": ["n", "w"],
    "7": ["s", "w"],
    "F": ["s", "e"],
    'S': ["n", "s", "w", "e"],
}
DIRECTIONS_MAP = {
    "n": (-1, 0, "s"),
    "s": (1, 0, "n"),
    "w": (0, -1, "e"),
    "e": (0, 1, "w"),
}

def within_bounds(direction, height, width):
    y, x = direction
    if y < 0 or y >= height:
        return False
    if x < 0 or x >= width:
        return False
    return True

def find_start(grid):
    for y, line in enumerate(grid):
        if 'S' in grid[y]:
            x = line.index('S')
            return (y,x)

def walk_the_loop(grid, grid_height, grid_width, S):
    visited_pipes = dict()
    next_pipes = [(S, 0)]
    
    while len(next_pipes) > 0:
        current_pipe, distance = next_pipes.pop(0)

        if current_pipe in visited_pipes:
            continue
        
        visited_pipes[current_pipe] = distance

        y, x = current_pipe
        valid_directions = PIPE_MAP[grid[y][x]]

        for direction in valid_directions:
            dy, dx, opposite_direction = DIRECTIONS_MAP[direction]
            new_direction = (y + dy, x + dx)

            if not within_bounds(new_direction, grid_height, grid_width):
                continue

            target = grid[new_direction[0]][new_direction[1]]
            
            if target not in PIPE_MAP:
                continue
            
            target_directions = PIPE_MAP[target]
            
            if opposite_direction in target_directions:
                next_pipes.append((new_direction, distance + 1))
    
    return visited_pipes

def solve(filepath):
    grid = [list(line.strip()) for line in open(filepath)]
    start = find_start(grid)
    grid_height = len(grid)
    grid_width = len(grid[0])

    visited_pipes = walk_the_loop(grid, grid_height, grid_width, start)
    max_distance = max(visited_pipes.values())
    print(max_distance)

solve("test_input.txt")
solve("input.txt")