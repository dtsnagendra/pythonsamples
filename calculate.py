class cal:
    def __init__(objectname, x, y):
        objectname.x= x
        objectname.y = y

    def add(objectname):
        return objectname.x + objectname.y

    def sub(objectname):
        return objectname.x - objectname.y

    def mul(objectname):
        return objectname.x * objectname.y

    def div(objectname):
        return objectname.x / objectname.y

  
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
value=cal(x,y)
select = 1
while select!= 0:
    print("0. Exit")
    print("1. Add")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    select = int(input("Select the option: "))
    if select==1:
        print("Result: ",value.add())
    elif select==2:
        print("Result: ",value.sub())
    elif select==3:
        print("Result: ",value.mul())
    elif select==4:
        print("Result: ",round(value.div(),2))
    elif select==0:
        print("Exit!")
    else:
        print("Invalid select!!")
 