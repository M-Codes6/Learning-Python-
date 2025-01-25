
# Q1: Create a student class that takes name and marks of 3 subjects as arguments in constructor. Then create a method to print the average

class Student:

    def __init__(self, name, marks):
        self.name = name 
        self.marks = marks
    
    def avg(self):
        avg = sum(self.marks) / len(self.marks)
        return avg
    
s1 = Student("Muzamil", [90, 80, 88])
print(s1.name, s1.marks)
print("Average Marks", s1.avg())



# Q2 :  Create Account class  with 2 attributes - balance and account no. Create Methods for debit, credit and printing the balance

class Account:
    def __init__(self, bal, acc_no):
        self.balance = bal
        self.acc_no = acc_no
    
    def debit(self, amount):
        self.balance -= amount
        print("Rs:", amount,"was debited from your account")
        print("Total balance =", self.get_balance())
    
    def credit(self, amount):
        self.balance += amount
        print("Rs:", amount,"was credited to your account")
        print("Total balance = ", self.get_balance())
    
    def get_balance(self):
        return self.balance
        

acc1 = Account(25600000, "xxxxx456")

acc1.debit(50000)   
acc1.credit(70000) 
print(acc1.get_balance())


        