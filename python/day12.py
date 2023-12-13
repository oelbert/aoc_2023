import argparse


def parse_row(row):
    reduced = row.strip()
    vals, v2s = reduced.split(" ")
    contigs = v2s.split(",")
    pass


def main(imgfile):
    data = open(imgfile, "r")
    rows = data.readlines()
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="day 12 of Advent of Code")
    parser.add_argument("datafile", help='text file of data')
    args = parser.parse_args()
    main(args.datafile)