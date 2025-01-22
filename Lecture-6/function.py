
# Funtions in Python 

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))

def sum(a, b) :

    sum = a + b

    return(sum)

print(sum(a, b))

# another eg

def cal_sum (a, b) :   

    sum = a + b

    return sum 

print(sum(2, 3))



# Write a function to calculate average of 3 numbers

def cal_avg(a, b, c) :

    sum = a + b + c

    avg = sum / 3

    return(avg)

print(cal_avg(2, 4, 3))





# Function Types 

# Built-in : print(), len(), type(), range() etc..
# User-defined : not built-in , written by users


# Default parameters : Assigning a default value to parameters which is used when no argument is passed

