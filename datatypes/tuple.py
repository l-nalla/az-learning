# tuple data type tuple is where we store the data which we don't want to change.
# python indexes will start from zero to length(list/tuple) - 1
tup = (1,2,4,6) 

print(type(tup))

print(tup[1])

nums = (8,)
print(type(nums))

tup = tup + (8,)
print(tup)

# similar pop functionality 
print(tup[-1])

print(f"length of tuple: {len(tup)}")