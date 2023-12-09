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

    part1(nodes, instrs)
    part2(nodes, instrs)


def part1(nodes, instrs):
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


def part2(nodes, instr):
    pass


if __name__ == "__main__":
    main()
