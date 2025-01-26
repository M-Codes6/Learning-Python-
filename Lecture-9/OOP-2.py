
# del Keyword
'''  
used to delete object properties or object itself 

del s1.name 
del s1
'''

class Student :
    
    def __init__(self, name):
        self.name = name
        
    
s1 = Student("Muzamil")
del s1.name



# Inheritence

'''
When one class(child/derived) derives the properties and methods of another class (Parent/base)
class Car:
.....

class ToyotaCar(Car):
...

'''


class Car:
    @staticmethod
    def start():
       print("Car started...")

    @staticmethod
    def stop():
       print("Car stopped.")

class TataCar(Car):
    def __init__(self, name):
        self.name = name

car1 = TataCar("Punch")
car2 = TataCar("Curv")

print(car1.name)
print(car1.start())


# Types of inheritence
'''
Single , Multi-level, Multiple
'''

# Single


class Car:
    @staticmethod
    def start():
       print("Car started...")

    @staticmethod
    def stop():
       print("Car stopped.")

class TataCar(Car):
    def __init__(self, name):
        self.name = name

car1 = TataCar("Punch")
car2 = TataCar("Curv")

print(car1.name)
print(car1.start())



# Multi-level


class Car:
    @staticmethod
    def start():
       print("Car started...")

    @staticmethod
    def stop():
       print("Car stopped.")

class TataCar(Car):
    def __init__(self, brand):
        self.brand = brand

class Punch(TataCar):
    def __init__(self, type):
        self.type = type

car1 = Punch("Petrol")
car1.start()


# Super Method
# super() method is used to access methods of the parent class



class Car:

    def __init__(self, type):
        self.type = type
        
    @staticmethod
    def start():
       print("Car started...")

    @staticmethod
    def stop():
       print("Car stopped.")

class TataCar(Car):
    def __init__(self, name, type):
        self.name = name
        super().__init__(type)

car1 = TataCar("Punch", "Petrol")
print(car1.type)