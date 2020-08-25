


#OOPS - Object Oriented Programming System

# Classes & Objects
# what is class ? 
# - user defined type 
# - it will have data members, methods
# - any number of objects can be created for a class.
# - data in the data members is different for each object.
# - methods present in the class can be shared across objects.


#private - data members, methods can not be accessed outside of class.
#public - data members , methods can be accessed outside of class.

class Person:
  name = "noname"
  age = 0
  __address = "INDIA"

  def setDetails(swetha, na, ag, loc):
      swetha.name = na
      swetha.age = ag
      swetha.location = loc

  def setName(swetha, na):
    swetha.name = na
    swetha.location = "India"

  def setAge(self, ag):
    self.age = ag

  def getAge(self):
      return self.age
 
 #<obj> = <classname>
p1 = Person()

#<obj>.<membername>
p1.setDetails("Hari",23,"mumbai")
print(p1.name)
print(p1.location)
print(p1.age)
print(Person.name)
print(Person.age)
print(p1._Person__address)


'''
p2 = Person()
p2.setDetails("Swetha",22,"India")

p2.setName("Swetha")
print(p2.name)
print(p2.location)
print(p2.age)
print(p1.getAge())
'''
#list of Employee Objects

# list display
#print(p1.location)

# Data Abstraction

# Inheritance

# Polymorphism
