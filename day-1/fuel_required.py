# Advent of Code - 2019
# Puzzle 1

import sys
sys.path.insert(1, '../common')

import math
from read_fxns import read_file_into_list

def calc_fuel_from_mass(mass):
    """ Given the mass of a spacecraft module return the required fuel to launch
    it
    """
    fuel = math.floor(mass/3) - 2
    return fuel

def calc_fuel_till_wish(mass):
    """ Now we also need to calculate the amount of fuel required for our fuel.
    """
    needed_fuel = calc_fuel_from_mass(mass)
    fuel_sum = 0
    while (needed_fuel > 0):
        fuel_sum += needed_fuel
        needed_fuel = calc_fuel_from_mass(needed_fuel)

    return (fuel_sum)

def calc_total_fuel(int_list):
    """
    For each module's mass in the given list, calculate the fuel required
    for the module and create a new list with these values
    """
    fuel_list = [calc_fuel_from_mass(x) for x in int_list]
    return fuel_list

def calc_true_total_fuel(int_list):
    fuel_list = [calc_fuel_till_wish(x) for x in int_list]
    return fuel_list

# Grab the list of mass values as ints
mass_list = read_file_into_list("aoc_1.txt")

# Calculate fuel needed for each module
#fuel_list = calc_total_fuel(mass_list)

# Calculate true fuel needed for each module (taking into account fuel needed for fuel)
fuel_list = calc_true_total_fuel(mass_list)

# Sum items in list
sum = 0
for x in fuel_list:
    sum += x

print(sum)
