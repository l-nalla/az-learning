# **kwargs keyword arguments that are passed to python function, we can n number of key word args when **kwargs specified 

def person(**person):
    print(type(person))
    print(person.keys())
    print(person.values())
    # print(person['age'])
    person_details = f"{person.get('name')}, , his/her age is {person.get("age")}, weights about {person.get("weight")}"
    
    return person_details


# calling a function with kwargs
print(person(name="Jhon",  weight= 76))

