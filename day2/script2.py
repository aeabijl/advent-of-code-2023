from difflib import SequenceMatcher
import time

def solve(filepath):
    start = time.time()
    input = open(filepath, "r")

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

    def get_power_of_game(pulls):
        minimum_cubes = {
        "red": 0,
        "green": 0,
        "blue": 0
        }
        for pull in pulls:
            for color in pull:
                if minimum_cubes[color[1]] < int(color[0]):
                    minimum_cubes[color[1]] = int(color[0])
        return minimum_cubes["red"] * minimum_cubes["green"] * minimum_cubes["blue"]

    def get_sum_of_powers(data):
        sum = 0
        for game in data:
            sum += get_power_of_game(game["pulls"])
        return sum

    data = parse_games(input)
    print(get_sum_of_powers(data))
    input.close()

    end = time.time()
    total_time = end - start
    print("Total runtime was: " + str(total_time))

solve("test_input.txt")
solve("input.txt")