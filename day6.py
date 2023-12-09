import re

file = "data/day6.txt"

PART1 = False
if PART1:
    times, distances = [
        [int(n) for n in re.findall("\d+", s)] for s in list(open(file))
    ]
else:
    times, distances = [[int("".join(re.findall("\d+", s)))] for s in list(open(file))]

total_ways_to_win = 1
for race, (t, d) in enumerate(zip(times, distances)):
    min_time = 0
    max_time = t
    while min_time * (t - min_time) < d:
        min_time += 1
    while max_time * (t - max_time) < d:
        max_time -= 1
    ways_to_win = max_time - min_time + 1
    total_ways_to_win *= ways_to_win

print(total_ways_to_win)
