test_input = open("test_input.txt").read().splitlines()
puzzle_input = open("input.txt").read().splitlines()

def solve(input):
    part_number = []
    should_check = False
    valid = False
    total = 0

    for line_index in range(len(input)):
        for char_index in range(len(input[0])):
            if input[line_index][char_index].isdigit():
                part_number.append(input[line_index][char_index])
                should_check = True
            else:
                if should_check and valid:
                    total += int("".join(part_number))
                should_check = False
                valid = False
                part_number = []

            if should_check and not valid:
                for adjacent_char_index in [0,-1,1]:
                    for adjacent_line_index in [0,-1,1]:
                        if adjacent_char_index == adjacent_line_index == 0 or  char_index+adjacent_char_index in [-1,len(input[0])] or line_index+adjacent_line_index in [-1,len(input)]:
                            continue
                        
                        if not input[line_index+adjacent_line_index][char_index+adjacent_char_index].isdigit() and input[line_index+adjacent_line_index][char_index+adjacent_char_index] != ".":
                            valid = True
    return total

print(solve(test_input))
print(solve(puzzle_input))