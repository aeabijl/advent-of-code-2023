from collections import namedtuple
from itertools import cycle
from math import lcm

# Makes fields accessible by name, e.g. x.L
LR = namedtuple("LR", "L R")

def prepare_input(filepath):
    instructions,raw_nodes = [x for x in open(filepath).read().strip().split('\n\n')]
    nodes = {}
    
    for node in raw_nodes.splitlines():
        node, directions = node.split(' = ')
        left, right = directions.strip()[1:-1].split(", ")
        nodes[node] = LR(left, right)
    
    return instructions, nodes

def walk_path(node, instructions, nodes):
    steps = 0
    for direction_ in cycle(instructions.strip()):
        steps += 1
        if direction_ == 'L':
            next_node = nodes[node].L
        else:
            next_node = nodes[node].R
        
        node = next_node
        if node.endswith('Z'):
            break
    return steps

def solve(filepath):
    instructions,nodes = prepare_input(filepath)
    start_nodes = [node for node in nodes if node.endswith('A')]
    # Determine how many steps each start node needs to end up at Z
    steps = [walk_path(start_node, instructions, nodes) for start_node in start_nodes]
    # Based on this, we need to find one number of steps that all these steps have in common.
    # That is where they will all end up on Z at the same time. 
    # For this the Least Common Multiple works great.
    result = lcm(*steps)
    print(result)

solve("test_input.txt")
solve("test_input2.txt")
solve("input.txt")