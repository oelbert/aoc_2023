import argparse


def extrapolate_variable(history: list[int]):
    if len(set(history)) == 1:
        return history[-1]
    else:
        delta = [history[i] - history[i-1] for i in range(1, len(history))]
        return history[-1] + extrapolate_variable(delta)


def extrapolate_variable_backwards(history: list[int]):
    if len(set(history)) == 1:
        return history[0]
    else:
        delta = [history[i] - history[i-1] for i in range(1, len(history))]
        return history[0] - extrapolate_variable_backwards(delta)


def main(datafile: str):
    data = open(datafile, "r")
    variables = data.readlines()
    extrap_sums = 0
    extrap_back = 0
    for var in variables:
        hist = list(map(int, var.strip().split()))
        nextval = extrapolate_variable(hist)
        firstval = extrapolate_variable_backwards(hist)
        extrap_sums += nextval
        extrap_back += firstval
    print(extrap_sums, extrap_back)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="day 9 of Advent of Code")
    parser.add_argument("datafile", help='text file of data')
    args = parser.parse_args()
    main(args.datafile)
