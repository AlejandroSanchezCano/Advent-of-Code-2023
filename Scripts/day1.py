'''
Welcome to Advent of Code!
Day 1: Trebuchet?!
https://adventofcode.com/2023/day/1
'''

from typing import Generator, Literal

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

def digit_search(
        string: str, 
        side: Literal['front', 'back'], 
        exercise: Literal[1, 2]
        ) -> int:
    '''
    Finds the first (side = "front") or last (side = "back") digit in a string. 
    The digit could be represented by integers solely (exercise = 1) or also by
    their words in the English language (exercise = 2) (e.g. 2 = two)

    Parameters
    ----------
    string: str
        Each input line where the digits must be found

    side: Literal['front', 'back']
        "front" if the first digit is wanted
        "back" if the last digit is wanted

    exercise: Literal[1, 2]
        1 if first AoC exercise
        2 if second AoC exercise
    
    Returns
    -------
    Digit wanted
    '''

    # Initialize dictionary to translate to integers
    words_to_digits = {
        'zero' : 0,
        'one' : 1,
        'two' : 2,
        'three' : 3,
        'four' : 4,
        'five' : 5,
        'six' : 6,
        'seven' : 7,
        'eight' : 8,
        'nine': 9    
    }

    # Determine which indeces to look with
    if side == 'front':
        indeces = range(len(string)) # 0, 1, 2, 3, ..., len() - 1
    elif side == 'back':
        indeces = range(len(string) - 1, -1, -1) # len() - 1, len() - 2, ..., 0

    # Loop over the string characters
    for index in indeces:

        # Check if character is a digit 
        char = string[index]
        if char.isdigit():
            return int(char)
        
        # Skip the rest for exersice 1
        if exercise == 1:
            continue
        
        # If no digits have been found, the substrting from the index point
        # until the beginning (front) or the end (back) is alphabetic
        if side == 'front':
            alphabetic = string[0 : index + 1]
        elif side == 'back':
            alphabetic = string[index : len(string)]

        # Check if the alphabetic sequence corresponds to any digit
        for word_number in words_to_digits:
            if word_number in alphabetic:
                return int(words_to_digits[word_number])

def calibrate(exercise: Literal[1, 2]) -> int:
    '''
    Calculate the calibration values and its sum.

    Paramaters
    ----------
    exercise: Literal[1, 2]
        1 if first AoC exercise
        2 if second AoC exercise

    Returns
    -------
    Sum of all calibration values
    '''

    # Initialize general sum
    calibration_sum = 0

    # Iterate over input lines
    for line in read_input('Inputs/day1.txt'):

        # Get first (decenas) and last (unidades) digits
        first_digit = digit_search(line, 'front', exercise) * 10 
        last_digit = digit_search(line, 'back', exercise)

        # Add them to the sum
        calibration_sum += first_digit + last_digit

    return calibration_sum

def main():
    '''Program process'''
    print(calibrate(1))
    print(calibrate(2))

if __name__ ==  '__main__':
    main()