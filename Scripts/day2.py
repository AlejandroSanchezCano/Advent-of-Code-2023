'''
Welcome to Advent of Code!
Day 2: Cube Conundrum
https://adventofcode.com/2023/day/2
'''

from typing import Generator, Tuple

def read_input(file: str) -> Generator[str, None, None]:
    '''
    Builds a generator yielding each line of the Advent of Code input file. 

    Parameters
    ----------
    file: str
        Path to the input file.
    Returns
    -------
    Generator[str, None, None]:
        Each line of the input file.
    '''
    with open(file, 'r') as handle:
        for line in handle.readlines():
            yield line.strip()

def cubes_per_game() -> Tuple:

    for line in read_input('Inputs/day2.txt'):

        cube_tally = {
            'red' : 0,
            'green' : 0, 
            'blue' : 0
        }

        game_info, cube_info = line.split(': ')
        game_id = int(game_info[5:])

        for cubes in cube_info.replace(';', ',').split(', '):
            n_cubes, color = cubes.split(' ')
            if int(n_cubes) > cube_tally[color]:
                cube_tally[color] = int(n_cubes)

        yield game_id, cube_tally

def check_possibility_configuration(cube_tally):
        max_cubes = {
            'red' : 12,
            'green' : 13, 
            'blue' : 14
        }

        for color in ('red', 'green', 'blue'):
            if cube_tally[color] > max_cubes[color]:
                return False
        
        return True

def count_posible_games():

    possible_games_sum = 0
    power_sum = 0

    for game_id, cube_tally in cubes_per_game():

        power_sum += cube_tally['red'] * cube_tally['green'] * cube_tally['blue']

        if check_possibility_configuration(cube_tally):
            possible_games_sum += game_id
    
    return f'Solution 1: {possible_games_sum},  solution 2: {power_sum}'

def main():
    '''Program process'''
    print(count_posible_games())

if __name__ ==  '__main__':
    main()