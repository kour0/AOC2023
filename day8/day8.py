import math


def main():
    with open("input.txt", "r") as f:
        instrs = f.readline()
        instrs = instrs.strip()
        instrs = instrs.replace("L", "0").replace("R", "1")
        instrs = [int(i) for i in instrs]
        f.readline()
        lines = f.readlines()
        nodes = {}
        for node in [line.split(" = ") for line in lines]:
            nodes[node[0]] = node[1].strip().replace("(", "").replace(")", "").replace(",", "").split(" ")

    part1(instrs, nodes)
    part2(instrs, nodes)


def part1(instrs, nodes):
    start_point = "AAA"
    end_point = "ZZZ"
    steps = 0
    while start_point != end_point:
        for instr in instrs:
            steps += 1
            start_point = nodes[start_point][instr]
            if start_point == end_point:
                break
    print("Part1: {}".format(steps))


def part2(instrs, nodes):
    start_point = [node for node in nodes if node[2] == "A"]
    steps_number = 0
    steps_point = [0 for i in range(len(start_point))]
    while len(list(start_point)) != len([steps for steps in steps_point if steps != 0]):
        for instr in instrs:
            steps_number += 1
            for i in range(len(start_point)):
                start_point[i] = nodes[start_point[i]][instr]
                if start_point[i][2] == "Z":
                    steps_point[i] = steps_number
            if len(start_point) == len([steps for steps in steps_point if steps != 0]):
                break
    print("Part2: {}".format(math.lcm(*steps_point)))


if __name__ == "__main__":
    main()
