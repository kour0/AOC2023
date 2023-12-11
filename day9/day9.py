def main():
    with open("input.txt", "r") as f:
        datasets = f.readlines()
        datasets = [line.strip().split(" ") for line in datasets]
        datasets = [[int(y) for y in x] for x in datasets]

    part1(datasets)
    part2(datasets)


def construct_history(dataset):
    history = [dataset]
    while len(history[-1]) != history[-1].count(0):
        history.append([history[-1][i + 1] - history[-1][i] for i in range(len(history[-1]) - 1)])
    return history


def part1(datasets):
    result = 0
    for dataset in datasets:
        history = construct_history(dataset)
        for values in history:
            result += values[-1]
    print("Part1: " + str(result))


def part2(datasets):
    result = 0
    for dataset in datasets:
        history = construct_history(dataset)
        history.reverse()
        value_history = 0
        for values in history:
            value_history = values[0] - value_history
            print(value_history)
        result += value_history
    print("Part2: " + str(result))


if __name__ == "__main__":
    main()
