'''
Welcome to Advent of Code!
Day 5: If you give a seed a fertilizer 
https://adventofcode.com/2023/day/5
'''

from typing import Generator

def read_input(file: str) -> Generator[str, None, None]:

    with open(file, 'r') as handle:
        lines = handle.readlines()
        seeds1 = [int(seed) for seed in lines[0][6:].split()]

        seeds2 = [0]*(len(seeds1)//2)
        for n, pair in enumerate(range(0, len(seeds1), 2)):
            start = seeds1[pair]
            stop = start + seeds1[pair + 1]
            print(start, stop)
            seeds2[n] = range(start, stop)
        #seeds2 = [range(seeds1[pair], seeds1[pair + 1]) for pair in range(0, len(seeds1), 2)]
        #print(seeds2)
        
        maps = {}
        for line in lines[2:]:
            if line.endswith('map:\n'):
                map_name = line[:-5]
                maps[map_name] = []
            elif line != '\n':
                numbers = [int(number) for number in line.split()]
                maps[map_name].append(numbers)

        return seeds1, seeds2, maps
    
def use_map(seed = 1, map = [[0, 222541565, 2]]):

    for map_part in map:
        if map_part[1] < seed < map_part[1] + map_part[2]:
            return map_part[0] + seed - map_part[1]
        
    return seed

def solve1(seeds, maps):
    seeds_locations = [0]*len(seeds)

    for n, seed in enumerate(seeds):
        for map in maps.values():
            seed = use_map(seed, map)
            
        seeds_locations[n] = seed

    return min(seeds_locations)

def solve2(seeds, maps):
    min_location = 490809890809226660576
    for seed_range in seeds:
        print('jey', min_location)
        for seed in seed_range:
            for map in maps.values():
                seed = use_map(seed, map)

        if seed < min_location:
            min_location = seed

    return min_location


def main():
    '''Program process'''
    seeds1, seeds2, maps = read_input('Inputs/day5.txt')
    print(solve2(seeds2, maps))
    #print(use_map())

if __name__ ==  '__main__':
    main()