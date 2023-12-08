'''
Welcome to Advent of Code!
Day 8: Haunted Wasteland
https://adventofcode.com/2023/day/8
'''

import re
from math import lcm

def read_input(file: str) -> tuple[list[int], dict[str, tuple[str, str]]]:
    '''
    Reads the Advent of Code input file and returns the binary left/right
    instructions as 0s and 1s, respectively, and the network as a dictionary
    with nodes as keys and their children nodes as values.

    Parameters
    ----------
    file : str
        Path to the input file.

    Returns
    -------
    tuple[list[int], dict[str, tuple[str, str]]]
        1) directions: list of 0s (left) and 1s (right) representing the index
        of which children node to follow next.
        2) parent2children: dictionary with parent nodes as keys and their
        children nodes as values.
    '''
    # Open file
    with open(file, 'r') as handle:
        # Read all lines in memory
        lines = handle.readlines()
        # Convert 'L' and 'R' to 0s and 1s
        directions = [0 if i == 'L' else 1 for i in lines[0].strip() ]
        # Make the parent2children dictionary by using re to find the triplets
        parent2children = {}
        for line in lines[2:]:
            prevoius, left, right = re.findall(r'[A-Z]{3}', line)
            parent2children[prevoius] = (left, right)

    return directions, parent2children

def navigate_network1(
        directions: list[int], 
        parent2children: dict[str, tuple[str, str]]
        ) -> int:
    '''
    Brute force network navigation method in which we transverse the tree of 
    nodes represented by the 'parent2children' dictionary from node to node 
    following the 'directions' indications until reaching the 'ZZZ' node.

    Parameters
    ----------
    directions : list[int]
        List of 0s (left) and 1s (right) representing the index
        of which children node to follow next.
    parent2children : dict[str, tuple[str, str]]
        Dictionary with parent nodes as keys and their
        children nodes as values -> {'AAA': ('ZZZ', 'ZZZ')}

    Returns
    -------
    int
        Number of steps required to reach ZZZ.
    '''

    # Initialize starting variables
    step, times = 0, 0
    current_node = 'AAA'

    # While loop to iterate over eacht direction step and also each cycle of
    # directions
    while current_node != 'ZZZ':
        
        # Update current node
        current_node = parent2children[current_node][directions[step]]

        # One step taken
        step += 1

        # One cycle of directions taken
        if step == len(directions):
            step = 0
            times += 1

    # Amount of total steps 
    return times*len(directions) + step

def navigate_network2(
        directions: list[int], 
        parent2children: dict[str, tuple[str, str]]
        ) -> int:
    '''
    For the second problem, brute force is not possible. The more intelligent
    and efficient way of computing the number of navigating steps for all the
    starting nodes (those ending with 'A') to reach a node ending in 'Z' takes
    into account a clever pattern: navigating the network results in cycles of
    a certain periodicity in which the ending node is reached in a fixed number
    of steps specific for each starting point. Least common multiple is used to
    calculate when all starting nodes will reach their corresponding ending
    node.

    Parameters
    ----------
    directions : list[int]
        List of 0s (left) and 1s (right) representing the index
        of which children node to follow next.
    parent2children : dict[str, tuple[str, str]]
        Dictionary with parent nodes as keys and their
        children nodes as values -> {'AAA': ('ZZZ', 'ZZZ')}

    Returns
    -------
    int
        Number of steps for all starting nodes ('__A') to reach an ending node
        ('__Z') simultaneously.
    '''
    
    # Search starting nodes, those that end with 'A'
    starting_nodes = [node for node in parent2children if node.endswith('A')]
    # List with the number of direction steps to reach the converging node
    n_steps = [0]*len(starting_nodes)

    # Iterate over the 6 starting nodes
    for step, node in enumerate(starting_nodes):
        # Iterate over (concatenated) directions list
        for direction in directions*100:
            # Update current node
            node = parent2children[node][direction]
            # Add a step to the corresponding starting nodes
            n_steps[step] += 1
            # Detect node ending with 'Z'
            if node.endswith('Z'):
                break

    return lcm(*n_steps)

def main():
    '''Program process'''
    directions, parent2children = read_input('Inputs/day8.txt')
    print(navigate_network1(directions, parent2children))
    print(navigate_network2(directions, parent2children))
    
if __name__ ==  '__main__':
    main()