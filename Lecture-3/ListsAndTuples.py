
marks = 68
marks1 = 78
marks2 =  88
marks3 = 98
marks4 = 58

# instead of writing above codee we can use list to store the values

marks = [68, 78, 88, 98, 58]
print(marks)

# Accessing the elements of the list
print(marks[0])
print(marks[1])

# In List we can store different types of data

student = ["Muzamil", 23, 3.5, "AI"]
print(student)
print(type(student))



# List Slicing

marks = [68, 78, 88, 98, 58]
print(marks[0:3]) # output (0 to 2)


# List Methods

list = [1, 2, 3, 4]

list.append(5) # append method is used to add the element in the list at the end [1, 2, 3, 4, 5]

list.insert(2, 6) # insert method is used to add the element in the list at the specific index [1, 2, 6, 3, 4, 5]

list.remove(3) # remove method is used to remove the element from the list [1, 2, 6, 4, 5]

list.pop() # pop method is used to remove the last element from the list [1, 2, 6, 4]

list.pop(2) # pop method is used to remove the element from the list at the specific index [1, 2, 4]

list.sort() # sort method is used to sort the list in ascending order [1, 2, 4]

list.reverse() # reverse method is used to reverse the list [4, 2, 1]

list.index(2) # index method is used to find the index of the element in the list





 # TUPLES IN PYTHON

tup = (1, 2, 3, 4, 5)
print(type(tup))


# Tuple Methods

tup = (1, 2, 3, 4, 5)

tup.count(2) # count method is used to count the number of times the element is present in the tuple

tup.index(2) # index method is used to find the index of the element in the tuple