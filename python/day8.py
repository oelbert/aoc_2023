from math import gcd


def LCM(a, b):
    return abs(a*b)//gcd(a, b)


def parse_node(node, nodemap):
    name, points = node.strip().split(" = ")
    left = points.split(", ")[0][1:]
    right = points.split(", ")[1][:-1]
    nodemap[name] = [left, right]


def run_day8(instructions, nodes):
    nodemap = {}
    for node in nodes:
        parse_node(node, nodemap)
    name = "AAA"
    nsteps1 = 0
    # breakpoint()
    while name != "ZZZ":
        direction = instructions[nsteps1 % len(instructions)]
        if direction == "L":
            name = nodemap[name][0]
        elif direction == "R":
            name = nodemap[name][1]
        else:
            raise ValueError(f"direction {direction} not L or R")
        nsteps1 += 1

    ghost_steps = []
    ghost_nodes = list(filter(lambda x: x.endswith("A"), list(nodemap.keys())))
    for node in ghost_nodes:
        nsteps = 0
        while not node.endswith("Z"):
            direction = instructions[nsteps % len(instructions)]
            if direction == "L":
                node = nodemap[node][0]
            elif direction == "R":
                node = nodemap[node][1]
            else:
                raise ValueError(f"direction {direction} not L or R")
            nsteps += 1
        ghost_steps.append(nsteps)
    nsteps2 = 1
    for count in ghost_steps:
        nsteps2 = LCM(nsteps2, count)
    return nsteps1, nsteps2


def main():
    data = open("../data/day8.txt", "r")
    lines = data.readlines()
    instructions = lines[0].strip()
    nodes = lines[2:]
    print(run_day8(instructions, nodes))


if __name__ == "__main__":
    main()
