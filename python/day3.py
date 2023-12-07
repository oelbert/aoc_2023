from collections import defaultdict

not_symbol = [".", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "\n"]


def run_day3(file: str):
    data = open(file, "r")
    lines = data.readlines()
    part_sums = 0
    num = ""
    savenum = False
    star_index = None
    maybe_gears = defaultdict(list)
    ratio_sum = 0
    for j, line in enumerate(lines):
        l = line.split()[0]
        for i, char in enumerate(l):
            if char.isnumeric():
                num += char
                for jj in [-1, 0, 1]:
                    for ii in [-1, 0, 1]:
                        if (j+jj >= 0) and (i+ii) >= 0:
                            try:
                                if not (lines[j+jj][i+ii] in not_symbol):
                                    savenum = True
                                    if lines[j+jj][i+ii] == "*":
                                        star_index = (j+jj, i+ii)
                            except IndexError:
                                continue
                if (i+1 < len(l)):
                    if l[i+1].isnumeric():
                        continue
                if savenum is True:
                    part_sums += int(num)
                    savenum = False
                    if star_index is not None:
                        maybe_gears[star_index].append(int(num))
                num = ""
                star_index = None
    for index in maybe_gears:
        if len(maybe_gears[index]) == 2:
            grat = maybe_gears[index][0] * maybe_gears[index][1]
            ratio_sum += grat
    return part_sums, ratio_sum


def main():
    print(run_day3('../data/day3.txt'))


if __name__ == '__main__':
    main()
