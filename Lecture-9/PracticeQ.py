

# Q1 : Define a Circle class to create a circle with radius r using the constructor.
# Define an Area() method of the class which calculates the area of the circle.
# Define a Perimeter() method of the  class which allows you  to calculate the perimeter of the circle


class Circle:

    def __init__(self, r):
        self.radius = r
    
    def area(self):
        return 3.14 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14 * self.radius


c1 = Circle(7)
print(c1.area())
print(c1.perimeter())




# Q2 :  Define a Employee class with attributs role, department and salary. This class also has a showdetail()
# Method 

class Employee:

    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary
    
    def showDetails(self):
        print("Role:", self.role, "Dept:", self.dept, "Salary:", self.salary)
    

emp1 = Employee("SDE,", "CS,", "20LPA")
emp1.showDetails()




# Q3 : Create an Engineer class that inherits properties from Employee and has additional attributes : name and age


class Employee:

    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary
    
    def showDetails(self):
        print("Role:", self.role, "Dept:", self.dept, "Salary:", self.salary)


class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name 
        self.age = age
        super().__init__("SDE2,", "IT,", "22LPA")
          

eng1 = Engineer("Muzamil", 25)
print("Name:",eng1.name,"Age:", eng1.age)
eng1.showDetails()




# Q4: Create a class called order which stores items and price. Use Dunder function __gt__() to convey that.
# order1 > order2  if price of order1 > price of order2


class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price
    
    def __gt__(self, odr2):   
        return self.price > odr2.price
        


odr1 = Order("Chips,", 30)
print("Item:", odr1.item, "Price:", odr1.price)

odr2 = Order("Dew,", 20)
print("Item:", odr2.item, "Price:", odr2.price)

print(odr1 > odr2)

