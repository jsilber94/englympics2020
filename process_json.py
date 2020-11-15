import json
import re
from SearchObject import SearchObject


def text_annotations(store):
    return store[0]["description"]


def full_text_annotation(store):
    return store["text"]


def get_phone_number(text_to_parse):
    reg = re.compile("(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}")
    phone = reg.search(str(text_to_parse))
    if phone is None:
        return re.search("XXX-XXX-XXXX", text_to_parse)
    return phone


def get_name(text_to_parse):
    names = []
    text_to_parse_split = text_to_parse.split('\n')
    try:
        for j in range(0, 3):
            if text_to_parse_split[j].isnumeric() is False and \
                    re.search('[a-zA-Z]', text_to_parse_split[j]) is not None:
                names.append(text_to_parse_split[j])
        return names
    except:
        return names


def process_json():
    search_objects = []

    for i in range(1, 21):
        try:
            with open("data/Training Json/j" + str(i) + ".json", "r") as f:
                json_data = json.load(f)

            search_object = SearchObject()

            try:
                store = json_data[0]['textAnnotations']
                text_to_parse = text_annotations(store)
            except KeyError:
                store = json_data[0]['fullTextAnnotation']
                text_to_parse = full_text_annotation(store)

            phone = get_phone_number(text_to_parse)
            search_object.phone = phone if phone is None else phone.group()

            names = get_name(text_to_parse)
            search_object.name = names

            search_objects.append(search_object)
        except IndexError:
            print("An interesting exception occurred")
        except:
            print("An exception occurred")

    for search_object in search_objects:
        print(search_object.phone)
        print(search_object.name)
        print("----------------------")

    return search_objects


process_json()
