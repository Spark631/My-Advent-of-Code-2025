import math

inputs = 0
with open("puzzle_input/day01.txt", "r") as f:
    x = f.readlines()
    inputs = [y.rstrip('\n') for y in x]

def unlock(inputs):
    lock = 50
    answer = 0
    for comb in inputs:
        direction = comb[0]
        ticks = int(comb[1:])

        if direction == "R":
            lock = (lock + ticks) % 100
            if lock == 0:
                answer += 1
        elif direction == "L":
            lock = (lock - ticks) % 100
            if lock == 0:
                answer += 1
    return answer

unlock(inputs)