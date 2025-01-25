
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
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

s1 = Student("M-Codes6", 80)
print(s1.name, s1.marks)


class Car:
    def __init__(self, newcar):
        self.name = newcar
    
car1 = Car("Punch")
print(car1.name)

car2 = Car("Curv")
print(car2.name)



# Default constructor

class Subject:
   def __init__(self):
       pass
   

# Parameterized Constructor

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks




'''
Class and Instance(object) Attributes :

class.attr
obj.attr
'''


# Methods 

''' Methods are functions that belong to objects
 # Creating class
    
 class Student:
    def __init__(self, name):
    self.name = name 

    def hello(self):
    print("hello", self.name)
s1 = Student("Muzamil")
s1.hello
 '''


class Student:
    def __init__(self, name, marks):
        self.name = name 
        self.marks = marks

    def hello(self):
        print("hello", self.name)
    
    def get_marks(self):
        return self.marks
        
s1 = Student("Muzamil", 80)
s1.hello()
print(s1.get_marks())    






# Static Methods 

'''  Methods that don't  use the self parameter(work at class level)

class Student  :
@static method    #decorator
def college():
    print("ABC College")

    
Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function
without permanently modifying it ..

''' 

class Student:
    @staticmethod
    def college():
        print("ABC College")

Student.college()




# IMPORTANT

'''
Abstraction : Hiding the implementation details of a class and only showing the essential 
            features to the user

            
Encapsulation : Wrapping data and functions into a single unit(object)

'''