# voting age > 18
age = int(input("Enter age: "))



if age < 1 or age > 100:
    print("you entered a invalid age, age should be between 1-100")
elif age > 18 :
    print("you can vote!!!")
elif age == 18:
    print("you are ready to register for vote!!")
else:
    print("You are still not 18 you can not vote!!")