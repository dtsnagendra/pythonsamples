class Bank:
    name=""
    code = ""
    location = ""
    accounttypes = []

    def setdetails(objectname,name,code,loc,acc):
        objectname.name = name
        objectname.code = code
        objectname.location = loc
        objectname.accounttypes = acc

    def setName(objectname,name):
        objectname.name = name
    
    def setcode(objectname,code):
        objectname.code = code

    def setLocation(objectname,location):
        objectname.location = location

    def setAccountTypes(objectname,accounttypes):
        objectname.accounttypes = accounttypes

    def display(objectname):
        print(objectname.name)
        print(objectname.code)
        print(objectname.location)
        print(objectname.accounttypes)

bnk = Bank()
bnk.setdetails("SBI", "SBI001", "Hyd",["SavingAccount","personalAccount","currentAccount"])
bnk.display()

