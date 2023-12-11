'''
Welcome to Advent of Code!
Day 11: Cosmic Expansion
https://adventofcode.com/2023/day/11
'''

import numpy as np

def read_input(file: str) -> np.ndarray:
    '''
    Reads the input file and converts its content into a 2D numpy array where
    each element is either a galaxy '#' or empty space '.'.

    Parameters
    ----------
    file : str
        Path to the input file.

    Returns
    -------
    np.ndarray
        Space matrix.
    '''
    with open(file, 'r') as handle:
        return np.array([tuple(line.strip()) for line in handle.readlines()])
    
def manhattan(galaxy_h: tuple[int, int], galaxy_v:tuple[int, int]) -> int:
    '''
    Calculates the Manhattan distance of to points in the space grid given their
    horizontal and vertical coordinates.

    Parameters
    ----------
    galaxy_h : tuple[int, int]
        Tuple of horizontal coordinates of the galaxies.
    galaxy_v : tuple[int, int]
        Tuple of vertical coordinates of the galaxies.

    Returns
    -------
    int
        Manhattan distance.
    '''
    return np.abs(galaxy_h[1] - galaxy_h[0]) + np.abs(galaxy_v[1] - galaxy_v[0])

def empty(
        space: np.ndarray, 
        galaxies: tuple[np.ndarray, np.ndarray]
        ) -> tuple[np.ndarray, np.ndarray]:
    '''
    Locating the position of the galaxies also gives us the information of the
    rows and columns that are empty space. This is done by seeing which indeces 
    are missing in the horizontal and vertical indeced of the galaxies.

    Parameters
    ----------
    space : np.ndarray
        Space matrix.
    galaxies : tuple[np.ndarray, np.ndarray]
        Tuple with the vertical coordinates array of the galaxies in the first
        position anf the horizontal coordinates array of the galaxies in the
        second position.

    Returns
    -------
    tuple[np.ndarray, np.ndarray]
        Row and column indeces where there is no galaxy.
    '''
    n_empty_h = np.setdiff1d(np.arange(space.shape[0]), galaxies[0])
    n_empty_v = np.setdiff1d(np.arange(space.shape[1]), galaxies[1])

    return n_empty_h, n_empty_v

def distance_galaxies(space: np.ndarray, constant: int) -> int:
    '''
    The space matrix is used first to locate the galaxies and the rows and 
    columns without galaxies. To calculate the distance between galaxy pairs 
    after expansion we need to know how many expansion events happen between the
    galaxies. For that, the indeces of the galaxies are used to check for rows
    and columns wihtout galaxies. With this the distance after the expansion can 
    be calculated as the sum of:
    - Manhattan distance between the galaxies in the unexpanded space
    - Expansion constant * number of rows and cols without galaxies
    - Number of rows and cols without galaxies

    Parameters
    ----------
    space : np.ndarray
        Space matrix.
    constant : int
        Expansion constant.

    Returns
    -------
    int
        Sum of the distances between every pair of galaxies.
    '''
    # Initialize return variable
    distance_sum = 0
    # Locate galaxies in space
    galaxies = np.where(space == '#')
    # Locate rows and columns with no galaxies
    n_empty_h, n_empty_v = empty(space, galaxies)
    
    # Iterate over each pair of galaxies (without overlap)
    for i in range(len(galaxies[0])):
        for j in range(i + 1, len(galaxies[0])):

            # Useful sort of horizontal and vertical indeces of galaxies
            galaxies_h = sorted((galaxies[0][i], galaxies[0][j]))
            galaxies_v = sorted((galaxies[1][i], galaxies[1][j]))

            # Calculate the number of rows and cols without galaxies
            n_empty_row = len([i for i in n_empty_h if galaxies_h[0] < i < galaxies_h[1]])
            n_empty_col = len([i for i in n_empty_v if galaxies_v[0] < i < galaxies_v[1]])
            n_empty = n_empty_row + n_empty_col

            # Calculate distance after expansion 
            distance = manhattan(galaxies_h, galaxies_v)
            distance_sum += distance + n_empty*constant - n_empty

    return distance_sum

def main():
    '''Program process'''
    space = read_input('Inputs/day11.txt')
    print(distance_galaxies(space, 2))
    print(distance_galaxies(space, 1_000_000))

if __name__ ==  '__main__':
    main()

