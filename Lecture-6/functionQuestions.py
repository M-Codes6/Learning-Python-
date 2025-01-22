

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





# Q3: Write a function to find the factorial of n. (n is the parameter)

def cal_fact(n) :

    fact = 1

    for i in range (1, n+1) :

        fact *= i

    print(fact)

cal_fact(5) 






# Q4 : Write a function to convert USD into INR


def converter(usd_val) :
    inr_val = usd_val * 83   # bcz 1 usd = 83rs

    print(usd_val, "USD =", inr_val, "INR")
    
converter(3)




# Q5: Write a function in which it takes input and if the number is odd it will return string "ODD" other wise if even i will return string "EVEN"

            # One way to solve

num = int(input("Enter the number :"))

def func(n) :
    if(n % 2 == 0) :
        return "EVEN"

    else:
        return "ODD"


print(func(num))


         # Another way to solve 
         

def func(n) :
    if(n % 2 == 0) :
        return "EVEN"

    else:
        return "ODD"

num = int(input("Enter the number :"))

print(func(num))
    

