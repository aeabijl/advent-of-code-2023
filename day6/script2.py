import time

def is_record(hold, time, distance):
    return hold * (time - hold) > distance

def first_best_score_left(time, distance):
    low, high = 0, time
    while low < high:
        middle_button_hold = low + (high - low >> 1)
        if is_record(middle_button_hold, time, distance):
            high = middle_button_hold
        else:
            low = middle_button_hold + 1
    return low


def first_best_score_right(time, distance):
    low, high = 0, time
    while low <= high:
        middle_button_hold = low + (high - low >> 1)
        if is_record(middle_button_hold, time, distance):
            low = middle_button_hold + 1
        else:
            high = middle_button_hold - 1
    return high

def determine_number_of_ways_to_win(time, distance):
    return first_best_score_right(time, distance) - first_best_score_left(time, distance) + 1


def solve(filepath):
    start=time.time()
    lines=open(filepath).read().strip().split('\n')
    race_time,distance=[int(''.join(line.split()[1:]))for line in lines]

    result = determine_number_of_ways_to_win(race_time, distance)
    print(result)

    end = time.time()
    total_time = end - start
    print("Total runtime was: " + str(total_time))

solve("test_input.txt")
solve("input.txt")