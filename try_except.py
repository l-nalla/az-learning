user_inp = input("Enter first Name: ")
age = int(input("Enter last name: "))
try:
    print(f"Full Name: "+ user_inp + age)
except Exception as e:
    print(f"Some error occured:  {e}")
# print(f"Full Name: "+ user_inp + age)
print("end")