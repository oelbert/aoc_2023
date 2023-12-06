max_bag = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def reduce_game(game: str):
    noline = game.split("\n")[0]
    idstr, game_data = noline.split(": ")
    reveals = game_data.split("; ")
    game_id = int(idstr[5:])
    return game_id, reveals


def cube_power(cubes: dict) -> int:
    pow = 1
    for key in cubes.keys():
        pow *= cubes[key]
    return pow


def min_cubes(reveals: str):
    mins = {
        "green": 0,
        "red": 0,
        "blue": 0,
    }
    is_possible = True
    for reveal in reveals:
        color_pull = reveal.split(", ")
        for color in color_pull:
            num, name = color.split(" ")
            if int(num) > mins[name]:
                mins[name] = int(num)
            if int(num) > max_bag[name]:
                is_possible = False
    pow = cube_power(mins)
    return is_possible, pow


def run_day2(file: str) -> int:
    data = open(file, "r")
    games = data.readlines()
    id_sum = 0
    pow_sum = 0
    for game in games:
        game_id, reveals = reduce_game(game)
        is_possible, pow = min_cubes(reveals)
        pow_sum += pow
        if is_possible:
            id_sum += game_id
    return id_sum, pow_sum


def main():
    print(run_day2('../data/day2.txt'))


if __name__ == '__main__':
    main()
