
# CONDITIONAL STATEMENTS
# Conditional statements are used to execute a block of code based on a condition.
# if-elif-else ( syntax )

# if (condition1):
#     statement1
# elif (condition2):
#     statement2
# else:
#     statement


#if statement
age = 20

if (age >= 18 ) :
    print("You can drive")


#if-elif statement

light = "green"

if (light == "red"):
    print("Stop")
elif (light == "green"):
    print("go")
elif (light == "yellow"):
    print("wait")


#if-else statement
age = 10

if (age >= 18 ) :
    print("You can drive")
else:
    print("You can't drive")


# if-elif-else statement

light = "pink"

if (light == "red"):
    print("Stop")
elif (light == "green"):
    print("go")
elif (light == "yellow"):
    print("wait")
else:
    print(light)



# NESTING

# if statement inside if statement


age = 14
if (age >= 18):
    print("You are eligible to drive")
else:
    print("You are not eligible to drive")