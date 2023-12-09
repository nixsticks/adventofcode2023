def extrapolate_sequence(sequence):
    differences = [sequence]

    while len(set(differences[-1])) > 1:
        current_diff, next_diff = differences[-1], []
        for i in range(1, len(current_diff)):
            next_diff.append(current_diff[i]-current_diff[i-1])
        differences.append(next_diff)

    for i in range(len(differences)-2, -1, -1):
        differences[i].append(differences[i][-1] + differences[i+1][-1])

    return differences[0][-1]


def form_pyramid(sequence: list[int]) -> list[list[int]]:
    differences = [sequence]

    while len(set(differences[0])) > 1:
        current_diff, next_diff = differences[0], []
        for i in range(1, len(current_diff)):
            next_diff.append(current_diff[i]-current_diff[i-1])
        differences.insert(0, next_diff)

    return differences


def extrapolate_forward(sequences: list[list[int]]) -> list[list[int]]:
    for i in range(1, len(sequences)):
        sequences[i].append(sequences[i][-1] + sequences[i-1][-1])
    return sequences


def extrapolate_backward(sequences: list[list[int]]) -> list[list[int]]:
    for i in range(1, len(sequences)):
        sequences[i].insert(0, sequences[i][0] - sequences[i-1][0])
    return sequences


if __name__ == "__main__":
    data = [[int(i) for i in line.split(" ")] for line in open("input.txt").read().split("\n")]
    seqs = [form_pyramid(seq) for seq in data]
    forwards, backwards = [extrapolate_forward(seq) for seq in seqs], [extrapolate_backward(seq) for seq in seqs]
    print(sum([seq[-1][-1] for seq in forwards]))
    print(sum([seq[-1][0] for seq in backwards]))