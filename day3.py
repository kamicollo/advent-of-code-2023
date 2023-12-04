import numpy as np
import re
from math import prod


with open('data/day3.txt', 'r') as f:
    data = f.readlines()

#the new line characters really got me \--(-_-)--/
symbols = [[0 if s.isdigit() or s == "." else 1 for s in list(row)[:-1]] for row in data]
gears = [[1 if s == "*" else 0 for s in list(row)[:-1]] for row in data]

# process locations with symbols
symbol_rows, symbol_columns = np.where(np.array(symbols) > 0)
symbol_locations = {(x, y) for x, y in zip(symbol_rows, symbol_columns)}

# process locations with gears
gear_locations = {(x, y): [] for x, y in zip(*np.where(np.array(gears) > 0))}

# process numbers
numbers = []
for x, line in enumerate(data):
    for number in re.finditer(r"\d+", line):
        number_area = {
            (x_offset, y_offset)
            for x_offset in [x - 1, x, x + 1]
            for y_offset in range(number.start() - 1, number.end() + 1)
        }

        if number_area.intersection(symbol_locations):
            numbers.append(int(number.group()))

        for gear_location in number_area.intersection(gear_locations.keys()):
            gear_locations[gear_location].append(int(number.group()))

#part 1
print(sum(numbers))

#part 2
print(sum([prod(ns) for ns in gear_locations.values() if len(ns) > 1]))

