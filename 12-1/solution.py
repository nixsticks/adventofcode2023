import re, unittest


valid_digits = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

pattern = "(\d|{})".format("|".join(valid_digits.keys()))


def get_calibration_value(data: str) -> int:    
    matches = [re.search(pattern, data).group(0), re.search(".*{}".format(pattern), data).group(1)]
    clean_matches = [match if re.match("\d", match) else valid_digits[match] for match in matches]
    return int(clean_matches[0] + clean_matches[-1])


def solve(data: list[str]) -> int:
    digits = [get_calibration_value(line) for line in data]
    return sum(digits)


if __name__ == "__main__":
    data = open("input.txt").read().split("\n")
    print(solve(data))


class AdventTest(unittest.TestCase):

    def setUp(self):
        self.file = open("test_input.txt")
        self.data = self.file.read().split("\n")

    def tearDown(self):
        self.file.close()

    def test_calibration_value(self):
        self.assertEqual(get_calibration_value("ninesevensrzxkzpmgz8kcjxsbdftwoner"), 91)
        self.assertEqual(get_calibration_value("onedtrbdcdseven6twosvlhbdfive9"), 19)

    def test(self):
        self.assertEqual(solve(self.data), 281)