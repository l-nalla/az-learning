# sample = open('/workspaces/az-learning/Functions/sample.txt', 'r')

# # sample_text = """this is a sample text\n for testing multiline with open() function"""
# # sample.write(sample_text)

# print(sample.read())

# sample.close()


with open('/workspaces/az-learning/Functions/sample.txt', 'r') as file:
    print(file.readlines())