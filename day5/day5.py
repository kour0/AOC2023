def main():
    with open("input.txt", "r") as f:
        seeds = f.readline()
        seeds = seeds.strip()
        seeds = seeds.split(": ")[1]
        seeds = seeds.split(" ")
        lines = f.readlines()
        ranges = dict()
        ranges['1'] = []
        ranges['2'] = []
        ranges['3'] = []
        ranges['4'] = []
        ranges['5'] = []
        ranges['6'] = []
        ranges['7'] = []
        k_ranges = 1
        for i in range(len(lines)):
            if lines[i].strip()[0].isdigit():
                numbers = lines[i].strip().split(" ")
                ranges[str(k_ranges)].append(
                    (range(int(numbers[0]) - int(numbers[2]), int(numbers[0]) + int(numbers[2]) + 1),
                     range(int(numbers[1]) - int(numbers[2]), int(numbers[1]) + int(numbers[2]) + 1)))
            elif lines[i].strip() != "":
                k_ranges += 1

    part1(games)
    part2(games)


def part1(games):
    pass


def part2(games):
    pass


if __name__ == "__main__":
    main()
