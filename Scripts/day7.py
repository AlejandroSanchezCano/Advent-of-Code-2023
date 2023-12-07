'''
Welcome to Advent of Code!
Day 7: Camel Cards 
https://adventofcode.com/2023/day/7
'''

from typing import Literal
from collections import Counter

def read_input(file: str) -> list[list[str, str]]:
    '''
    Reads the Advent of Code input file and returns the hands and bids as lists
    of [hand, bid] lists.

    Parameters
    ----------
    file : str
        Path to the input file.

    Returns
    -------
    list[list[str, str]]
        List with [hand, bid] lists
    '''

    hands_bids = []

    with open(file, 'r') as handle:
        for line in handle.readlines():
            hands_bids.append(line.strip().split())
    
    return hands_bids

def hash_hand1(hand: str) -> str:
    '''
    Hashes the playing hand to an alphabetic code that eases the process of 
    sorting using the 'key' argument of the sorting functions/methods. The 
    hashing method is:
    - 1 capital letter A-G according to the hand type.
    - 5 lowercase letters a-m according to the rank of the sequencial cards.
    This does not takes into account that J is a joker/placeholder card and has the
    lowest rank (problem 1)


    Parameters
    ----------
    hand : str
        Playing hand -> 'AAKJ4'

    Returns
    -------
    str
        Hashed hand -> 'Faabdk'
    '''

    # Count the number of cards in each hand
    card2count = Counter(hand)

    # Rank hash dictionary
    cards2rank = {
        'A': 'a', 'K': 'b', 'Q': 'c', 'J': 'd', 
        'T': 'e', '9': 'f', '8': 'g', '7': 'h',
        '6': 'i', '5': 'j', '4': 'k', '3': 'l', '2': 'm'
    }

    # Sort per values
    card_counts = sorted(card2count.values())

    # Type hash conditionals
    if card_counts == [5]:
        hash = 'A'
    elif card_counts == [1, 4]:
        hash = 'B'
    elif card_counts == [2, 3]:
        hash = 'C'
    elif card_counts == [1, 1, 3]:
        hash = 'D'
    elif card_counts == [1, 2, 2]:
        hash = 'E'
    elif card_counts == [1, 1, 1, 2]:
        hash = 'F'
    else:
        hash = 'G'

    # Concatenate the two hash parts
    return hash + ''.join([cards2rank[card] for card in hand])

def hash_hand2(hand: str) -> str:
    '''
    Hashes the playing hand to an alphabetic code that eases the process of 
    sorting using the 'key' argument of the sorting functions/methods. The 
    hashing method is:
    - 1 capital letter A-G according to the hand type.
    - 5 lowercase letters a-m according to the rank of the sequencial cards.
    This takes into account that J is a joker/placeholder card and has the
    lowest rank (problem 2)


    Parameters
    ----------
    hand : str
        Playing hand -> 'AAKJ4'

    Returns
    -------
    str
        Hashed hand -> 'Daabmj'
    '''

    # Count the number of cards in each hand
    card2count = Counter(hand)

    # Rank hash dictionary
    cards2rank = {
        'A': 'a', 'K': 'b', 'Q': 'c', 'J': 'm', 
        'T': 'd', '9': 'e', '8': 'f', '7': 'g',
        '6': 'h', '5': 'i', '4': 'j', '3': 'k', '2': 'l'
    }

    # Transform the J card into the most convenient card
    if 1 <= card2count.get('J', 0) <= 4:

        # J cards will transform into other cards
        j = card2count.pop('J')

        # If all cards are different, the J cards will morph into the one with
        # highest rank in the hand. Otherwise, into the most frequent card
        if len(card2count.values()) == 5:
            most_convenient = min(card2count, key=lambda x: cards2rank[x])
        else:
            most_convenient = max(card2count, key=card2count.get)

        # Add the amount of J cards to the most convinient card type
        card2count[most_convenient] += j

    # Edge case -> 'JJJJJ'
    elif card2count.get('J', 0) == 5:
        return 'Ammmmm'
    
    # Sort per values
    card_counts = sorted(card2count.values())

    # Type hash conditionals
    if card_counts == [5]:
        hash = 'A'
    elif card_counts == [1, 4]:
        hash = 'B'
    elif card_counts == [2, 3]:
        hash = 'C'
    elif card_counts == [1, 1, 3]:
        hash = 'D'
    elif card_counts == [1, 2, 2]:
        hash = 'E'
    elif card_counts == [1, 1, 1, 2]:
        hash = 'F'
    else:
        hash = 'G'

    # Concatenate the two hash parts
    return hash + ''.join([cards2rank[card] for card in hand])
    
def calculate_winnings(hands_bids: list[list[str, str]], problem: Literal[1,2]) -> int:
    '''
    Takes the list with hands and bids, sort it based on the hash function and
    calculate the winnings as the sum of the bids times their position after
    the sorting. Depending on the problem, a different hashing function is used.

    Parameters
    ----------
    hands_bids : list[list[str, str]]
        List with [hand, bid] lists
    problem : Literal[1,2]
        Problem

    Returns
    -------
    int
        Winnings
    '''
    
    # Sort the hands based on the hashing and the problem
    if problem == 1:
        sorted_hands = sorted(
            hands_bids, 
            reverse = True, 
            key = lambda x: hash_hand1(x[0])
        )
    elif problem == 2:
        sorted_hands = sorted(
            hands_bids, 
            reverse = True, 
            key = lambda x: hash_hand2(x[0])
        )
        
    # Calculate the winnings
    winnings = 0
    for rank, hand in enumerate(sorted_hands):
        winnings += (rank + 1) * int(hand[1])

    return winnings


def main():
    '''Program process'''
    hands_bids = read_input('Inputs/day7.txt')
    print(calculate_winnings(hands_bids, 1))
    print(calculate_winnings(hands_bids, 2))


    
if __name__ ==  '__main__':
    main()