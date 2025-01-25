
# OOP : to map with real world scenarios we started using objects in code

# Class and Object 

# Class : it is a blueprint for creating objects .

'''e.g'''

    # creating class
class Student :
    name = "Muzamil"

    #creating object (instance)

s1 = Student
print(s1.name)


class Car :
    color ="Black"
    mode = "Manuall"

car1 = Car
print(car1.color)
print(car1.mode)


# __init__ function

''' 
Constructor : All classes have a function called __init__(), which is always executed when the
              object is being initiated


# Creating Class

class Student:
def __init__(self, fullname):
        self.name = fullname


# creating object

s1 = Student()
print(s1.name)


The self parameter is a refrence to the current instance of the class, and is used 
to access variables that belongs to the class.

'''


class Student:
    def __init__(self, fullname):
        self.name = fullname

s1 = Student("M-Codes6")
print(s1.name)


class Car:
    def __init__(self, newcar):
        self.name = newcar
    
car1 = Car("Punch")
car2 = Car("Curv")
print(car1.name)
print(car2.name)
