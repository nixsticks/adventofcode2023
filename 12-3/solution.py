import re, unittest


def scan_line(data: list[str], x: int) -> list[int]:
    def in_grid(x: int, y: int) -> bool:
        return x >= 0 and y >= 0 and x < len(data) and y < len(data[0])

    part_numbers = []
    line = data[x]

    for match in re.finditer("\d+", line):
        start, end = match.start(), match.end()
        n = int(line[start:end])
        bordering = [data[i][j] for i in [x - 1, x + 1] for j in range(start - 1, end + 1) if in_grid(i, j)] + [data[x][j] for j in [start - 1, end] if in_grid(x, j)]
        for border in bordering:
            if re.match("[^\d.]", border):
                part_numbers.append(n)
                break

    return part_numbers


def gear_ratios(data: list[str]) -> list[int]:
    def in_grid(x: int) -> bool:
        return x >= 0 and x < len(data)

    stars = [(x,y) for x in range(len(data)) for y in range(len(data[0])) if data[x][y] == "*"]
    ratios = []
    
    for star in stars:
        x, y = star
        borders = [data[i] for i in [x-1, x+1] if in_grid(i)]
        adjacent_numbers = []

        for line in borders:
            for match in re.finditer("\d+", line):
                start,end = match.start(), match.end()
                if y in range(start - 1, end + 1):
                    adjacent_numbers.append(int(line[start:end]))

        for match in re.finditer("\d+", data[x]):
            start,end = match.start(), match.end()
            if y == start - 1 or y == end:
                adjacent_numbers.append(int(data[x][start:end]))

        print(adjacent_numbers)
        if len(adjacent_numbers) == 2:
            ratios.append(adjacent_numbers[0] * adjacent_numbers[1])
    
    return ratios


if __name__ == "__main__":
    data = open("input.txt").read().split("\n")
    print(sum([sum(scan_line(data, x)) for x in range(len(data))]))
    print(sum(gear_ratios(data)))


class AdventTest(unittest.TestCase):

    def setUp(self):
        self.file = open("test_input.txt")
        self.data = self.file.read().split("\n")


    def tearDown(self):
        self.file.close()


    def test_scan_line(self):
        lines = self.data[0:3]
        self.assertEqual(scan_line(self.data, 0), [467])
        self.assertEqual(scan_line(self.data, 2), [35, 633])
        self.assertEqual(scan_line(self.data, 9), [664, 598])