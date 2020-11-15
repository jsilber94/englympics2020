import os

def parse_json(path):
  print("path: " + path)

  files = os.listdir(path)
  print(files)

  for file in files:
      file_path = path + "/" + file
      get_supplier(file_path)


  return "Couche Tard"


def get_supplier(file_path):
    print(file_path)