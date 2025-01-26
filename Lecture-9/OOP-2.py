
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



# Class Method
'''
A class method is bound to the class and recieves the class as an implicit first argument.

Note: Static method can not access or modify class state and generally for utility

class Student:
@classmethod
def college(cls):
pass

'''

class Person:
    name = "Anonymous"

    # def change_name(self, name):
    #     self.__class__.name = "Muzamil"

    @classmethod
    def change_name(cls, name):
        cls.name = name

p1 = Person()
p1.change_name("Muzamil")
# print(p1.name)   
print(Person.name)




# Property
'''
We use property decorator on any method in the class to use the method as a property

'''



# Polymorphism
'''
When the same operator is allowed to have different meaning according to the context.

Operators   and    Dunder functions.

a + b  #addition            a.__add__(b)
a + b  #subtraction         a.__sub__(b)
a + b  #Multiplication      a.__mul__(b)
a + b  #division            a.__truediv__(b)
a + b  #addition            a.__mod__(b)

'''

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    
    def showNumber(self):
        print(self.real,"i +", self.img,"j")

    def __add__(self, num2):                    # Dunder Function
        newReal = self.real + num2.real
        newimg = self.img + num2.img
        return Complex(newReal, newimg)
    
    def __sub__(self, num2):                      # Dunder Function
        newReal = self.real - num2.real
        newimg = self.img - num2.img
        return Complex(newReal, newimg)
    
    def __mul__(self, num2):                       # Dunder Function
        newReal = self.real * num2.real
        newimg = self.img * num2.img
        return Complex(newReal, newimg)
    
    def __truediv__(self, num2):                   # Dunder Function
        newReal = self.real / num2.real           
        newimg = self.img / num2.img
        return Complex(newReal, newimg)
    
    def __mod__(self, num2):                        # Dunder Function
        newReal = self.real % num2.real
        newimg = self.img % num2.img
        return Complex(newReal, newimg)
    
num1 = Complex(1, 3)
num1.showNumber()

num2 = Complex(2, 6)
num2.showNumber()

num3 = num1 + num2
num3.showNumber()

num4 = num1 - num2
num4.showNumber()
        
num5 = num1 * num2
num5.showNumber()

num6 = num1 / num2
num6.showNumber()

num7 = num1 % num2
num7.showNumber()