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

    Yields
    -------
    Generator[str, None, None]:
        Each line of the input file.
    '''
    with open(file, 'r') as handle:
        for line in handle.readlines():
            yield line.strip()

def cubes_per_game() -> Generator[Tuple[int, dict[str, int]], None, None]:
    '''
    Takes each game line and yields its ID and how many cubes per color are 
    needed for the game to be possible.

    Yields
    ------
    Generator[Tuple[int, dict[str, int]], None, None]
        Game ID and dictionary with 'red', 'green' and 'blue' as keys and their
        respective maximum number of cubes in the game.
    '''

    # Read line
    for line in read_input('Inputs/day2.txt'):
        
        # Initialize empty dictionary color : max cubes
        cube_tally = {
            'red' : 0,
            'green' : 0, 
            'blue' : 0
        }

        # Get game ID
        game_info, cube_info = line.split(': ')
        game_id = int(game_info[5:])

        # Update dict with max number of cubes per color in all sets
        for cubes in cube_info.replace(';', ',').split(', '):
            n_cubes, color = cubes.split(' ')
            if int(n_cubes) > cube_tally[color]:
                cube_tally[color] = int(n_cubes)

        yield game_id, cube_tally

def check_possibility_configuration(cube_tally: dict[str, int]) -> bool:
    '''
    Compares the game configuration with the maximum number of cubes allowed for
    a game to be possible and returns whether the game is possible or 
    impossible.

    Parameters
    ----------
    cube_tally : dict[str, int]
        Dictionary with 'red', 'green' and 'blue' as keys and their
        respective maximum number of cubes in the game.

    Returns
    -------
    bool
        Whether the game is possible or impossible
    '''

    # Maximum number of cubes allowed in each game
    max_cubes = {
        'red' : 12,
        'green' : 13, 
        'blue' : 14
    }

    # Check if game configuration exceeds the maximum allowed
    for color in ('red', 'green', 'blue'):
        if cube_tally[color] > max_cubes[color]:
            return False
    
    # Returns true as default
    return True

def give_solutions() -> str:
    '''
    Take the cube tally per color of all games and calculate the sum of
    possible games and the sum of the power.

    Returns
    -------
    str
        Human-readible string with the sum of possible games (solution 1) and 
        the sum of the power (solution 2)
    '''

    # Initialize return variables
    possible_games_sum = 0
    power_sum = 0

    # Iterate over the game IDs and the maximum cubes found
    for game_id, cube_tally in cubes_per_game():

        # Power = minumum configuration of cubes for the game to be valid
        power_sum += cube_tally['red'] * cube_tally['green'] * cube_tally['blue']

        # Is the game possible?
        if check_possibility_configuration(cube_tally):
            possible_games_sum += game_id
    
    return f'Solution 1: {possible_games_sum},  solution 2: {power_sum}'

def main():
    '''Program process'''
    print(give_solutions())

if __name__ ==  '__main__':
    main()