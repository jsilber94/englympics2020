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

    binary_search_on_suppliers(supplier_lists_path, '$29 Garage Door Openers Repair Alameda Ca 510-214-800')
    m = MatchString();
    print(m.match('$29 Garage Door Openers Repair Alameda Ca 510-214-8005', '$29 Garage Door Openers Repai Alameda Ca 510-214-8005'))

