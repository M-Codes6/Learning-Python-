

# Q1: Write a recursive function to calculate the sum of first n natural numbers ?

def calc_sum(n):
    if (n == 0):
        return 0
    return calc_sum(n-1) + n

sum = calc_sum(5)
print(sum)





# Q2: Write a recursie function to print all elements in a list (Hint: use list and index as a parameter)


def print_el(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_el(list, idx+1)

fruits = ["mango", "apple", "banana", "orange"]

print_el(fruits)