import re
from collections import deque
from operator import itemgetter

# For converting the string lines into integers
def get_integers(string, negatives: bool=True):
    exp = r'-?\d+' if negatives else r'\d+'
    if isinstance(string, bytes):
        exp = exp.encode()
    return list(map(int, re.findall(exp, string)))

def overlapping(a, b, c, d):
    return not (a > d or b < c)

def process_mappings(seed_ranges, maps):
    for map in maps:
        new_ranges = deque()

        while seed_ranges:
            smallest_seed, largest_seed = seed_ranges.popleft()

            for destination, source, size in map:
                smallest_map, largest_map = source, source + size - 1
                delta = destination - source

                if not overlapping(smallest_seed, largest_seed, smallest_map, largest_map):
                    continue

                # SM--SS--LS--LM completely inside
                # ====================================
                if smallest_map <= smallest_seed <= largest_map and smallest_map <= largest_seed <= largest_map:
                    new_ranges.append((smallest_seed + delta, largest_seed + delta))
                    break

                # SS--SM--LS--LM escapes left
                # ====================================
                if smallest_map <= largest_seed <= largest_map:
                    # SM--LS (overlap)
                    new_ranges.append((smallest_map + delta, largest_seed + delta))
                    # SS--SM (no overlap)
                    seed_ranges.append((smallest_seed, smallest_map - 1))
                    break

                # SM--SS--LM--LS escapes right
                # ====================================
                if smallest_map <= smallest_seed <= largest_map:
                    # SM--SS (overlap)
                    new_ranges.append((smallest_seed + delta, largest_map + delta))
                    # LM--LS (no overlap)
                    seed_ranges.append((largest_map + 1, largest_seed))
                    break

                # SS--SM--LM--LS escapes both sides
                # ====================================
                if smallest_seed < smallest_map and largest_seed > largest_map:
                    # SM--LM (overlap)
                    new_ranges.append((smallest_map + delta, largest_map + delta))
                    # SS--SM (no overlap)
                    # LM--LS (no overlap)
                    seed_ranges.extend(((largest_map + 1, largest_seed), (smallest_seed, smallest_map - 1)))
                    break
            else:
                # There is no overlap with any map segment
                new_ranges.append((smallest_seed, largest_seed))

        seed_ranges = new_ranges
    return seed_ranges

def solve(filepath):
    data = open(filepath).read()
    lines = data.split('\n\n')
    seeds = get_integers(lines[0])
    seed_pairs = [seeds[i:i+2] for i in range(0, len(seeds), 2)]
    maps = []

    for line in lines[1:]:
        ints = get_integers(line)
        maps.append([ints[i:i + 3] for i in range(0, len(ints), 3)])

    seed_ranges = [(a, a + b - 1) for a, b in seed_pairs]
    # Deque from the collections module creates a double ended queue. 
    # It's quicker to append and to pop from both ends of the list.
    # deque provides an O(1) time complexity for append and pop operations as compared to a list that provides O(n) time complexity.
    seed_ranges = deque(seed_ranges)

    mapped_locations = process_mappings(seed_ranges, maps)
    result = min(map(itemgetter(0), mapped_locations))
    print(result)

    

solve("test_input.txt")
solve("input.txt")