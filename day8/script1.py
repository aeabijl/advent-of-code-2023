from collections import namedtuple
from itertools import cycle

# Makes fields accessible by name, e.g. x.L
LR = namedtuple("LR", "L R")

def prepare_input(filepath):
    instructions,raw_nodes = [split for split in open(filepath).read().strip().split('\n\n')]
    nodes = {}
    
    for node in raw_nodes.splitlines():
        node, directions = node.split(' = ')
        left, right = directions.strip()[1:-1].split(", ")
        nodes[node] = LR(left, right)
    
    return instructions, nodes

def solve(filepath):
    instructions,nodes = prepare_input(filepath)

    node = 'AAA'
    steps = 0
    for direction_ in cycle(instructions.strip()):
        steps += 1
        if direction_ == 'L':
            next_node = nodes[node].L
        else:
            next_node = nodes[node].R
        
        node = next_node
        if node == 'ZZZ':
            break
    print(steps)

solve("test_input.txt")
solve("input.txt")