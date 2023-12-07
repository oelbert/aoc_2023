def card_wins(card: str) -> int:
    nwins = 0
    vals = card.split(": ")[1]
    winners = vals.split("|")[0].split()
    plays = vals.split("|")[1].split()
    for play in plays:
        if play in winners:
            nwins += 1
    return nwins


def run_day4(file: str) -> int:
    data = open(file, "r")
    cards = data.readlines()
    card_numbers = [1] * len(cards)
    tot_points = 0
    for i, item in enumerate(cards):
        card = item.split("\n")[0]
        nwins = card_wins(card)
        tot_points += int(2**(nwins-1))
        for j in range(1, nwins+1):
            card_numbers[i+j] += card_numbers[i]
    return tot_points, sum(card_numbers)


def main():
    print(run_day4('../data/day4.txt'))


if __name__ == '__main__':
    main()
