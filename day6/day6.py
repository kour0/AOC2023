def main():
    with open("input.txt", "r") as f:
        time = f.readline()
        time = time.strip()
        time = time.split(": ")[1].split()
        time = [int(x) for x in time]
        distance = f.readline()
        distance = distance.strip()
        distance = distance.split(": ")[1].split()
        distance = [int(x) for x in distance]

    part1(time, distance)

    time = str(time).replace("[", "").replace("]", "").replace(",", "").replace(" ", "")
    distance = str(distance).replace("[", "").replace("]", "").replace(",", "").replace(" ", "")
    time = int(time)
    distance = int(distance)

    part2(time, distance)


def valid_solution(time, distance):
    k = 0
    for i in range(time):
        vitesse = i
        time_restant = time - i
        if vitesse * time_restant > distance:
            k += 1
    return k


def part1(time, distance):
    result = 1

    for i in range(len(time)):
        numbersol = valid_solution(time[i], distance[i])
        result *= numbersol

    print("Part1: " + str(result))


def part2(time, distance):
    result = valid_solution(time, distance)

    print("Part2: " + str(result))


if __name__ == "__main__":
    main()
