from collections import Counter

def get_hand_value(cards):
    deck_options = '23456789TJQKA'
    cards = [deck_options.index(card) for card in cards]
    counted_cards = Counter(cards)
    hand_pattern = tuple(sorted(counted_cards.values()))
    score = [(1,1,1,1,1),(1,1,1,2),(1,2,2),(1,1,3),(2,3),(1,4),(5,)].index(hand_pattern)
    return (score, *cards)

def solve(filepath):
    lines = [i for i in open(filepath).read().split('\n') if i.strip()]
    hand_values = sorted((get_hand_value(hand), int(bet)) for hand, bet in (line.split() for line in lines))
    total = 0
    for rank,(_,bet) in enumerate(hand_values):
        total+=rank*bet+bet
    print(total)

solve("test_input.txt")
solve("input.txt")