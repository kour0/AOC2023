cards1 = [str(i) for i in range(2, 10)] + ["T", "J", "Q", "K", "A"]
cards2 = ["J"] + [str(i) for i in range(2, 10)] + ["T", "Q", "K", "A"]


def main():
    with open("input.txt", "r") as f:
        games = f.readlines()
        games = [line.strip() for line in games]
        games = [line.split(" ") for line in games]

    part1_2(games, 1)
    part1_2(games, 2)


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


def part1_2(games, part=1):
    result = 0

    dict_games = dict()
    dict_games["High card"] = []
    dict_games["One pair"] = []
    dict_games["Two pairs"] = []
    dict_games["Three of a kind"] = []
    dict_games["Full house"] = []
    dict_games["Four of a kind"] = []
    dict_games["Flush"] = []

    if part == 1:
        cards = cards1
    else:
        cards = cards2

    for game in games:
        if part == 2:
            J_game = change_joker(game[0], cards)
            dict_games[type_hand(J_game)] += [game]
        else:
            dict_games[type_hand(game[0])] += [game]

    rank = 0

    for key in dict_games.keys():
        dict_games[key].sort(key=lambda x: (
            cards.index(x[0][0]), cards.index(x[0][1]), cards.index(x[0][2]), cards.index(x[0][3]),
            cards.index(x[0][4])))
        for i in range(len(dict_games[key])):
            rank += 1
            result += rank * int(dict_games[key][i][1])

    print("Part" + str(part) + ": " + str(result))


def change_joker(hand, cards):
    ensemble = set(hand)
    max_occ = 0
    max_card = ""
    for card in ensemble:
        if card != "J":
            if max_occ == hand.count(card):
                max_card = max(max_card, card, key=lambda x: cards.index(x))
            elif hand.count(card) > max_occ:
                max_occ = hand.count(card)
                max_card = card
    if max_occ == 0:
        return hand.replace("J", "A")
    return hand.replace("J", max_card)


if __name__ == "__main__":
    main()
