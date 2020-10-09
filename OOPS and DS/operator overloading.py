

#OOPS - Object Oriented Programming System
# deals with Classes & Objects
# Class - its a user defined type, contains methods(behaviours), members(properties)
# Object - its an instance to the Class (xerox copy for a Class)

# Data Abstraction - members/methods 
# Data Hiding / Encapsulation
# Inheritance - Single, Multiple, Multi level, Hybrid
# Polymorphism - Operator Overloading / Method over loading

# + - to add to integers/floats/strings/ complex numbers
# i want to add 2 objects
#x = 10
#y = 'india'
#c = x + y

# Operator Overloading
class A:
    def __init__(self,a=0, b=0):
        self.x = a
        self.y = b

    def __add__(self,other):
        pass
        #print(f"values ({self.x},{other.x}) ({self.y},{other.y})")
        #x = self.x +  other.x
        #y = self.y + other.y
        #return A(x,y)
    
    def __str__(self): # object in string representation
          return f'({self.x},{self.y})'

loca = "US"
a = A(1020)
b = A(80)
#1100$
amount = a + b
#print(c)
INR 
'''
* - __mul__  = c = a*b
- - __sub__ - c = a-b
/ - __truediv__
__pow__  - **
__floordiv__ - //
__mod__ %

__lt__ - < - c = a<b
__le__ - <=
__gt__
__ge__
__eq__

__rshift__ - p3 = p1 >> p2
__lshift__
__and__
__or__
__xor__

'''
