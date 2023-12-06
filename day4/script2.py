def get_number_of_matches(card): 
    winning_numbers, card_numbers = [side.split()
                      for side in card.strip().split(': ')[1].split(' | ')] 
    return sum(1 for n in card_numbers if n in winning_numbers)

def solve(filepath):
    input = open(filepath)
    card_data = [line for line in input]
    cards = [1] * len(card_data)

    for index, card in enumerate(card_data):
        number_of_matches = get_number_of_matches(card)
        for line in range(1, number_of_matches + 1):
            cards[index + line] += cards[index]

    return sum(cards)

print(solve("test_input.txt"))
print(solve("input.txt"))