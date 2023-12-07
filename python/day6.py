def num_ways_to_win(time, dist):
    speed = 0
    winners = 0
    while time > 0:
        distance = speed * time
        if distance > dist:
            winners += 1
        time -= 1
        speed += 1
    return winners


def run_day6(times, distances):
    winning_combos = 1
    for i in range(len(times)):
        winning_combos *= num_ways_to_win(times[i], distances[i])
    return winning_combos


def main():
    data = open("../data/day6.txt", "r")
    times = list(map(int, data.readline().split()[1:]))
    distances = list(map(int, data.readline().split()[1:]))
    print(run_day6(times, distances))
    newtimes = [int("".join(list(map(str, times))))]
    newdists = [int("".join(list(map(str, distances))))]
    print(run_day6(newtimes, newdists))


if __name__ == "__main__":
    main()