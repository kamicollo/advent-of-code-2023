import re
import itertools
import math

data = list(open("data/day8.txt"))
directions = itertools.cycle(list(data[0])[:-1])
raw_map = [re.findall("[0-9A-Z]{3}", line) for line in data[2:]]
maps = {x: (y, z) for x, y, z in raw_map}

PART1 = False

if PART1:
    # part 1
    location = "AAA"
    steps = 0
    while location != "ZZZ":
        location = maps[location][0 if next(directions) == "L" else 1]
        steps += 1
    print("Part1 ", steps)

else:
    # part 2
    steps_required = {k: None for k in maps.keys() if k[2] == "A"}
    locations = [k for k in maps.keys() if k[2] == "A"]
    steps = 0
    while not all(l is not None for l in steps_required.values()):
        direction = next(directions)
        steps += 1
        for i, location in enumerate(locations):
            locations[i] = maps[location][0 if direction == "L" else 1]
            if locations[i][2] == "Z":
                steps_required[list(steps_required.keys())[i]] = steps
    print(math.lcm(*steps_required.values()))
