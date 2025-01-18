
# Q1: Write aprogram to grade student based on makrs input
# marks >= 90 : A,  90 > marks >= 80 : B,  80 > marks >= 70 : C,  70 > marks D .

marks = int(input("Enter the marks of the student : "))

if (marks >= 90):
    grade = "A"
elif (marks >= 80 and marks < 90):
    grade = "B"
elif (marks >= 70 and marks < 80):
    grade = "C"
else:
    grade = "D"

print("Grade of the student : ", grade)




# Q2 : Write a program to check whether the given number entered by the user is even or odd.

num = int(input("Enter the number : "))

if (num % 2 == 0):
    print("The number is even")
else:
    print("The number is odd")


# Q3 : Write a program  to find the greatest of three numbers entered by the user?

num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))
num3 = int(input("Enter the third number : "))

if (num1 > num2 and num3 ):
    print ("The greatest number is : ", num1)
elif (num2 > num3 and num1):
    print ("The greatest number is : ", num2)
elif (num3 > num2 and num1):
    print ("The greatest number is : ", num3)


# Q4: Write a program to check if a number is multiple of 7 or not ?

num = int(input("Enter the number : "))

if (num % 7 == 0):
    print("The number is multiple of 7")
else:
    print("The number is not multiple of 7")

