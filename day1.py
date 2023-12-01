'''
Welcome to Advent of Code!
Day 1: Trebuchet?!
https://adventofcode.com/2023/day/1
'''

from typing import Generator

def read_input(file: str) -> Generator[str, None, None]:
    with open(file, 'r') as handle:
        for line in handle.readlines():
            yield line.strip()

def digit_search(string: str, side: str, exercise) -> int:

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
        indeces = range(len(string))
    elif side == 'back':
        indeces = range(-1, -len(string) - 1, -1)

    # Use the indeces to check whether the characters are digits
    alpha_char_memo = ''
    for index in indeces:
        char = string[index]
        if char.isdigit():
            return int(char)
        
        if exercise == 1:
            continue

        if side == 'front':
            alpha_char_memo += char
        elif side == 'back':
            alpha_char_memo = char + alpha_char_memo

        for word_number in words_to_digits:
            if word_number in alpha_char_memo:
                return int(words_to_digits[word_number])

def calibrate(exercise) -> int:

    # Initialize general sum
    calibration_sum = 0

    # Iterate over input lines
    for line in read_input('day1.txt'):

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