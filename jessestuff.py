import json
import re


class SearchObject:
    phone = ""
    name = []


searchObjects = []

for i in range(1, 21):

    with open("data/Training Json/j" + str(i) + ".json", "r") as f:
        json_data = json.load(f)

    store = json_data[0]['textAnnotations']

    reg = re.compile("(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}")
    phone = reg.search(str(store))
    if phone is None:
        phone = re.search("XXX-XXX-XXXX", str(store))

    searchObject = SearchObject()
    searchObject.phone = phone if phone is None else phone.group()


    searchObjects.append(searchObject)

for searchObject in searchObjects:
    print(searchObject.phone)
#     print(searchObject.name)
