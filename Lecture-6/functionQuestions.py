

# Q1 : Write a function to print the length of a list. ( List is the parameter)

nums = [2, 3, 4, 6, 7, 8]
cities = ["Sopore", "Baramulla", "Srinagar", "Handwara"]

def print_length(list) :
    print(len(list))

print(len(nums))
print(len(cities))





# Q2 : Write a function to print the elements of a list in a single line (list is the parameter)

nums = [1, 3, 4, 7, 6]

def print_el(list) :

    print(*list)  # * unpack the list to print it in single line 

print_el(nums)
