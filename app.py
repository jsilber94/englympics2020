import sys

from parsing import parse_json
from matchstrings import MatchString


if __name__ == '__main__':
    #supplier_name = parse_json(sys.argv[1])
    #print(supplier_name)
    m = MatchString();
    print(m.match("test", "jesj"))

