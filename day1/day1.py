def main():
    # On veut lire le fichier input.txt
    # On veut lire chaque ligne du fichier
    with open("input.txt", "r") as f:
        lines = f.readlines()

    print(lines)

    # On veut enlever les \n
    lines = [line.strip() for line in lines]

    part1(lines)
    part2(lines)


def part1(strings):
    result = 0

    for line in strings:
        result += int(firstdigit(line) + firstdigit(line[::-1]))

    print(result)


def firstdigit(string):
    for char in string:
        if char.isdigit():
            return char


def part2(strings):
    result = 0

    for line in strings:
        lowerdigit, upperdigit = fstandlastdigit(line)
        result += int(lowerdigit + upperdigit)

    print(result)


def fstandlastdigit(string):
    strdigits = [("one", "1"), ("two", "2"), ("three", "3"), ("four", "4"), ("five", "5"),
                 ("six", "6"), ("seven", "7"), ("eight", "8"), ("nine", "9")]

    intdigits = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    lowerpos = len(string)
    upperpos = -1
    lowerdigit = "0"
    upperdigit = "0"

    for digit in strdigits:
        strdigit = digit[0]
        if strdigit in string:
            if lowerpos != min(string.find(strdigit), lowerpos):
                lowerpos = min(string.find(strdigit), lowerpos)
                lowerdigit = digit[1]
            if upperpos != max(string.rfind(strdigit), upperpos):
                upperpos = max(string.rfind(strdigit), upperpos)
                upperdigit = digit[1]

    for digit in intdigits:
        intdigit = str(digit)
        if intdigit in string:
            if lowerpos != min(string.find(intdigit), lowerpos):
                lowerpos = min(string.find(intdigit), lowerpos)
                lowerdigit = str(intdigit)
            if upperpos != max(string.rfind(intdigit), upperpos):
                upperpos = max(string.rfind(intdigit), upperpos)
                upperdigit = str(intdigit)

    print(lowerdigit, upperdigit)

    return lowerdigit, upperdigit


if __name__ == "__main__":
    main()
