import time

def solve(filepath):
    start = time.time()
    input = open(filepath, "r")
    sum = 0

    for line in input:
        first = None
        last = None
        for c in line:
            if c.isdigit():
                if first is None:
                    first=c
                last=c
        calibration_value = (int(first + "" + last)) 
        sum += calibration_value

    input.close()
    print(sum)
    end = time.time()
    total_time = end - start
    print("Total runtime was: " + str(total_time))

solve("test_input.txt")
solve("input.txt")