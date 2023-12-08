from math import prod
import time

def is_record(hold, time, distance):
    return hold * (time - hold) > distance

def get_lower_boundary(time, distance):
    low, high = 0, time
    while low < high:
        middle_button_hold = low + (high - low >> 1)
        if is_record(middle_button_hold, time, distance):
            high = middle_button_hold
        else:
            low = middle_button_hold + 1
    return low


def get_upper_boundary(time, distance):
    low, high = 0, time
    while low <= high:
        middle_button_hold = low + (high - low >> 1)
        if is_record(middle_button_hold, time, distance):
            low = middle_button_hold + 1
        else:
            high = middle_button_hold - 1
    return high

def determine_number_of_ways_to_win(time, distance):
    return get_upper_boundary(time, distance) - get_lower_boundary(time, distance) + 1


def solve(filepath):
    start = time.time()
    lines=open(filepath).read().strip().split('\n')
    times,distances=[int(time)for time in lines[0].split(':')[1].split()],[int(distance)for distance in lines[1].split(':')[1].split()]
    races = list(zip(times, distances))
    
    result = prod(determine_number_of_ways_to_win(time, distance) for time, distance in races)
    print(result)

    end = time.time()
    total_time = end - start
    print("Total runtime was: " + str(total_time))


solve("test_input.txt")
solve("input.txt")