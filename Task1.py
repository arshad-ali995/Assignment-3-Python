# PROBLEM 1
name = input("Enter name: ")
age = int(input("Enter age: "))
score = int(input("Enter exam score: "))
income = float(input("Enter family income: "))

if age < 16:
    print(name + ", Sorry, too young.")
elif score < 60:
    print(name + ", Exam score too low.")
else:
    if income < 30000:
        print(name + ", Admitted with full scholarship")
    elif income < 80000:
        print(name + ", Admitted with partial scholarship")
    else:
        print(name + ", Admitted without scholarship")