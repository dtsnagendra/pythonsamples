
# Constructors and Destructors

#Constructors
# - will be called at the time of Object creation.
# - used to intialize the data members with default data.
# - used to initialise the object's members with some given data.

#Destructors
# - used to free the memory allocation
# - used to close the resources allocated to the current object.
# - will be called automatically when the current object goes out of scope


class Employee:
    name = "No-Name" # Class variables/members
    __address = "USA"  #private class member
    __empcount = 0

    def __init__(self, name= 'No Name', salary = 1000): #constructor
        print("Constructor called ...")
        self.name = name #instance/object members
        self.designation = ""
        self.salary = salary
        Employee.__empcount += 1
        #Employee.name = "Siva"
        #print(f"name is {self.name} , designation {self.designation}, salary {self.salary}")       
    
    def __del__(self):
        print(f"Destructor called ... {self.__class__}")
    
    def setDetails(self, name, desg,sal):
        self.name = name
        self.designation = desg
        self.salary = sal

    def DisplayDetails(self):
        print(f"name is {self.name} , designation {self.designation}, salary {self.salary}")


e = Employee("Swetha", 50000)
e.DisplayDetails()
print(e._Employee__empcount)

print(Employee.name)
print(e._Employee__address)
p = Employee()
print(e._Employee__empcount)

q = Employee()
print(e._Employee__empcount)

'''
OOPS
- classes objects
- class members
- instance members
- methods in class
- constructor and destructor

- inheritance
- operator overloading 
'''