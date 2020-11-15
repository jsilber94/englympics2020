import sys
from parsing import parse_json

if __name__ == '__main__':
    supplier_name = parse_json(sys.argv[1])
    print(supplier_name)

