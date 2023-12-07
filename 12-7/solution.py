card_strength = [str(i) for i in range(2, 10)] + ["T","J","Q","K","A"]
card_strength_map = {c:i+1 for i, c in enumerate(card_strength)}
card_strength_jokers = ["J"] + [str(i) for i in range(2, 10)] + ["T","Q","K","A"]
card_strength_map_jokers = {c:i+1 for i, c in enumerate(card_strength_jokers)}


def hand_strength_by_type(hand: str) -> int:
    card_types = {}
    for c in hand:
        if c not in card_types:
            card_types[c] = 0
        card_types[c] += 1

    match len(card_types):
        case 1:
            return 7
        case 2:
            if 4 in card_types.values():
                return 6
            return 5
        case 3:
            if 3 in card_types.values():
                return 4
            return 3
        case 4:
            return 2
        case _:
            return 1


def compare_by_type(h1: str, h2: str) -> int:
    hs1, hs2 = hand_strength_by_type(h1), hand_strength_by_type(h2)
    if hs1 == hs2:
        return 0
    return -1 if hs1 < hs2 else 1


def compare_by_order(h1: str, h2: str, order_map: dict) -> int:
    for i, c1 in enumerate(h1):
        c2 = h2[i]
        if c1 == c2:
            continue
        return -1 if order_map[c1] < order_map[c2] else 1
    return 0


def compare(h1: str, h2: str) -> int:
    type_comparison = compare_by_type(h1, h2)
    return compare_by_order(h1, h2, card_strength_map) if not type_comparison else type_comparison


def compare_with_jokers(h1: str, h2: str) -> int:
    hj1, hj2 = transform_jokers(h1), transform_jokers(h2)
    type_comparison = compare_by_type(hj1, hj2)
    return compare_by_order(h1, h2, card_strength_map_jokers) if not type_comparison else type_comparison


def rank_hands(hands: list[str], compfunc) -> list[str]:
    import functools
    return sorted(hands, key=functools.cmp_to_key(compfunc))


def transform_jokers(hand: str) -> str:
    if "J" not in hand or hand == "JJJJJ":
        return hand

    card_types = {}
    for c in hand:
        if c not in card_types:
            card_types[c] = 0
        card_types[c] += 1

    highest_card, highest_value = None, 0
    for c,v in card_types.items():
        if c == "J":
            continue
        if v > highest_value:
            highest_card, highest_value = c, v

    return "".join([highest_card if c == "J" else c for c in hand])


def calculate_winnings(game_map: dict, ranked_hands: list[str]):
    return [game_map[hand] * (i+1) for i, hand in enumerate(ranked_hands)]



if __name__ == "__main__":
    game_map = {c[0]:int(c[1]) for c in [line.split(" ") for line in open("input.txt").read().split("\n")]}
    ranked_hands = rank_hands(game_map.keys(), compare)
    ranked_hands_with_jokers = rank_hands(game_map.keys(), compare_with_jokers)
    print(sum(calculate_winnings(game_map, ranked_hands)))
    print(sum(calculate_winnings(game_map, ranked_hands_with_jokers)))