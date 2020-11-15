import sys
import os
import time
from process_json import process_json

from search import binary_search_on_suppliers

if __name__ == '__main__':
    # supplier_name = parse_json(sys.argv[1])
    supplier_lists_path = [
        os.path.abspath("data/supplierList/supplierlist1-sorted.csv"),
        os.path.abspath("data/supplierList/supplierlist2-sorted.csv")
    ]

    # process json and get a list of keywords to match
    # supplier_name = parse_json(sys.argv[1])
    search_objects = process_json("data/Training Json")

    start = time.time()
    # iterate through the keywords file by file
    for store in search_objects:
        if store.phone is not None and binary_search_on_suppliers(supplier_lists_path, store.phone) is False:
            for name in store.name:
                if binary_search_on_suppliers(supplier_lists_path, name) is True:
                    break
        print(time.time() - start)

    print(str((time.time() - start) / 60) + " minutes.")

#  if binary_search_on_suppliers(supplier_lists_path, '$29 Garage Door Openers Repair Alameda Ca 510-214-8005') is True:
