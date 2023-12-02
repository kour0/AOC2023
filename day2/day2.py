def main():
    # On veut lire le fichier input.txt
    # On veut lire chaque ligne du fichier
    with open("input.txt", "r") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        lines = [line[line.index(": ") + 2:] for line in lines]
        lines = [line.split("; ") for line in lines]
        lines = [[y.split(", ") for y in x] for x in lines]
        lines = [[[z.split(" ") for z in y] for y in x] for x in lines]

    part1(lines)


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
            result += i+1

    print("Part1: " + str(result))


if __name__ == "__main__":
    main()
