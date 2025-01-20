
# SETS IN PYTHON

num = {1, 2, 3, 4}

print(num)
print(type(num))


# SET METHODS

num = {1, 2, 3, 4}

num.add(5) # adds an element to the set
print(num)

num.remove(3) # removes an element from the set
print(num)

num.clear() # removes all the elements from the set
print(num)

collection = {"apple", "banana", "cherry"}
print(collection.pop()) # removes the last element from the set


num = {1, 2, 3, 4}
collection = {"apple", "banana", "cherry"}

print(num.union(collection)) # returns a set containing the union of sets

num = {1, 2, 3, 4, 5, 6}
num1 = {4, 5, 6, 7, 8, 9}

print(num.intersection(num1)) # returns a common values in set
