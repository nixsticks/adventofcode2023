import re


def parse_data(data: list[str]):
    seeds = [int(i) for i in re.findall("\d+", data[0])]
    resources = [[[int(i) for i in line.strip().split(" ")] for line in m.split("\n")[1:]] for m in data[1:]]
    return seeds, resources


def destination(source_value, resources):
    current_value = source_value
    for resource in resources:
        for _range in resource:
            dest_start, source_start, span = _range
            if current_value in range(source_start, source_start + span):
                current_value = dest_start + (current_value - source_start)
                break

    return current_value


def get_range_overlap(seed_ranges, resources):
    location_ranges = []
    for seed_range in seed_ranges:
        current_ranges, destination_ranges = [seed_range], []
        for resource in resources:
            while len(current_ranges) > 0:
                r1, r2 = current_ranges.pop()
                for resource_range in resource:
                    d1, s1, span = resource_range
                    s2 = s1 + span
                    # If the current range does not overlap with the source range
                    if s2 <= r1 or r2 <= s1:
                        continue
                    # If the current range starts before the source range, put the subrange on the stack
                    # for later and shorten the current range under examination
                    if r1 < s1:
                        current_ranges.append((r1, s1))
                        r1 = s1
                    # If the current range extends beyond the source range, put the subrange on the stack
                    # for later and shorten the current range under examination
                    if s2 < r2:
                        current_ranges.append((s2, r2))
                        r2 = s2
                    # Append our current result to the destination ranges to be examined when we move to the 
                    # next map, adding the offset required to change it to the destination range
                    destination_ranges.append((r1 + (d1 - s1), r2 + (d1 - s1)))
                    break
                else:
                    # The current range did not overlap with any of the source ranges so append as is
                    destination_ranges.append((r1, r2))
            current_ranges = destination_ranges
            destination_ranges = []
        # Whatever is left over at the end is the location ranges
        location_ranges += current_ranges
    return location_ranges


if __name__ == "__main__":
    data = open("input.txt").read().split("\n\n")
    seeds, resources = parse_data(data)
    locations = [destination(seed, resources) for seed in seeds]
    print(min(locations))
    seed_ranges = [(seeds[i], seeds[i] + seeds[i+1]) for i in range(0, len(seeds), 2)]
    print(min([r[0] for r in get_range_overlap(seed_ranges, resources)]))