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
                    offset = d1 - s1
                    if s2 <= r1 or r2 <= s1:
                        continue
                    if r1 < s1:
                        current_ranges.append((r1, s1))
                        r1 = s1
                    if s2 < r2:
                        current_ranges.append((s2, r2))
                        r2 = s2
                    destination_ranges.append((r1 + offset, r2 + offset))
                    break
                else:
                    destination_ranges.append((r1, r2))
            current_ranges = destination_ranges
            destination_ranges = []
        location_ranges += current_ranges # what is left over at the end
    return location_ranges


if __name__ == "__main__":
    data = open("input.txt").read().split("\n\n")
    seeds, resources = parse_data(data)
    locations = [destination(seed, resources) for seed in seeds]
    print(min(locations))
    seed_ranges = [(seeds[i], seeds[i] + seeds[i+1]) for i in range(0, len(seeds), 2)]
    print(min([r[0] for r in get_range_overlap(seed_ranges, resources)]))