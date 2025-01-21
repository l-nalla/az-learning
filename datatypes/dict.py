person = {
    "Name": "Jhon",
    "age": 30,
    "heights": 5.8,
    "weight": 150
}

print(type(person))

print(person)

print(person["age"])

# I want to update the name of the person
person["Name"] = "James"

print(person)

# I wanted to add one more attribute to the dict 
person.update({"Gender": "Male"})

print(person)

# I want to find all keys in the dict
keys = person.keys()

print(f"keys in the dictionary: {keys}")

person.clear()
print(person)