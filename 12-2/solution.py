import functools


bag_contents = {"red": 12, "green": 13, "blue": 14,}


# For both part 1 and part 2, retrieves maximum number of cubes required of each color for all moves,
# with 'game' as a string of input data containing the moves in the game
def max_by_color(game: str):
    game_id, moves = game.split(": ")
    game_id = int(game_id.split(" ")[-1])
    moves = moves.split("; ")
    cleaned_moves = {k:0 for k in bag_contents.keys()}

    for move in moves:
        for piece in move.split(", "):
            n, color = piece.split(" ")
            cleaned_moves[color] = max(cleaned_moves[color], int(n))
    return (game_id, cleaned_moves)


# Given a game, i.e. a set of moves, retrieves max number of cubes required of each color
# for all moves, checking that against the global contents of the bag.
def is_possible(moves: dict) -> bool:
    for color, amt in bag_contents.items():
        if color in moves and moves[color] > amt:
            return False
    return True


def solve_one(data: list[str]) -> int:
    def check_possible(game):
        game_id, moves = max_by_color(game)
        return game_id if is_possible(moves) else 0

    return sum([check_possible(game) for game in data])


def solve_two(data: list[str]) -> int:
    def get_power(game):
        game_id, moves = max_by_color(game)
        return functools.reduce(lambda a, b: a*b, moves.values())

    return sum([get_power(game) for game in data])


if __name__ == "__main__":
    data = open("input.txt").read().split("\n")
    print(solve_one(data))
    print(solve_two(data))