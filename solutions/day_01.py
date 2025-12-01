from utils.read_input import read_input

def wrap_number(num):
    """
    Ensure the number is within the range 0-99 inclusive.
    If num is negative, wrap around from 100. (e.g., -1 becomes 99)
    If num is greater than 99, wrap around from 0. (e.g., 100 becomes 0)
    0-99 remain unchanged.
    Continue wrapping until the number is within range.
    """
    while True:
        if num < 0:
            num =  100 + num
        elif num > 99:
            num =  num - 100
        else:
            return num
        

def day_one_part_one():
    """Solve Day 1, Part 1 of the challenge."""

    # Get input and initialize variables
    inp = read_input("inputs/day_01.txt")
    dial_point = 50
    total_zeros = 0

    # Process each instruction
    for line in inp:
        # L means turn left (decrease), R means turn right (increase)
        if line[0] == "L":
            dial_point -= int(line[1:])
        else:
            dial_point += int(line[1:])

        # Wrap around if out of bounds (0-99)
        if dial_point < 0 or dial_point > 99:
            dial_point = wrap_number(dial_point)
        
        # Count how many times the dial hits 0
        if dial_point == 0:
            total_zeros += 1

    print(f"Total times dial hit 0: {total_zeros}")
    return total_zeros
    

day_one_part_one()