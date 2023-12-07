cards = [str(i) for i in range(2, 10)] + ["T", "J", "Q", "K", "A"]


def main():
    with open("input.txt", "r") as f:
        games = f.readlines()
        games = [line.strip() for line in games]
        games = [line.split(" ") for line in games]

    print(games)
    part1(games)


def type_hand(hand):
    if len(set(hand)) == 1:
        return "Flush"
    elif len(set(hand)) == 2:
        return "Four of a kind" if hand.count(hand[0]) == 4 or hand.count(hand[1]) == 4 else "Full house"
    elif len(set(hand)) == 3:
        return "Three of a kind" if hand.count(hand[0]) == 3 or hand.count(hand[1]) == 3 or hand.count(
            hand[2]) == 3 else "Two pairs"
    elif len(set(hand)) == 4:
        return "One pair"
    else:
        return "High card"


def part1(games):
    result = 0

    dict_games = dict()
    dict_games["High card"] = []
    dict_games["One pair"] = []
    dict_games["Two pairs"] = []
    dict_games["Three of a kind"] = []
    dict_games["Full house"] = []
    dict_games["Four of a kind"] = []
    dict_games["Flush"] = []

    for game in games:
        dict_games[type_hand(game[0])] += [game]

    rank = 0

    for key in dict_games.keys():
        # if 2 cards have same value, sort by order cards list, if the first card is the same, sort by second card, etc...
        # dict_games[key] = [(cards, bid), (cards, bid), (cards, bid), (cards, bid), (cards, bid)] where cards is 5 cards
        print(key + ": " + str(dict_games[key]))
        dict_games[key] = sorted(dict_games[key], key=lambda x: (
            cards.index(x[0][0]), cards.index(x[0][1]), cards.index(x[0][2]), cards.index(x[0][3]),
            cards.index(x[0][4])))
        print(dict_games[key])
        for i in range(len(dict_games[key])):
            rank += 1
            result += rank * int(dict_games[key][i][1])

    print("Part1: " + str(result))


def part2(games):
    pass


if __name__ == "__main__":
    main()
