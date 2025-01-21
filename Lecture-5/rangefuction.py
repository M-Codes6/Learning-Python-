
# Range : returns a sequence of numbers starting from 0 bu default and increments by 1 b default and stops before a specified number

num = range(5)

for i in num :
    print(i)


for i in range(5):
    print(i)



a = range(10)

for i in a :
    print(i)


for i in range(10) :
    print(i)



    # PRACTICE QUESTIONS USING FOR AND RANGE


# Q1 : Print numbers from 1 to 100

for i in range(1, 101) :
    print(i)


# Q2 : Print numbers from 100 to 1

for i in range(100, 0, -1) :
    print(i)


# Q3 : Print the multiplication table of a number n

n = int(input("Enter number:"))

for i in range(1, 11) :
    print(i * n)


# Pass Statement
# it  is a null statemnt that doess nothing , used as a placeholder for future code 

for i in range(10) :
    pass