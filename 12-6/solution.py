# Yes I know re is not the fastest, but it's easier to read and the speed difference is trivial given that the input is two lines long

import functools, re


def beats_record(charging_time: int, race_time: int, race_record: int) -> bool:
	return (race_time - charging_time) * charging_time > race_record


def ways_to_win(race_time: int, race_record: int) -> int:
	lower_bound = upper_bound = 0
	for charging_time in range(race_time - 1):
		if beats_record(charging_time, race_time, race_record):
			lower_bound = charging_time
			break
	for charging_time in range(race_time - 1, 0, -1):
		if beats_record(charging_time, race_time, race_record):
			upper_bound = charging_time
			break

	return upper_bound - lower_bound + 1


def solve_one(data: list[str]) -> int:
	times = [int(i) for i in re.findall("\d+", data[0])]
	distances = [int(i) for i in re.findall("\d+", data[1])]
	race_data = [(times[i], distances[i]) for i in range(len(times))]

	return functools.reduce(lambda a, b: a*b, [ways_to_win(d[0], d[1]) for d in race_data])


def solve_two(data: list[str]) -> int:
	race_time = int("".join(re.findall("\d+", data[0])))
	race_record = int("". join(re.findall("\d+", data[1])))

	return ways_to_win(race_time, race_record)


if __name__ == "__main__":
    data = open("input.txt").read().split("\n")
    print(solve_one(data))
    print(solve_two(data))