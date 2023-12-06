from difflib import SequenceMatcher
import time

def solve(filepath):
    start = time.time()
    input = open(filepath, "r")
    cubes = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    def parse_games(input):
        return [
            {
                "game_id": int(game[0]),
                "pulls": [list(map(str.split, pull.split(", "))) for pull in game[1].split("; ")]
            }
            for game in (extract_data("Game %: %", line) for line in input)
        ]

    def extract_data(template, line):
        seq = SequenceMatcher(None, template, line, True)
        return [line[c:d] for tag, a, b, c, d in seq.get_opcodes() if tag == 'replace']

    def is_good_pull(pull):
        for color in pull:
            if cubes[color[1]] < int(color[0]):
                return False
        return True

    def is_good_game(pulls):
        for pull in pulls:
            if not is_good_pull(pull):
                return False
        return True

    def get_sum_of_good_games(data):
        sum = 0
        for game in data:
            if is_good_game(game['pulls']):
                sum += game['game_id']
        return sum

    data = parse_games(input)
    print(get_sum_of_good_games(data))
    input.close()

    end = time.time()
    total_time = end - start
    print("Total runtime was: " + str(total_time))

solve("test_input.txt")
solve("input.txt")