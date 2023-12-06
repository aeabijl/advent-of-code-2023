import re
from math import inf as INFINITY

# For converting the string lines into integers
def get_integers(string, negatives: bool=True):
    exp = r'-?\d+' if negatives else r'\d+'
    if isinstance(string, bytes):
        exp = exp.encode()
    return list(map(int, re.findall(exp, string)))

def solve(filepath):
    data = open(filepath).read()
    lines = data.split('\n\n')
    seeds = get_integers(lines[0])
    maps = []

    for line in lines[1:]:
        ints = get_integers(line)
        maps.append([ints[i:i + 3] for i in range(0, len(ints), 3)])

    # Can't initialize as 0, because the min() check will always pick this.
    # Nothing greater than positive INFINITY I guess!
    result = INFINITY

    for seed in seeds:
        for map in maps:
            for destination, source, size in map:
                source_end = source + size -1
                if source <= seed <= source_end:
                    seed = seed - source + destination
                    break
        result = min(result, seed)

    print(result)

solve("test_input.txt")
solve("input.txt")