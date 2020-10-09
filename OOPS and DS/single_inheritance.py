

#Inheritance.
# - One of the important oops concepts

# more than one class will be involved

# person - name, age, gender, move, talk, eat, run, sleep
# father (person) : employed, haskids, ismarried

# parent - 8
# father - 8 + 3 = 11
# grandfather (person) - 8 + 4 
# Employee (person) - 8 + 3  


# Parent / Base 
# Child / Sub
'''
class Parent:
    def set(self, a):
        print("into parent set method")
        self.x = a
        print(self.x)

#class <childclass>(<baseclass>):
class Child(Parent):
    def set(self, b,c):
        print("into child's set method")
        self.y = b
        print(self.y)
        super().set(c)

c = Child()
c.set(22,10) 
#method overriding
# how to call methods in super class 
#c.set(10)
'''
#Single Inheritance - one parent clas and one child class
#Multiple Inheritance - more than one parent class, one child class
#Muti level Inheritance - each class will be either a parent or child

class Person:
      def __init__(self,a):
          print("Person constr called ...")
          self.p = a
          print(self.p)
      def set_name(self, n):
          print(f"Name of Person is {n}")

class Father(Person):
    def __init__(self,x,y):
        super().__init__(x)
        print("Father constr called ...")
        self.b = y
        print(self.b)

    def set_father_address(self, add):
         print(f"address of father is {add}")

x = 10
y = 20 

f = Father(x,y)

BankAccount - AcctType, BankCode, BankAddr,Balance
#Customer - Cname, cAddr,Cage, Cgender

- SAccount- Custname, caddress, Cage - minbalance 5000
- CurrentAccount - Custname, caddress, cage,minbalance 100000

SAccount ( BankAccount)
- list of customers

CAccount ( BankAccount)
- list of customers

create the account
display accounts
withdraw
deposit
displaybalance - display balance based on account type
exit




