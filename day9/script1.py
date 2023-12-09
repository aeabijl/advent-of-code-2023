def resolve_history(history):
    # prevent list index out of range errors. 
    # If we are at a history of 0 we are done.
    if sum(number != 0 for number in history) == 0:
        return 0
    
    additional_sequence = []
    
    for number in range(len(history)-1):
        additional_sequence.append(history[number+1]-history[number])

    return history[-1] + resolve_history(additional_sequence)

def solve(filepath):
    oasis_histories = [[int(number) for number in line.split()] for line in open(filepath).read().strip().split('\n')]
    result = sum(resolve_history(history) for history in oasis_histories)
    print(result)

solve("test_input.txt")
solve("input.txt")