import random as ran

def write_to_file(filepath):
    content = ""

    for i in range(1001):
        content += str(ran.random()) + str(i) + '\n'
    
    with open(filepath , 'w') as sample_text_file:
        sample_text_file.write(content)
    
    return filepath

def read_from_file(filepath):
    with open(filepath, 'r') as read_file:
        print(read_file.readlines())


written_file_path = write_to_file("/workspaces/az-learning/FileHandling/sample_text.txt")

read_from_file('/workspaces/az-learning/FileHandling/sample_json.json')

