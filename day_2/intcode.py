# Advent of Code - 2019
# Puzzle 2

""" Your puzzle input is the gravity assist program. You will restore this
    program to the '1202 program alarm' state, from before the fire. To do so,
    before running the program, replace position '1' with the value '12' and
    replace position '2' with the value '2'.

    What value is left at position 0 after the program halts?
"""
def intcode(ints):
    """ A representation of an Intcode computer

    The computer takes a list of integers as input. It then iterates over the
    list running the following algorithm:
        If a 1 is encountered at position 'x', positions 'x + 1' and 'x + 2'
        represent positions of values to be added together.
        Likewise, if a 2 is encountered, then the values at positions 'x + 1'
        and 'x + 2' represent positions of values to be multiplied together.
    """
    for x in range(len(ints)):
        res_pos = ints[x+3]
        arg_1_pos = ints[x+1]
        arg_2_pos = ints[x+2]
        if ints[x] == 1:
            ints[res_pos] = ints[arg_1_pos] + ints[arg_2_pos]
        elif ints[x] == 2:
            ints[res_pos] = ints[arg_1_pos] * ints[arg_2_pos]
        x += 4 # go to the next instruction

    return ints
