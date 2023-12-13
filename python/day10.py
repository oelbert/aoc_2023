import argparse


LEFT = ['-', 'F', 'L']
RIGHT = ['-', '7', 'J']
UP = ['|', 'F', '7']
DOWN = ['|', 'L', 'J']


def parse_pipes(pipes):
    buffered_pipes = []
    for pipe in pipes:
        buffered_pipes.append(['.'] + list(pipe.strip()) + ['.'])
    vertical_pad = ['.'] * len(buffered_pipes[0])
    buffered_pipes.insert(0, vertical_pad)
    buffered_pipes.append(vertical_pad)
    return buffered_pipes


def findstart(pipes):
    for i in range(len(pipes)):
        for j in range(len(pipes[i])):
            if pipes[i][j] == "S":
                return i, j


def find_next(pipes, index):
    i = index[0]
    j = index[1]
    if pipes[i][j] == 'S':
        if (pipes[i][j+1] in RIGHT):
            pipes[i][j] = "X"
            return i, j+1
        elif (pipes[i][j-1] in LEFT):
            pipes[i][j] = "X"
            return i, j-1
        elif (pipes[i+1][j] in UP):
            pipes[i][j] = "X"
            return i+1, j
        elif (pipes[i-1][j] in DOWN):
            pipes[i][j] = "X"
            return i-1, j
    if (pipes[i][j+1] in RIGHT) and (pipes[i][j] in LEFT):
        pipes[i][j] = "X"
        return i, j+1
    elif (pipes[i][j-1] in LEFT) and (pipes[i][j] in RIGHT):
        pipes[i][j] = "X"
        return i, j-1
    elif (pipes[i+1][j] in DOWN) and (pipes[i][j] in UP):
        pipes[i][j] = "X"
        return i+1, j
    elif (pipes[i-1][j] in UP) and (pipes[i][j] in DOWN):
        pipes[i][j] = "X"
        return i-1, j
    else:
        return False


def main(pipefile):
    data = open(pipefile, "r")
    pipes0 = data.readlines()
    pipes = parse_pipes(pipes0)
    start_i, start_j = findstart(pipes)
    incrementer = 0
    visited = [(start_i, start_j)]
    point = find_next(pipes, (start_i, start_j))
    while point:
        incrementer += 1
        visited.append(point)
        point = find_next(pipes, point)
    print((incrementer+1)//2)

    internal_points = 0
    cleanpipes = parse_pipes(pipes0)
    for i, row in enumerate(cleanpipes):
        for j, val in enumerate(row):
            if (i, j) in visited:
                continue
            pipe_crossings = 0
            i2, j2 = i, j
            while (i2 < len(cleanpipes)) and (j2 < len(row)):
                point = cleanpipes[i2][j2]
                if ((i2, j2) in visited) and (point != 'L') and (point != '7'):
                    pipe_crossings += 1
                i2 += 1
                j2 += 1
            if pipe_crossings % 2 == 1:
                internal_points += 1
    print(internal_points)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="day 10 of Advent of Code")
    parser.add_argument("datafile", help='text file of data')
    args = parser.parse_args()
    main(args.datafile)
