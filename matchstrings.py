import numpy as np
from weighted_levenshtein import lev


class MatchString:

    def __init__(self):
        self.insert_costs = np.ones(128,
                                    dtype=np.float64)  # make an array of all 1's of size 128, the number of ASCII characters
        # Insert Weight Distance
        self.insert_costs[ord(' ')] = 1.5
        self.insert_costs[ord('1')] = 1.5
        self.insert_costs[ord('2')] = 1.5
        self.insert_costs[ord('3')] = 1.5
        self.insert_costs[ord('4')] = 1.5
        self.insert_costs[ord('5')] = 1.5
        self.insert_costs[ord('6')] = 1.5
        self.insert_costs[ord('7')] = 1.5
        self.insert_costs[ord('8')] = 1.5
        self.insert_costs[ord('9')] = 1.5

        self.substitute_costs = np.ones((128, 128), dtype=np.float64)  # make a 2D array of 1's

        # Common OCR Deletion Mistakes
        self.delete_costs = np.ones(128, dtype=np.float64)
        self.delete_costs[ord(' ')] = 0.25

        # Common OCR Mistakes - Group 1
        self.substitute_costs[ord('o'), ord('o')] = 0.25
        self.substitute_costs[ord('d'), ord('o')] = 0.25

        self.substitute_costs[ord('q'), ord('d')] = 0.25
        self.substitute_costs[ord('d'), ord('q')] = 0.25

        self.substitute_costs[ord('o'), ord('q')] = 0.25
        self.substitute_costs[ord('q'), ord('o')] = 0.25

        # Common OCR Mistakes - Group 2
        self.substitute_costs[ord('i'), ord('j')] = 0.25
        self.substitute_costs[ord('j'), ord('i')] = 0.25

        self.substitute_costs[ord('i'), ord('l')] = 0.25
        self.substitute_costs[ord('l'), ord('i')] = 0.25

        self.substitute_costs[ord('i'), ord('t')] = 0.25
        self.substitute_costs[ord('t'), ord('i')] = 0.25

        self.substitute_costs[ord('j'), ord('l')] = 0.25
        self.substitute_costs[ord('l'), ord('j')] = 0.25

        self.substitute_costs[ord('j'), ord('t')] = 0.25
        self.substitute_costs[ord('t'), ord('j')] = 0.25

        self.substitute_costs[ord('l'), ord('t')] = 0.25
        self.substitute_costs[ord('t'), ord('l')] = 0.25

        # Common OCR Mistakes - Group 3

        self.substitute_costs[ord('u'), ord('v')] = 0.25
        self.substitute_costs[ord('v'), ord('u')] = 0.25

        # Common OCR Mistakes - Group 4

        self.substitute_costs[ord('f'), ord('p')] = 0.25
        self.substitute_costs[ord('p'), ord('f')] = 0.25

        # Common OCR Mistakes - Group 5

        self.substitute_costs[ord('c'), ord('g')] = 0.25
        self.substitute_costs[ord('g'), ord('c')] = 0.25

    def match(self, string1, string2):
        # Testing
        return lev(string1.lower(), string2.lower(), substitute_costs=self.substitute_costs, delete_costs=self.delete_costs, insert_costs=self.insert_costs)
