from pandas import read_csv
from matchstrings import MatchString


def binary_search_on_suppliers(supplier_lists_path, target, search_type):
    # raw_data = []
    #
    # for x in range(len(supplier_lists_path)):
    #     raw_data.append(read_csv(supplier_lists_path[x]))

    dataframe_csv1 = read_csv(supplier_lists_path[0], delimiter=',', encoding='utf-8')
    dataframe_csv2 = read_csv(supplier_lists_path[1], delimiter=',', encoding='utf-8')
    dataframe_csv3 = read_csv(supplier_lists_path[2], delimiter=',', encoding='utf-8')
    dataframe_csv4 = read_csv(supplier_lists_path[3], delimiter=',', encoding='utf-8')

    raw_data_csv1 = dataframe_csv1.to_numpy()
    raw_data_csv2 = dataframe_csv2.to_numpy()
    raw_data_csv3 = dataframe_csv3.to_numpy()
    raw_data_csv4 = dataframe_csv4.to_numpy()

    supplier = None

    if search_type == 'name':
        supplier = binary_search_for_strings(raw_data_csv1, target, search_type)
    elif search_type == 'phone':
        supplier = binary_search_for_strings(raw_data_csv3, target, search_type)

    if supplier is not None:
        print_supplier(supplier, '1')
        return True

    else:
        if search_type == 'name':
            supplier = binary_search_for_strings(raw_data_csv2, target, search_type)
        elif search_type == 'phone':
            supplier = binary_search_for_strings(raw_data_csv4, target, search_type)
        if supplier is not None:
            print_supplier(supplier, '2')
            return False


def clean_str(string):
    cast_string = str(string)
    clean_string = cast_string.replace('\ufffd', '')
    return clean_string


def binary_search_for_strings(arr, target, search_type):
    m = MatchString()
    start = 0
    end = len(arr) - 1
    max_distance = 100000
    best_index = -1
    best_name = ""
    while start <= end:
        middle = (start + end) // 2
        search_string = ''

        if search_type == 'name':
            search_string = clean_str(arr[middle][0])
        elif search_type == 'phone':
            search_string = clean_str(arr[middle][3]) + '.0'

        midpoint = search_string
        distance = m.match(target.lower(), search_string.lower())

        if distance < max_distance:
            best_index = middle
            max_distance = distance
            if distance < 2:
                return arr[best_index]

        if midpoint > target:
            end = middle - 1
        elif midpoint < target:
            start = middle + 1

    for row in arr:
        search_string = clean_str(row[0])
        distance = m.match(target.lower(), search_string.lower())

        if distance < max_distance:
            max_distance = distance
            if distance < 5:
                return row

    return arr[best_index]


def print_supplier(supplier, file_nbr):
    print('name: ' + supplier[0])
    # print('SIC4 Category: ' + supplier[1])
    # print('SIC8 Category: ' + supplier[2])
    # print('Phone: ' + str(supplier[3]))
    # print('id: ' + str(supplier[4]))
    # print('file number: ' + file_nbr)
