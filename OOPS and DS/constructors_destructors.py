
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
    def __init__(self, name= 'No Name', salary = 1000): #constructor
        print("Constructor called ...")
        self.name = name
        self.designation = ""
        self.salary = salary
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

e.setDetails("Harish", "Manager",50000)
e.DisplayDetails()

#print(f"name is {e.name} , designation {e.designation}, salary {e.salary}")
del e

e2 = Employee()
e2.DisplayDetails()
#print(f"name is {e2.name} , designation {e2.designation}, salary {e2.salary}")


