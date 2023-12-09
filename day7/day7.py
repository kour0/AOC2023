cards = [str(i) for i in range(2, 10)] + ["T", "J", "Q", "K", "A"]


def main():
    with open("input.txt", "r") as f:
        games = f.readlines()
        games = [line.strip() for line in games]
        games = [line.split(" ") for line in games]

    part1(games)
    part2(games)


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
        # sort the differnts hands by the cards, the egalities are sorted by the rank of the hand
        dict_games[key] = sorted(dict_games[key], key=lambda x: (
            cards.index(x[0][0]), cards.index(x[0][1]), cards.index(x[0][2]), cards.index(x[0][3]),
            cards.index(x[0][4])))
        for i in range(len(dict_games[key])):
            rank += 1
            result += rank * int(dict_games[key][i][1])

    print("Part1: " + str(result))


def change_joker_bis(hand):
    typ_han = type_hand(hand)

    if typ_han == "Flush":
        return hand.replace("J", "A")
    elif typ_han == "Four of a kind":
        # replace the joker by the card that is in the hand 4 times
        return hand.replace("J", hand[hand.index("J") - 1])
    elif typ_han == "Full house":
        # replace the joker by the card that is in the hand 3 times
        for card in hand:
            if hand.count(card) == 3 and card != "J":
                return hand.replace("J", card)
            elif hand.count(card) == 2 and card != "J":
                return hand.replace("J", card)
    elif typ_han == "Three of a kind":
        # replace the joker by the card that is in the hand 3 times
        for card in hand:
            if hand.count(card) == 3 and card != "J":
                return hand.replace("J", card)
        return hand.replace("J", "A")
    elif typ_han == "Two pairs":
        # replace the joker by the best card that is in the hand 2 times
        best_card = ""
        for card in hand:
            if hand.count(card) == 2 and card != "J":
                best_card += card
        return hand.replace("J", max(best_card, key=lambda x: cards.index(x)))
    elif typ_han == "One pair":
        # replace the joker by the card that is in the hand 2 times
        for card in hand:
            if hand.count(card) == 2 and card != "J":
                return hand.replace("J", card)
        return hand.replace("J", "A")
    else:
        # replace the joker by the best card
        return hand.replace("J", "A")


def change_joker(hand):
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
    if max_occ != 0:
        return hand.replace("J", max_card)
    else:
        return hand.replace("J", "A")


def part2(games):
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
        if "J" in game[0]:
            new_game = change_joker(game[0])
            dict_games[type_hand(new_game)] += [[new_game, game[1]]]
        else:
            dict_games[type_hand(game[0])] += [game]

    rank = 0

    for key in dict_games.keys():
        dict_games[key] = sorted(dict_games[key], key=lambda x: (
            cards.index(x[0][0]), cards.index(x[0][1]), cards.index(x[0][2]), cards.index(x[0][3]),
            cards.index(x[0][4])))
        print(key + " : " + str(dict_games[key]))
        for i in range(len(dict_games[key])):
            rank += 1
            result += rank * int(dict_games[key][i][1])

    print("Part2: " + str(result))


if __name__ == "__main__":
    main()
