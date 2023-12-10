data = [list(l[:-1]) for l in open("data/day10.txt")]

start_pos = [(i, x.index("S")) for (i, x) in enumerate(data) if "S" in x][0]

directions = {"N": (-1, 0), "S": (1, 0), "E": (0, 1), "W": (0, -1)}

reverse_directions = {"N": "S", "S": "N", "E": "W", "W": "E"}

connectors = {
    "|": {"N", "S"},
    "-": {"E", "W"},
    "L": {"N", "E"},
    "J": {"N", "W"},
    "7": {"S", "W"},
    "F": {"S", "E"},
    ".": {},
}

loop_closed = False
steps_required = 0
paths = {k: {"locations": [(start_pos)], "direction": k} for k in directions.keys()}

while not loop_closed:
    steps_required += 1
    for path in paths.values():
        x, y = path["locations"][-1]
        x_offset, y_offset = directions[path["direction"]]
        connectivity_required = reverse_directions[path["direction"]]
        new_x = x + x_offset
        new_y = y + y_offset
        if new_x >= 0 and new_x < len(data[0]) and new_y >= 0 and new_y < len(data):
            connector = data[new_x][new_y]
            if connectivity_required in connectors[connector]:
                # we found a match, let's proceed
                new_direction = connectors[connector].difference(
                    {connectivity_required}
                )
                path["direction"] = list(new_direction)[0]
                path["locations"].append((new_x, new_y))
            else:
                # the pipe found doesn't connect - do nothing
                pass
        else:
            # we'd be walking off grid - do nothing
            pass
    # check if any paths overlap
    for k, p in paths.items():
        for k2, p2 in paths.items():
            if k != k2:
                if len(set(p2["locations"]).intersection(set(p["locations"]))) > 1:
                    print(f"paths starting from {k} {k2} connected!")
                    full_loop = set(p2["locations"]).union(set(p["locations"]))
                    loop_closed = True

print(steps_required)
print(full_loop)
