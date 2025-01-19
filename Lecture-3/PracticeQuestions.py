
# Q1: Write a program to ask the user to enter names of their 3 favourite movies and store them in a list ?

movies = [(input("Enter your 1st favourite movie: ")), (input("Enter your 2nd favourite movie: ")), (input("Enter your 3rd favourite movie: "))] 
print(movies)


# Q2 : Write a program to ask the user to enter names of their 3 favourite movies and store them in a tuple ?

movies = ((input("Enter your 1st favourite movie: ")), (input("Enter your 2nd favourite movie: ")), (input("Enter your 3rd favourite movie: ")))
print(movies)



# Q3: Write a program to check if a list containing a palindrome of elements ? (palindrome means that can read the same from left to right and right to left)

list = [1, 2, 1]

copy_list = list.copy()
copy_list.reverse()

if (list == copy_list):
    print("Palindrome")
else:
    print("Not Palindrome")



# Q4 : Write a program to count the number of students with the "A" grade in the following tuple?
# grades = ("C", "D", "A", "A", "B", "B", "A")
# store the above values in a list and sort them from "A" to "D"

grades = ("C", "D", "A", "A", "B", "B", "A")
print(grades.count("A"))

list = list(grades)
list.sort()
print(list)


# Q4 : Write a program to create a list of 5 elements and then remove the 3rd element from the list ?

list = [1, 2, 3, 4, 5]
list.pop(3)
print(list)

# Q5 : Write a program to insert a new element at the 2nd index of the list ?

list = [1, 2, 3, 4, 5]
list.insert(2, 6)
print(list)

# Q6 : Write a program to create a list of 5 elements and then sort the list in ascending order ?

list = [5, 4, 3, 2, 1]
list.sort()
print(list)

# Q7 : Write a program to create a list of 5 elements and then reverse the list ?

list = [1, 2, 3, 4, 5]
list.reverse()
print(list)

# Q8 : Write a program to create a list of 5 elements and then find the index of the element "3" ?

list = [1, 2, 3, 4, 5]
print(list.index(3))