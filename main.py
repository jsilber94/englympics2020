import sys
import os

from search import binary_search_on_suppliers
from matchstrings import MatchString

if __name__ == '__main__':
    # supplier_name = parse_json(sys.argv[1])
    supplier_lists_path = [
        os.path.abspath("data/supplierList/supplierlist1-sorted.csv"),
        os.path.abspath("data/supplierList/supplierlist2-sorted.csv")
    ]

    binary_search_on_suppliers(supplier_lists_path, '')
    m = MatchString()

