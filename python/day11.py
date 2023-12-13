import argparse


def expand_image(image):
    columns = [j for j in range(len(image[0].strip()))]
    galaxy_columns = set([])
    parsed_image = []
    empty_rows = []
    for i, row0 in enumerate(image):
        row = row0.strip()
        if row == '.'*len(row):
            empty_rows.append(i)
        else:
            for j, val in enumerate(row):
                if val == '#':
                    galaxy_columns.add(j)
        parsed_image.append(list(row))
    empty_columns = [col for col in columns if col not in galaxy_columns]
    return parsed_image, empty_rows, empty_columns


def find_distances_with_variable_expansion(
    image,
    empty_rows,
    empty_columns,
    expansion_factor
):
    tot_dist = 0
    all_galaxies = set([])
    for i, row in enumerate(image):
        for j, val in enumerate(row):
            if val == '#':
                all_galaxies.add((i, j))
    galaxies = list(all_galaxies)
    for k, gal in enumerate(galaxies[:-1]):
        for pair in galaxies[k+1:]:
            i_diff = [d + min([gal[0], pair[0]]) for d in range(abs(gal[0] - pair[0]))]
            empties_i = [row for row in empty_rows if row in i_diff]
            i_dist = len(i_diff) - len(empties_i) + (len(empties_i) * expansion_factor)
            
            j_diff = [d + min([gal[1], pair[1]]) for d in range(abs(gal[1] - pair[1]))]
            empties_j = [row for row in empty_columns if row in j_diff]
            j_dist = len(j_diff) - len(empties_j) + (len(empties_j) * expansion_factor)
            tot_dist += i_dist + j_dist
            # breakpoint()
    return tot_dist


def main(imgfile):
    data = open(imgfile, "r")
    image0 = data.readlines()
    simple_image, empty_rows, empty_cols = expand_image(image0)
    tot_dist = find_distances_with_variable_expansion(simple_image, empty_rows, empty_cols, 2)
    print(tot_dist)
    new_dist = find_distances_with_variable_expansion(simple_image, empty_rows, empty_cols, 1000000)
    print(new_dist)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="day 11 of Advent of Code")
    parser.add_argument("datafile", help='text file of data')
    args = parser.parse_args()
    main(args.datafile)
