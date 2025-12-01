from utils.read_input import read_input

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
            dial_point = abs(dial_point % 100)
        
        # Count how many times the dial hits 0
        if dial_point == 0:
            total_zeros += 1
    
    print(f"Total times dial hit 0: {total_zeros}")
    return total_zeros
    

day_one_part_one()