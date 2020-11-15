import sys

import numpy as np
from weighted_levenshtein.clev import dam_lev

from parsing import parse_json
from matchstrings import MatchString


if __name__ == '__main__':
    #supplier_name = parse_json(sys.argv[1])
    #print(supplier_name)
    transpose_costs = np.ones((128, 128), dtype=np.float64)
    m = MatchString()
    print(m.match("HANANA", "BANANA"))

