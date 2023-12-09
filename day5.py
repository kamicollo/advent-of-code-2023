import re
from collections import defaultdict
import logging

logging.basicConfig(level=logging.INFO)

data_map = defaultdict(dict)
full_data_map = defaultdict(dict)

source = None
PART2 = False

with open("data/day5.txt") as f:
    for line in f.readlines():
        if (map_match := re.match("(.+)-to-(.+) map:\s", line)) is not None:
            source = map_match.group(1)
            dest = map_match.group(2)
        elif "seeds" in line:
            initial_seeds = [int(n.group(0)) for n in re.finditer("\d+", line)]
            # part 1
            if not PART2:
                for seed in initial_seeds:
                    data_map["seed"][(seed, seed)] = (seed, seed)
            else:
                # part 2
                for i, (seed_start, seed_length) in enumerate(
                    zip(initial_seeds[:-1], initial_seeds[1:])
                ):
                    if i % 2 == 0:
                        logging.info(f"{seed_start} -> {seed_start + seed_length}")
                        data_map["seed"][(seed_start, seed_start + seed_length)] = (
                            seed_start,
                            seed_length + seed_start,
                        )
        elif len(line) > 1:
            dest_start, source_start, length = [
                int(x) for x in line[:-1].split(" ") if x != ""
            ]
            # produce ranges
            temp_copy = data_map[source].copy()
            source_end = source_start + length - 1
            dest_end = dest_start + length - 1
            coordinate_conversion = -source_start + dest_start
            logging.info(
                f"Using mapping {source_start}-{source_end} -> {dest_start}-{dest_end} [coord shift: {coordinate_conversion}]"
            )
            for (k_start, k_end), (v_start, v_end) in data_map[source].items():
                start_offset = max(0, max(k_start, source_start) - k_start)
                end_offset = min(0, min(k_end, source_end) - k_end)
                if (source_start <= k_start and source_end >= k_start) or (
                    source_start <= k_end and source_end >= k_end
                ):
                    data_map[dest][
                        (
                            k_start + start_offset + coordinate_conversion,
                            k_end + end_offset + coordinate_conversion,
                        )
                    ] = (v_start + start_offset, v_end + end_offset)
                    logging.info(
                        f"Adding mapping: {source}[{(k_start + start_offset, k_end + end_offset)}] -> "
                        f"{dest}[{(k_start + start_offset + coordinate_conversion,k_end + end_offset + coordinate_conversion)}]"
                        f"for seed {(v_start + start_offset, v_end + end_offset)}"
                    )
                    if start_offset != 0:
                        temp_copy[(k_start, k_start + start_offset - 1)] = (
                            v_start,
                            v_start + start_offset - 1,
                        )
                    if end_offset != 0:
                        temp_copy[(k_end + end_offset + 1, k_end)] = (
                            v_end + end_offset + 1,
                            v_end,
                        )
                    temp_copy.pop((k_start, k_end))

            data_map[source] = temp_copy.copy()

        elif source is not None:
            # copy over initial IDs if not in range
            for (k_start, k_end), (v_start, v_end) in data_map[source].items():
                logging.info(
                    f"Adding 1:1 mapping: {source}[{(k_start, k_end)}] -> "
                    f"{dest}[{(k_start, k_end)}] for seed {(v_start, v_end)}"
                )
                data_map[dest][(k_start, k_end)] = (v_start, v_end)

# final processing of locations
for k, v in data_map[source].items():
    for (k_start, k_end), (v_start, v_end) in data_map[source].items():
        logging.info(
            f"Adding 1:1 mapping: {source}[{(k_start, k_end)}] -> "
            f"{dest}[{(k_start, k_end)}] for seed {(v_start, v_end)}"
        )
        data_map[dest][(k_start, k_end)] = (v_start, v_end)


print(min(data_map["location"].keys()))
print(min(data_map["location"].keys())[0])
