import time
from math import inf


def main():
    with open("input.txt", "r") as f:
        games = f.readlines()
        seed = games[0].strip().split(": ")[1]
        seed = [int(i) for i in seed.split(" ")]
        maps = dict()
        k_map = -1
        for i in range(1, len(games)):
            if games[i].strip() == "":
                continue
            if games[i].strip()[0].isdigit():
                maps[str(k_map)] += [games[i].strip().split(" ")]
            elif games[i].strip() != "":
                k_map += 1
                maps[str(k_map)] = []

    print("Seed: ", seed)
    print("Maps: ", maps)
    print("K_maps: ", k_map)

    part1(maps, seed, k_map)
    part2(maps, seed, k_map)


def inmap(maps, k, number):
    k = str(k)
    for i in range(len(maps[k])):
        min_source = int(maps[k][i][1])
        max_source = int(maps[k][i][1]) + int(maps[k][i][2]) - 1
        if min_source <= int(number) <= max_source:
            number += int(maps[k][i][0]) - int(maps[k][i][1])
    return number


def position(maps, k, number):
    for i in range(k + 1):
        number = inmap(maps, i, number)
    return number


def part1(maps, seed, k_map):
    lower_destination = inf
    for number in seed:
        number = position(maps, k_map, number)
        lower_destination = min(lower_destination, number)
    print("Part 1: ", lower_destination)


def min_range(maps, k, min, max):
    k = str(k)
    for i in range(len(maps[k])):
        min_source = int(maps[k][i][1])
        max_source = int(maps[k][i][1]) + int(maps[k][i][2]) - 1
        delta = int(maps[k][i][0]) - int(maps[k][i][1])
        if min_source <= min <= max_source and min_source <= max <= max_source:
            return [(min + delta, max + delta)]
        elif min_source <= min <= max_source < max:
            return [(min + delta, max_source + delta)] + min_range(maps, k, max_source + 1, max)
        elif max_source >= max >= min_source > min:
            return min_range(maps, k, min, min_source - 1) + [(min_source + delta, max + delta)]
    return [(min, max)]


def part2(maps, seed, k_map):
    time_start = time.time()
    lower_destination = inf
    list_interval = [(seed[i], seed[i] + seed[i+1] - 1) for i in range(0, len(seed), 2)]
    dict_list_interval = dict()
    dict_list_interval["-1"] = list_interval
    for k in range(k_map + 1):
        dict_list_interval[str(k)] = []
        for interval in dict_list_interval[str(k-1)]:
            dict_list_interval[str(k)] += min_range(maps, k, interval[0], interval[1])
        if k == k_map:
            lower_destination = min(dict_list_interval[str(k)])[0]
    print("Time: ", time.time() - time_start)
    print("Part 2: ", lower_destination)


if __name__ == "__main__":
    main()
