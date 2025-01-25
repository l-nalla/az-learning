#structure
def function_name():    #function defination, we might define some parameters that passed as input to function
  print("this block is under function_name function")
  print("this is another line")                            #we use arguments while calling a function whether it could be built in or user defined 


# print("this is not inside function block")

# function_name()     #function call


# function with parameters 
def sum_of_list(list_of_vals, sum): # function with parameter, list_of_vals is the parameter for the function
  for i in list_of_vals:
    sum += i
  return f"sum of list_of_vals is {sum}"



# sum_of_list(sum=0, list_of_vals=[2,3,5,7]) # parameter based indexing
print(sum_of_list([2,3,5,7], 0)) # position based argument passing


def greet():
  return "Hello!"

# print(greet(), "world")