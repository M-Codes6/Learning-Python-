
# Q1 : Print the elements of the following list using loop
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for el in nums :
    print(el)



# Q2 : Search for a number X in tuple using loop
# (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = 49

idx = 0
for el in nums :
    if (el == x) :
        print("Found at idx:", idx)
    idx += 1