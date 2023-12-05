def main():
    # On veut lire le fichier input.txt
    # On veut lire chaque ligne du fichier
    with open("input.txt", "r") as f:
        lines = f.readlines()

    # On veut enlever les \n
    lines = [line.strip() for line in lines]

    part1(lines)
    part2(lines)


def aroundsymbol(x, y, grid, height, width):
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if (i, j) != (x, y):
                if 0 <= i < height and 0 <= j < width and not (grid[i][j].isdigit() or grid[i][j] == "."):
                    return True
    return False


def part1(lines):
    result = 0
    x = 0
    y = 0
    height = len(lines)
    width = len(lines[x])

    while x < len(lines):
        while y < len(lines[x]):
            if lines[x][y].isdigit():
                mots = 0
                ispartnumber = False
                while 0 <= y < width and lines[x][y].isdigit():
                    ispartnumber = aroundsymbol(x, y, lines, height, width) or ispartnumber
                    mots += 1
                    y += 1
                if ispartnumber:
                    result += int(lines[x][y - mots:y])
            y += 1
        x += 1
        y = 0

    print("Part1: " + str(result))


def aroundmultiple(x, y, grid, height, width):
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if (i, j) != (x, y):
                if 0 <= i < height and 0 <= j < width and grid[i][j] == "*":
                    return True, (i, j)
    return False, (-1, -1)


def part2(lines):
    result = 0
    x = 0
    y = 0
    height = len(lines)
    width = len(lines[x])
    digits = []

    while x < len(lines):
        while y < len(lines[x]):
            if lines[x][y].isdigit():
                mots = 0
                isaroundmultiple, pos = False, (-1, -1)
                while 0 <= y < width and lines[x][y].isdigit():
                    researchmultiple = aroundmultiple(x, y, lines, height, width)
                    if researchmultiple[0]:
                        if researchmultiple[1] != pos and pos != (-1, -1):
                            print("WARNING: multiple around multiple")
                        isaroundmultiple, pos = researchmultiple
                    mots += 1
                    y += 1
                if isaroundmultiple:
                    digits.append((lines[x][y - mots:y], pos))
            y += 1
        x += 1
        y = 0

    for i in range(len(digits)):
        for j in range(i + 1, len(digits)):
            if digits[i][1] == digits[j][1]:
                result += int(digits[i][0]) * int(digits[j][0])

    print("Part2: " + str(result))


if __name__ == "__main__":
    main()
