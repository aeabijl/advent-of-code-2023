def resolve_histories(history):
    if sum(number != 0 for number in history) == 0:
        return 0
    
    additional_sequence = []
    
    for number in range(len(history)-1):
        additional_sequence.append(history[number+1]-history[number])

    return history[-1] + resolve_histories(additional_sequence)

def solve(filepath):
    oasis_histories = [[int(number) for number in line.split()] for line in open(filepath).read().strip().split('\n')]
    # invert the list instead of going from right to left.
    result = sum(resolve_histories(history[::-1]) for history in oasis_histories)
    print(result)

solve("test_input.txt")
solve("input.txt")