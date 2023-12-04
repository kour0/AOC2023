def main():
    with open("input.txt", "r") as f:
        games = f.readlines()
        games = [line.strip() for line in games]
        games = [line[line.index(": ") + 2:] for line in games]
        games = [line.split(" | ") for line in games]
        games = [[y.split(" ") for y in x] for x in games]

    part1(games)
    part2(games)


def part1(games):
    result = 0

    for game in games:
        score = -1
        for tirage in game[1]:
            if tirage.isdigit() and tirage in game[0]:
                score += 1
        if score >= 0:
            result += 2 ** score

    print("Part1: "+str(result))


def part2(games):
    list_occ = [1 for i in range(len(games))]
    list_score = [0 for i in range(len(games))]
    i = 0

    for game in games:
        score = -1
        result = 0
        for tirage in game[1]:
            if tirage.isdigit() and tirage in game[0]:
                score += 1
        if score >= 0:
            for j in range(score+1):
                list_occ[i + j + 1] += list_occ[i]
        i += 1

    print("Part2: "+str(sum(list_occ)))


if __name__ == "__main__":
    main()
