

# Q1 : Print numbers from 1 to 100

num = 1

while num <= 100 :
    print(num)
    num += 1



# Q2 : Print numbers from 100 to 1

num = 100

while num >= 1 :
    print(num)

    num -= 1




# Q3: Print a multiplication table of a umber n with user input

n = int(input("Enter number:"))
i = 1 
while i <= 10 :
    print(n * i)

    i += 1




# Q4 : Print the elements of the list using a Loop 
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

idx = 0

while idx < len(nums) :
    print(nums[idx])

    idx += 1


# Q5: Search for a number X in this tuple
# (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = 49
idx = 0 

while idx < len(nums) :
    if (nums[idx] == x) :

        print("Found at idx:", x)

    idx += 1