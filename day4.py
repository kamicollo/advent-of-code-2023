import re
from collections import defaultdict

data = list(open("data/day4.txt"))

pattern = re.compile("Card\s+\d+:\s*((\d+\s*)*)\|\s*((\d+\s*)*)\s")

numbers = [
    (pattern.match(r).group(1).split(" "), pattern.match(r).group(3).split(" "))
    for r in data
]

matches = [
    len(
        {int(w) for w in win_numbers if w != ""}.intersection(
            {int(n) for n in my_numbers if n != ""}
        )
    )
    for win_numbers, my_numbers in numbers
]

# part 1
points = [2 ** (m - 1) for m in matches if m > 0]
print(sum(points))

# part 2
tracker = defaultdict(lambda: 0)

for i, m in enumerate(matches):
    tracker[i] += 1
    for _ in range(tracker[i]):
        for k in range(i + 1, i + m + 1):
            tracker[k] += 1

print(sum(tracker.values()))
