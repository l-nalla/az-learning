# list data type

#array it stores similar dtypes
arr = [1,2,3,4, 2.4]
print(type(arr))

arr2 = ['jhon', 12, 20.3]

print(type(arr2))

print(arr2)


# list operations
length = len(arr)
print(f"length of arr: {length}")

#List follows index based access and index starts with 0 to len(list)-1, [1,2,3,4, 2.4] I want to access element 4
print(arr[3])


# I want to update value 4 to 10 
print(f"arr before assignment: {arr}")
arr[3] = 10

print(f"array after assignment {arr}")


# I want to access part of array [1, 2, 3, 10, 2.4] slicing array 
# array slicing gets values until end index-1
print(f"accessing values from 1-3: {arr[1:4]}")

sorted_arr = sorted(arr)
print(f"sorted array {sorted_arr}")

sample1 = "jhon"
print(sorted(sample1))

# I wanted to add some element to arr at end
arr.append(0.9)

print(arr)

# I wanted to add another list to existing list
print(f"array 1 {arr}")
print(f"array 2 {arr2}")

#arr3 = combination of arr and arr2
arr3 = arr + arr2
print(f"arr3 : {arr3}")

arr.extend(arr2)

print(f"arr4 {arr}")

print(arr.pop()) # pop 

print(arr)