class Employee:
    def __init__(objectname):
        objectname.eName=""
        objectname.eSal = 0
        objectname.eDesignation = ""
        objectname.eLocation = ""

    def setdetails(objectname,name,sal,desig,loc):
        objectname.eName = name
        objectname.eSal = sal
        objectname.eDesignation = desig
        objectname.eLocation = loc

    def setName(objectname,name):
        objectname.eName = name
    
    def setSal(objectname,sal):
        objectname.eSal = sal
    
    def setDesignation(objectname,designation):
        objectname.eDesignation = designation

    def setLocation(objectname,location):
        objectname.eLocation = location

    def display(objectname):
        print(objectname.eName)
        print(objectname.eSal)
        print(objectname.eDesignation)
        #print(objectname.eLoction)

Emp = Employee()
Emp.setdetails("Swetha",8000,"pydev","TN")
Emp.display()
#print(Emp.eLocation)