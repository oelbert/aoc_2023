import argparse
import numpy as np


def solve_pattern(pat):
    pattern = pat.split('\n')
    pp = []
    for line in pattern:
        lbuf = []
        for val in line:
            if val == '#':
                lbuf.append(1)
            else:
                lbuf.append(0)
        pp.append(lbuf)
    terrain = np.array(pp)
    for i in range(1, terrain.shape[0]):
        size = min([i, terrain.shape[0]-i])
        check = np.array_equal(terrain[i-size:i, :], np.flip(terrain[i:i+size, :], 0))
        if check:
            return 100*(i)
    for j in range(1, terrain.shape[1]):
        size = min([j, terrain.shape[1]-j])
        check2 = np.array_equal(terrain[:, j-size:j], np.flip(terrain[:, j:j+size], 1))
        if check2:
            return j


def solve_pattern2(pat):
    pattern = pat.split('\n')
    pp = []
    for line in pattern:
        lbuf = []
        for val in line:
            if val == '#':
                lbuf.append(1)
            else:
                lbuf.append(0)
        pp.append(lbuf)
    terrain = np.array(pp)
    for i in range(1, terrain.shape[0]):
        size = min([i, terrain.shape[0]-i])
        check = terrain[i-size:i, :] == np.flip(terrain[i:i+size, :], 0)
        if check.sum() == check.size - 1:
            return 100*(i)
    for j in range(1, terrain.shape[1]):
        size = min([j, terrain.shape[1]-j])
        check2 = terrain[:, j-size:j] == np.flip(terrain[:, j:j+size], 1)
        if check2.sum() == check2.size - 1:
            return j


def main(file):
    with open(file) as f:
        data = f.read()
    patterns = data.split("\n\n")
    accumulator = 0
    for pattern in patterns:
        accumulator += solve_pattern(pattern)
    print(accumulator)
    accumulator2 = 0
    for pattern in patterns:
        accumulator2 += solve_pattern2(pattern)
    print(accumulator2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="day 13 of Advent of Code")
    parser.add_argument("datafile", help='text file of data')
    args = parser.parse_args()
    main(args.datafile)