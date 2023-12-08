card_values = {
    "A": "c",
    "K": "b",
    "Q": "a",
    "J": "9",
    "T": "8",
    "9": "7",
    "8": "6",
    "7": "5",
    "6": "4",
    "5": "3",
    "4": "2",
    "3": "1",
    "2": "0"
}

card_values2 = {
    "A": "c",
    "K": "b",
    "Q": "a",
    "J": "0",
    "T": "9",
    "9": "8",
    "8": "7",
    "7": "6",
    "6": "5",
    "5": "4",
    "4": "3",
    "3": "2",
    "2": "1"
}


def parse_play(play):
    hand = play.split()[0]
    bid = int(play.split()[1])
    return (hand, bid)


def hand_value(hand):
    cardcounts = {}
    cardhex = " 0x"
    for i, card in enumerate(hand):
        if card in cardcounts.keys():
            cardcounts[card] += 1
        else:
            cardcounts[card] = 1
        cardhex += card_values[card]
    card_digits = float(int(cardhex, 16))*1e-7
    num_unique = len(cardcounts.keys())
    maxcards = max(list(cardcounts.values()))
    if num_unique <= 1:
        hand_value = 7.
    elif num_unique == 2:
        if maxcards == 4:
            hand_value = 6.
        else:
            hand_value = 5.
    elif num_unique == 3:
        if maxcards == 3:
            hand_value = 4.
        else:
            hand_value = 3.
    elif num_unique == 4:
        hand_value = 2.
    else:
        hand_value = 1.
    hand_value += card_digits
    return hand_value


def hand_value2(hand):
    cardcounts = {}
    cardhex = " 0x"
    for i, card in enumerate(hand):
        if card in cardcounts.keys():
            cardcounts[card] += 1
        else:
            cardcounts[card] = 1
        cardhex += card_values2[card]
    card_digits = float(int(cardhex, 16))*1e-7
    if "J" in cardcounts.keys():
        num_j = cardcounts.pop("J")
    else:
        num_j = 0
    num_unique = len(cardcounts.keys())
    try:
        maxcards = max(list(cardcounts.values()))
    except ValueError:
        maxcards = 0
    if num_j > 0:
        maxcards += num_j
    if num_unique <= 1:
        hand_value = 7.
    elif num_unique == 2:
        if maxcards == 4:
            hand_value = 6.
        elif maxcards == 3:
            hand_value = 5.
        else:
            raise ValueError(f"{num_unique} uniques, {maxcards} max cards")
    elif num_unique == 3:
        if maxcards == 3:
            hand_value = 4.
        elif maxcards == 2:
            hand_value = 3.
        else:
            raise ValueError(f"{num_unique} uniques, {maxcards} max cards")
    elif num_unique == 4:
        hand_value = 2.
    elif num_unique == 5:
        hand_value = 1.
    else:
        raise ValueError(f"{num_unique} uniques?")
    hand_value += card_digits
    return hand_value


def sort_hands(hands, bids, part=1):
    '''
    sorts hands into ascending order
    '''
    ranked_hands = []
    ranked_bids = []
    hand_values = {}
    for i, hand in enumerate(hands):
        if part == 1:
            hand_values[hand] = hand_value(hand)
        elif part == 2:
            hand_values[hand] = hand_value2(hand)
        else:
            raise ValueError(f"Part must be 1 or 2, got {part}")
        if i == 0:
            ranked_hands.append(hand)
            ranked_bids.append(bids[i])
        else:
            for j in range(len(ranked_hands)):
                if hand_values[ranked_hands[j]] > hand_values[hand]:
                    ranked_hands.insert(j, hand)
                    ranked_bids.insert(j, bids[i])
                    break
                elif j == len(ranked_hands) - 1:
                    ranked_hands.append(hand)
                    ranked_bids.append(bids[i])
                else:
                    continue
    return ranked_hands, ranked_bids


def calc_winnings(ranked_bids):
    hand_wins = [(i+1) * ranked_bids[i] for i in range(len(ranked_bids))]
    return sum(hand_wins)


def run_day7(plays: str):
    hands, bids = zip(*map(parse_play, plays))
    ranked_hands, ranked_bids = sort_hands(hands, bids)
    winnings = calc_winnings(ranked_bids)
    ranked_hands2, ranked_bids2 = sort_hands(hands, bids, 2)
    winnings2 = calc_winnings(ranked_bids2)
    return winnings, winnings2


def main():
    data = open("../data/day7.txt", "r")
    plays = data.readlines()
    print(run_day7(plays))


if __name__ == "__main__":
    main()
