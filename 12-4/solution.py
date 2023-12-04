from collections import deque


def get_matches(cards: list[str]):
    card_matches = {}

    for card in cards:
        card_id, numbers = card.split(": ")
        winning_numbers, your_numbers = [set([int(n) for n in side.split()]) for side in numbers.split(" | ")]
        overlaps = winning_numbers.intersection(your_numbers)
        card_matches[int(card_id.split(" ")[-1])] = len(overlaps)

    return card_matches


def solve_one(cards: list[str]):
    return sum([pow(2, (m-1)) for m in get_matches(cards).values() if m > 0])


def solve_two(cards: list[str]):
    card_matches = get_matches(cards)
    scratchcards = 0
    queue = deque(card_matches.keys())

    while len(queue) > 0:
        card = queue.popleft()
        scratchcards += 1
        matches = card_matches[card]
        for m in range(1, matches + 1):
            queue.append(card + m)

    return scratchcards


if __name__ == "__main__":
    data = open("input.txt").read().split("\n")
    print(solve_one(data))
    print(solve_two(data))
