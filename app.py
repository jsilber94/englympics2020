import sys

import numpy as np

from parsing import parse_json
from matchstrings import match

def init_constants():
    insert_costs = np.ones(128, dtype=np.float64)

    insert_costs = np.ones(128,
                           dtype=np.float64)  # make an array of all 1's of size 128, the number of ASCII characters
    insert_costs[ord('D')] = 1.5  # make inserting the character 'D' have cost 1.5 (instead of 1)

    substitute_costs = np.ones((128, 128), dtype=np.float64)  # make a 2D array of 1's
    substitute_costs[ord('H'), ord('B')] = 1.25  # make substituting 'H' for 'B' cost 1.25

    # Common OCR Deletion Mistakes
    delete_costs = np.ones(128, dtype=np.float64)
    delete_costs[ord('S')] = 0.5
    delete_costs[ord(' ')] = 0.5

    transpose_costs = np.ones((128, 128), dtype=np.float64)

    # Common OCR Mistakes - Group 1
    transpose_costs[ord('O'), ord('D')] = 0.5
    transpose_costs[ord('D'), ord('O')] = 0.5

    transpose_costs[ord('Q'), ord('D')] = 0.5
    transpose_costs[ord('D'), ord('Q')] = 0.5

    transpose_costs[ord('O'), ord('Q')] = 0.5
    transpose_costs[ord('Q'), ord('O')] = 0.5

    # Common OCR Mistakes - Group 2
    transpose_costs[ord('I'), ord('J')] = 0.5
    transpose_costs[ord('J'), ord('I')] = 0.5

    transpose_costs[ord('I'), ord('L')] = 0.5
    transpose_costs[ord('L'), ord('I')] = 0.5

    transpose_costs[ord('I'), ord('T')] = 0.5
    transpose_costs[ord('T'), ord('I')] = 0.5

    transpose_costs[ord('J'), ord('L')] = 0.5
    transpose_costs[ord('L'), ord('J')] = 0.5

    transpose_costs[ord('J'), ord('T')] = 0.5
    transpose_costs[ord('T'), ord('J')] = 0.5

    transpose_costs[ord('L'), ord('T')] = 0.5
    transpose_costs[ord('T'), ord('L')] = 0.5

    # Common OCR Mistakes - Group 3

    transpose_costs[ord('U'), ord('V')] = 0.5
    transpose_costs[ord('V'), ord('U')] = 0.5

    # Common OCR Mistakes - Group 4

    transpose_costs[ord('F'), ord('P')] = 0.5
    transpose_costs[ord('P'), ord('F')] = 0.5

    # Common OCR Mistakes - Group 5

    transpose_costs[ord('C'), ord('G')] = 0.5
    transpose_costs[ord('G'), ord('C')] = 0.5


if __name__ == '__main__':
    init_constants()
    #supplier_name = parse_json(sys.argv[1])
    #print(supplier_name)
    match()

