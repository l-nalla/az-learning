student_name = input("Enter Student Name: ")
math_marks = input("Enter Marks for Math subject: ")
science_marks = input("Enter Marks for science subject: ")

if math_marks.isdigit() and science_marks.isdigit():
    final_marks = int(math_marks) + float(science_marks)
    print(f"student {student_name} scored total of {final_marks}")
else:
    print("there is an issue input values for math_marks or science_marks, these values should be integers.")



if int(math_marks) > 50:
    print(f"student {student_name} score marks greater than 50 passed with distinction")
else:
    print(f"student {student_name} scored marks less than 50")


