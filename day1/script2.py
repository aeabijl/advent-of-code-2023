import time
start = time.time()

input = open("input1.txt", "r")
sum = 0

def convert_strings_to_digits(input_string):
    valid_digits = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    matches = []

    for word, digit in valid_digits.items():
        index = input_string.find(word)
        while index != -1:
            matches.append((digit, index))
            index = input_string.find(word, index + 1)

    return matches

for line in input:
    digits = convert_strings_to_digits(line)

    for index, c in enumerate(line):
        if c.isdigit():
            digits.append((int(c), index))

    # lambda to sort by index so we can easily grab first and last
    digits.sort(key=lambda x: x[1])
    calibration_value = int(str(digits[0][0]) + "" + str(digits[-1][0]))
    sum += calibration_value

input.close()
print(sum)
end = time.time()
total_time = end - start
print("Total runtime was: " + str(total_time))