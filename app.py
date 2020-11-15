import sys

import numpy as np
from weighted_levenshtein.clev import dam_lev

from process_json import process_json
from matchstrings import MatchString

if __name__ == '__main__':

    # supplier_name = parse_json(sys.argv[1])
    search_objects = process_json("data/Training Json")
    for search_object in search_objects:
        print(search_object.phone)
        print(search_object.name)
        print("----------------------")

    # supplier_name = parse_json(sys.argv[1])
    # print(supplier_name)
    transpose_costs = np.ones((128, 128), dtype=np.float64)
    m = MatchString()
    print(m.match("BODY", "BEDY"))
