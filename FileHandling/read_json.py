import json

def read_file_as_json(filepath):
    with open(filepath, 'r') as json_content:
        data = json.load(json_content)
    return data

def retrieve_from_json(json_object, key):
    static_dict = json_object["glossary"]
    glass_div = static_dict["GlossDiv"]

    return static_dict[key], glass_div['title']




data = read_file_as_json('/workspaces/az-learning/FileHandling/sample_json.json')


print(retrieve_from_json(data, 'title'))