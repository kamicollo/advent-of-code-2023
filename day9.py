import re

data = [[int(n) for n in re.findall("-?\d+", l)] for l in list(open("data/day9.txt"))]

# part 1

extrapolations = []
for seq in data:
    pyramid = [seq]
    diffs = seq
    while not all([n == 0 for n in diffs]):
        diffs = [x - y for x, y in zip(diffs[1:], diffs[:-1])]
        pyramid.append(diffs)
    diffs.append(0)
    reverse_pyramid = list(reversed(pyramid))
    for a, b in zip(reverse_pyramid[:-1], reverse_pyramid[1:]):
        b.append(b[-1] + a[-1])
    extrapolations.append(b[-1])

print(sum(extrapolations))

# part 2

extrapolations = []
for seq in data:
    pyramid = [seq]
    diffs = seq
    while not all([n == 0 for n in diffs]):
        diffs = [x - y for x, y in zip(diffs[1:], diffs[:-1])]
        pyramid.append(diffs)
    diffs.append(0)
    reverse_pyramid = list(reversed(pyramid))
    for a, b in zip(reverse_pyramid[:-1], reverse_pyramid[1:]):
        b.insert(0, b[0] - a[0])
    extrapolations.append(b[0])

print(sum(extrapolations))
