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

def get_start_piece(grid, grid_height, grid_width, S, visited_pipes):
    reachable_directions = []
    y, x = S

    for direction in DIRECTIONS_MAP:
        dy, dx, opposite = DIRECTIONS_MAP[direction]
        new_direction = (y + dy, x + dx)

        if not within_bounds(new_direction, grid_height, grid_width):
            continue

        if new_direction not in visited_pipes:
            continue

        target = grid[new_direction[0]][new_direction[1]]

        if target not in PIPE_MAP:
            continue
        
        target_directions = PIPE_MAP[target]

        if opposite not in target_directions:
            continue

        reachable_directions.append(direction)
    
    for pipe_piece in PIPE_MAP:
        if len(reachable_directions) == len(PIPE_MAP[pipe_piece]):
            if all([direction in PIPE_MAP[pipe_piece] for direction in reachable_directions]):
                return pipe_piece
    return None

def create_enclosed_grid(grid, grid_height, grid_width, visited_pipes):
    for y in range(grid_height):
        norths = 0
        for x in range(grid_width):
            place = grid[y][x]
            if (y,x) in visited_pipes:
                pipe_directions = PIPE_MAP[place]
                if "n" in pipe_directions:
                    norths += 1
                continue
            if norths % 2 == 0:
                grid[y][x] = "O"
            else:
                grid[y][x] = "I"
    return grid

def solve(filepath):
    grid = [list(line.strip()) for line in open(filepath)]
    grid_height = len(grid)
    grid_width = len(grid[0])
    start = find_start(grid)

    visited_pipes = walk_the_loop(grid, grid_height, grid_width, start)
    grid[start[0]][start[1]] = get_start_piece(grid, grid_height, grid_width, start, visited_pipes)

    enclosed_grid = create_enclosed_grid(grid, grid_height, grid_width, visited_pipes)

    total = sum(line.count('I') for line in enclosed_grid)
    print(total)


solve("test_input.txt")
solve("test_input2.txt")
solve("input.txt")