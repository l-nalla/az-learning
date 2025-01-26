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



# args 
print(greet(), "world")

# args - arguments, *args, **kwargs
# *args is going to be a collection of arguments 

# Example

# sum of any number of values which given to function

def sum_of_any_vals(*vals):

  sum = 0
  for i in vals:
    if isinstance(i, int):
      sum += i
  return sum

print(f"Sum of all arguments passed to function {sum_of_any_vals(1,2,3,'ni',6,6)}")

# combination normal args and *args
def test_normal_args_and_starargs(sum, *vals):
  initial_sum = sum
  for i in vals:
    sum += i
  return f"sum of all values passed to function is {sum} and initial value of sum is {initial_sum}"

print(test_normal_args_and_starargs(0, 1,2,3,4,5,6,7,7,8))

