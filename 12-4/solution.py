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
    base_matches = get_matches(cards)
    matches_with_copies = {card_id: 1 for card_id in base_matches.keys()}

    for card in range(1, len(cards) + 1):
        matches = base_matches[card]
        copies = matches_with_copies[card]
        for m in range(1, matches + 1):
            matches_with_copies[card + m] += copies
    
    return sum(matches_with_copies.values())


if __name__ == "__main__":
    data = open("input.txt").read().split("\n")
    print(solve_one(data))
    print(solve_two(data))