# 1.Write a Python program that takes an integer as input and prints whether it is even or odd.

number=int(input("enter a number: "))
if (number%2)==0:
    print("{0} is even number".format(number))
else:
    print("{0} is odd number".format(number))



# ---------------------------------------------------------------------------------------------------------------------------------------------

# 2.Write a program that takes two numbers as input and prints the larger number. If they are equal, print "Both numbers are equal".

num1=int(input("Enter first number : "))
num2=int(input("enter second number : py "))
if num1>num2:
    print(num1, "is largest number")
elif num2>num1:
    print(num2, "is largest number")
else:
    print("both numbers are equal")



# ---------------------------------------------------------------------------------------------------------------------------------------------

# 3.Write a Python program that asks the user for a number and prints whether it is positive, negative, or zero.

number=int(input("Enter a number"))
if number>0:
    print("positive")
elif number==0:
    print("zero")
else :
    print("negitive")


# ---------------------------------------------------------------------------------------------------------------------------------------------

# 4.Write a program that asks the user for their age. If the age is 18 or above, print "You are eligible to vote", otherwise print "You are not eligible to vote".

Age=int(input("enter your age : "))
if Age>=18:
    print("You are eligible to vote")
else :
    print("You are not eligible to vote")

# ---------------------------------------------------------------------------------------------------------------------------------------------
# 5.Write a program that takes a student's marks (out of 100) and prints:
# "Pass" if marks are 40 or more
# "Fail" if marks are less than 40

student_marks=int(input("enter student marks : "))
if student_marks>40:
    print("pass")
elif student_marks==40:
    print("pass")
else:
    print("fail")


