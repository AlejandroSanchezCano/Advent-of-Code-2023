'''
Welcome to Advent of Code!
Day 4: Scratchcards 
https://adventofcode.com/2023/day/4
'''

from collections import defaultdict
from typing import Generator, Iterator

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

def get_matches() -> Iterator[int]:
    '''
    Reads and formats each scratchcard using the split() method and yield the 
    number of common numbers between the winning numbers and the elf's numbers 
    using set().

    Yields
    ------
    Iterator[int]
        Number of common numbers between the winning numbers and the elf's 
        numbers.
    '''

    for stratchcard in read_input('Inputs/day4.txt'):
        numbers = stratchcard.split(':')[1]
        winning_numbers, elf_numbers = [nums.split() for nums in numbers.split('|')]
        yield len(set(winning_numbers) & set(elf_numbers))
    
def calculate_scratchcard_points(matches: int) -> int:
    '''
    Calculate the points each scratchcard is worth given the number of matching
    numbers between the winning numbers and the elf numbers.

    Matches: 0, 1, 2, 3, 4, 5
    Points:  0, 1, 2, 4, 8, 16

    Parameters
    ----------
    matches : int
        Number of matching numbers between the winning numbers and the elf 
        numbers.

    Returns
    -------
    int
        Scratchcard points
    '''
    if matches == 0:
        return 0
    else:
        return 2**(matches - 1)

def calculate_total_points() -> tuple[int, int]:
    '''
    Solves part 1 by summing up all the points for all the scratchcards
    Solves part 2 by creating a dictionary card_number : copy_number and update
        it with every card according to the current iterating card and its 
        number of matches ->
        1: 1
        2: 2
        3: 4
        ...

    Returns
    -------
    tuple[int, int]
        Total amount of points (solution 1)
        Total amount of cards (solution 2)
    '''
    # Initialize part 1 and 2 variables
    total_points = 0
    scratchcards = defaultdict(int) # Dict with 0 as values

    # Iterate over the card number and the matches in it
    for card_number, matches in enumerate(get_matches()):

        # Solve part 1
        total_points += calculate_scratchcard_points(matches)
        
        # Solve part 2
        # Add original 
        scratchcards[card_number] += 1
        # Add copies
        for n_cards_below in range(1, matches + 1):
            scratchcards[card_number + n_cards_below] += scratchcards[card_number]

    return total_points, sum(scratchcards.values())


def main():
    '''Program process'''
    print(calculate_total_points())
if __name__ ==  '__main__':
    main()