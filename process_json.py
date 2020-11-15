import json
import re
import os
from SearchObject import SearchObject


def text_annotations(store):
    return store[0]["description"]


def full_text_annotation(store):
    return store["text"]


def get_phone_number(text_to_parse):
    reg = re.compile("(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}")
    phone = reg.search(str(text_to_parse))
    if phone is None:
        return phone
    else:
        return ''.join(e for e in phone.group() if e.isalnum())


def get_name(text_to_parse):
    names = []
    text_to_parse_split = text_to_parse.split('\n')
    try:
        for j in range(0, 3):
            if text_to_parse_split[j].isnumeric() is False and \
                    re.search('[a-zA-Z]', text_to_parse_split[j]) is not None:
                names.append(text_to_parse_split[j])
        return names
    except IndexError:
        return names


def process_json(path):
    search_objects = []
    files = os.listdir(path)

    for file in files:
        file_path = path + "/" + file
        with open(file_path, "r") as f:
            json_data = json.load(f)
        search_objects.append(extract_data(json_data))

    return search_objects


def extract_data(json_data):
    try:
        search_object = SearchObject()

        try:
            store = json_data[0]['textAnnotations']
            text_to_parse = text_annotations(store)
        except KeyError:
            store = json_data[0]['fullTextAnnotation']
            text_to_parse = full_text_annotation(store)

        phone = get_phone_number(text_to_parse)
        search_object.phone = phone

        names = get_name(text_to_parse)
        search_object.name = names

        return search_object
    except IndexError:
        print("An interesting exception occurred")

    return None
