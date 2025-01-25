
# Q1: Create a student class that takes name and marks of 3 subjects as arguments in constructor. Then create a method to print the average

class Student:

    def __init__(self, name, sub1, sub2, sub3):
        self.name = name 
        self.submarks = sub1, sub2, sub3 
    
    def avg(self):
        avg = sum(self.submarks) / 3
        return avg
    
s1 = Student("Muzamil", 90, 80, 88)
print(s1.name, s1.submarks)
print("Average Marks", s1.avg())