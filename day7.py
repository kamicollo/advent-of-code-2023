from functools import cmp_to_key
from collections import Counter
from pprint import pprint

file = "data/day7.txt"

raw_cards = [s[:-1].split(" ") for s in list(open(file))]
PART1 = False


def strength(card):
    c = Counter(list(card))
    if PART1:
        v = max(c.values())
    else:
        jokers = 0 if "J" not in c else c["J"]
        del c["J"]

        non_jokers = 0 if len(c) == 0 else max([n for k, n in c.items() if k != "J"])
        if non_jokers == 0:
            v = 5
        else:
            v = non_jokers + jokers
            max_position = list(c.values()).index(non_jokers)
            max_key = list(c.keys())[max_position]
            c[max_key] += jokers

    if v == 3 and 2 in c.values():
        v = 3.5
    if v == 2 and len([x for x in c.values() if x == 2]) == 2:
        v = 2.5
    return v


cards = [{"hand": x[0], "bid": x[1], "strength": strength(x[0])} for x in raw_cards]

if PART1:
    order = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
else:
    order = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]


def poker_sort(a, b):
    if a["hand"] == b["hand"]:
        return 0
    elif a["strength"] > b["strength"]:
        return 1
    elif a["strength"] < b["strength"]:
        return -1
    else:
        first_mismatch = (
            [(x, y) for x, y in zip(list(a["hand"]), list(b["hand"])) if x != y]
        )[0]
        if order.index(first_mismatch[0]) < order.index(first_mismatch[1]):
            return 1
        else:
            return -1


sorted_cards = sorted(cards, key=cmp_to_key(poker_sort))

pprint(sorted_cards)
print(sum((i + 1) * int(c["bid"]) for i, c in enumerate(sorted_cards)))
