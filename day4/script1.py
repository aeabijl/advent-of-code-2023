def check_card_score(card): 
    winning_numbers, card_numbers = [side.split()
                      for side in card.strip().split(': ')[1].split(' | ')] 
    score = sum(1 for n in card_numbers if n in winning_numbers)
    return int(2** (score -1))

def solve(filepath): 
    input = open(filepath, "r")
    return sum(check_card_score(line) for line in input)
    
print(solve("test_input.txt"))
print(solve("input.txt"))