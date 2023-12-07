def elf_lookup(n: int, elfmap: list):
    for path in elfmap:
        destination, source, rangelen = map(int, path)
        if n in range(source, source+rangelen):
            return destination+n-source
    return n


def range_lookup(seeds, elfmap):
    return_seeds = []
    start = seeds[0]
    seedrange = seeds[1]
    while seedrange > 0:
        for path in elfmap[1:]:
            destination, source, rangelen = map(int, path)
            offset = start - source
            if offset in range(rangelen):
                interval = min(rangelen - offset, seedrange)
                return_seeds.append((destination + offset, interval))
                start += interval
                seedrange -= interval
                break
        else:
            return_seeds.append([start, seedrange])
            break
    return return_seeds


def run_day5(file: str) -> str:
    data = open(file, "r")
    lines = data.readlines()
    seeds = list(map(int, lines[0].split()[1:]))
    i = 2
    seed_soil_maplines = []
    minloc = -1
    while lines[i].split():
        seed_soil_maplines.append(lines[i].split())
        i += 1
    i += 1
    soil_fert_maplines = []
    while lines[i].split():
        soil_fert_maplines.append(lines[i].split())
        i += 1
    i += 1
    fert_water_maplines = []
    while lines[i].split():
        fert_water_maplines.append(lines[i].split())
        i += 1
    i += 1
    water_light_maplines = []
    while lines[i].split():
        water_light_maplines.append(lines[i].split())
        i += 1
    i += 1
    light_temp_maplines = []
    while lines[i].split():
        light_temp_maplines.append(lines[i].split())
        i += 1
    i += 1
    temp_hum_maplines = []
    while lines[i].split():
        temp_hum_maplines.append(lines[i].split())
        i += 1
    i += 1
    hum_loc_maplines = []
    while lines[i].split():
        hum_loc_maplines.append(lines[i].split())
        i += 1
        if i >= len(lines):
            break
    for seed in seeds:
        soil = elf_lookup(seed, seed_soil_maplines[1:])
        fertilizer = elf_lookup(soil, soil_fert_maplines[1:])
        water = elf_lookup(fertilizer, fert_water_maplines[1:])
        light = elf_lookup(water, water_light_maplines[1:])
        temp = elf_lookup(light, light_temp_maplines[1:])
        humidity = elf_lookup(temp, temp_hum_maplines[1:])
        location = elf_lookup(humidity, hum_loc_maplines[1:])
        if (minloc < 0) or (int(location) < minloc):
            minloc = int(location)
    inits = seeds[::2]
    ranges = seeds[1::2]
    soils = []
    ferts = []
    waters = []
    lights = []
    temps = []
    hums = []
    locs = []
    for i in range(len(seeds)//2):
        soils += range_lookup([inits[i], ranges[i]], seed_soil_maplines)
        for valpair in soils:
            ferts += range_lookup(valpair, soil_fert_maplines)
        for valpair in ferts:
            waters += range_lookup(valpair, fert_water_maplines)
        for valpair in waters:
            lights += range_lookup(valpair, water_light_maplines)
        for valpair in lights:
            temps += range_lookup(valpair, light_temp_maplines)
        for valpair in temps:
            hums += range_lookup(valpair, temp_hum_maplines)
        for valpair in hums:
            locs += range_lookup(valpair, hum_loc_maplines)
    minloc2 = min([loc[0] for loc in locs])
    return minloc, minloc2


def main():
    print(run_day5('../data/day5.txt'))


if __name__ == '__main__':
    main()
