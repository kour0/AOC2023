def main():
    # On veut lire le fichier input.txt
    # On veut lire chaque ligne du fichier
    with open("input.txt", "r") as f:
        games = f.readlines()
        games = [line.strip() for line in games]
        games = [line[line.index(": ") + 2:] for line in games]
        games = [line.split("; ") for line in games]
        games = [[y.split(", ") for y in x] for x in games]
        games = [[[z.split(" ") for z in y] for y in x] for x in games]

    part1(games)
    part2(games)


def part1(games):
    redcubes = 12
    greencubes = 13
    bluecubes = 14

    result = 0

    for i in range(len(games)):
        valid = True
        for sets in games[i]:
            for cube in sets:
                if cube[1] == "red" and int(cube[0]) > redcubes:
                    valid = False
                    break
                if cube[1] == "blue" and int(cube[0]) > bluecubes:
                    valid = False
                    break
                if cube[1] == "green" and int(cube[0]) > greencubes:
                    valid = False
                    break
            if not valid:
                break
        if valid:
            result += i + 1

    print("Part1: " + str(result))


def part2(games):

    result = 0

    for i in range(len(games)):
        redcubes = 0
        greencubes = 0
        bluecubes = 0
        for sets in games[i]:
            for cube in sets:
                if cube[1] == "red" and redcubes != max(int(cube[0]), redcubes):
                    redcubes = max(int(cube[0]), redcubes)
                if cube[1] == "blue" and bluecubes != max(int(cube[0]), bluecubes):
                    bluecubes = max(int(cube[0]), bluecubes)
                if cube[1] == "green" and greencubes != max(int(cube[0]), greencubes):
                    greencubes = max(int(cube[0]), greencubes)
        result += redcubes * greencubes * bluecubes

    print("Part2: " + str(result))


if __name__ == "__main__":
    main()
