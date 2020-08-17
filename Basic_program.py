'''
#check the given value +ve or -ve
x=float(input("enter the value :"))
if x>0 :
  print("value is +ve")
elif x<0 :
  print("value is -ve")
else:
  print("value is zero")
_______________________________________________

#check the given numbers are equal or not
a = float(input("Enter the 'a' value :"))
b = float(input("enter the 'b' value :"))
c = float(input("Enter the 'c' value :"))
if a>b and a>c:
  print("a is bigger")
elif b>a and b>c:
  print("b is bigger")
elif c>a and c>b:
  print("c is bigger")
else:
  print("all the values are equal")
_________________________________________-
#find the percentage and grade 
total_marks = float(input("Enter the marks :"))
per = (total_marks/800)*100
print(per)
if per>80:
  print("passed in Destingstion ")
elif per<80 and per>60:
  print("passed in First Class ")
elif per<60 and per>55:
  print("passed in second Class ")
else:
  print("Failed ")
_______________________________________

#sum of given numbers

n = (input("Enter a number :"))
i=1
sum = 0
while i<=int(n):
  sum = sum+i
  i=i+1
print(sum)
_____________________________________
#sum of even numbers and sum of Odd numbers

n = (input("Enter a number :"))
sumeve = 0
sumodd = 0
i=1
while i<=int(n):
    if i%2==0:
        sumeve = sumeve+i
    else:
        sumodd = sumodd+i
    i=i+1    
print(sumeve)
print(sumodd)
_________________________________
 For loop
#sum of given numbers

n = (input("Enter a number :"))
i=1
sum = 0
for i in range (1,int(n)):
  sum = sum+i
  i=i+1
print(sum)
_________________________________________
#sum of even numbers and sum of Odd numbers

n = int(input("Enter a number :"))
sumeve = 0
sumodd = 0
i=1
for i in range (1,n):
    if i%2==0:
        sumeve = sumeve+i
    else:
        sumodd = sumodd+i
    i=i+1    
print(sumeve)
print(sumodd)
__________________________________________
#squr of odd number from 1 to 10
n=10
i=1
while i<=n:
  if i%2!=0:
   a=i**2
   print(a)
  i+=1
______________________________________
n = 1
while n>0 :
  n = int(input("Enter the number "))
  if n>0:
    a=n**2
    print(a)
  else:
    print("Enter the +ve number ")

______________________________________________
pi=3.14

go=1
while (go==1):
  print("1=areaofcircle\n2=areaofrectangle\n3=areaofsqur\n4=simpleinterest\n5=addition\n6=substraction\n7= area of the triangle")
  option=int(input("Enter the option :"))
  if option==1:
    r=int(input("Enter the radius : "))
    value=pi*r*r
    print(value)
  elif option==2:
    w = int(input("Enter the width : "))
    l = int(input("Enter the length : "))
    value = w*l
    print(value)
  elif option==3:
    a = int(input("Enter the area : "))
    value = a**2
    print(value)
  elif option==4:
    p = int(input("Enter the principal amount : "))
    r = int(input("Enter the rate of interest : "))
    t = int(input("Enter the number of years : "))
    value = (p*r*t)/100
    print(value)
  elif option==5:
    a =int(input("Enter the 1st number : "))
    b = int(input("Enter the 2nd number : "))
    value = a+b
    print(value)
  elif option==6:
    a =int(input("Enter the 1st number : "))
    b = int(input("Enter the 2nd number : "))
    value = a-b
    print(value)
  elif option==7:
    h = int(input("Enter the height : "))
    b = int(input("Enter the base : "))
    value = h*(b/2)
    print(value)
  else:
    print("Choose the right option")
  con = input("Do you want to continue y/n : ")
  if con == "Yes" or con =="Y" or con =="y" or con =="yes" :
    pass
  else:
    go = 0
    print("Thank you")
  
________________________________________________________________________________
#half pyiramid
n=int(input("Enter the number :"))
a=input("Enter the char :")
for i in range(1,n+1):
  for j in range(1,i+1):
    print(a,end='\t')
  print('\n')
 ____________________________________________________________
#count the vowels in the given statement
n = input("Enter the statement :")
count=0
for i in n:
  if i in ("a","e","i","o","u"):
    count=count+1
print(count)
_______________________________________
#whether given char or str in the statement

n = input("enter the statement :")
v = input("Enter the string or char :")
print(v in n)
________________________________________________
#print the lower cas and upper case in the given statement
r = input("enter the statement :")
v = r.upper()
e = r.lower()
m = r.swapcase()
p =r[::-1]
print(e)
print(v)
print(m)
print(p)
_____________________________________________________________________


#check whether the char or string is palindrom or not
n = input("enter the char or string :")
if(n == n[::-1]):
   print("The given char or string is palindrom")
else:
   print("the given char or string is not palindrom ")
 __________________________________________________________________________
def add():
    a = float(input("enter the first value :"))
    b = float(input("enter the sec value :"))
    print("sum is {}".format(a+b))

add()
_________________________________________
def sub():
   print("subtraction is {}".format(a-b))
a = float(input("enter the first value :"))
b = float(input("enter the sec value :"))
sub()
_____________________________________
def mul(a,b):
   print("multipication is {}".format(a*b))
a = float(input("enter the first value :"))
b = float(input("enter the sec value :"))
mul(a,b)
______________________________________________
def power():
    a = 4
    b = 3
    print("power is {}".format(a**b))

power()
________________________________________
def dev(a,b):
   print("devision is {}".format(a/b))

dev(4,3)
________________________________________________
def comp(a,b):
    if a>b:
        print("a is greater than b")
    else:
        print("b is greater than a")
        
a = float(input("enter the first value :"))
b = float(input("enter the sec value :"))

comp(a,b)
_____________________________________
def comp():
    if a==b:
        print("a and b are equal")
    else:
        print("a and b are not equal")
        
a = input("enter the first string :")
b = input("enter the sec string :")

comp()
_________________________________________
def comp():
    a = "python"
    b = "google"
    if a==b:
        print("a and b are equal")
    else:
        print("a and b are not equal")
        
comp()
____________________________________________
Read a string from User, calculate length of each word in a string and display it.
n = input("enter the string :")
y = len(n)
p = n.split(" ")
for i in p:
    print(len(i))
___________________________________________
Read a string from User, remove all vowels from each word of the string and display
v = 'aeiouAEIOU'
n = input("Enter a string : ")
p = n
for i in n:
    if i in vowels:
        p = p.replace(i,"")
print(p)
_______________________________________________
Read a string from User, convert first letter of each word to upper case, if its already in upper case, convert that to lower case.

n = input("enter the string :")
p = n.split(" ")
print(p)
new_str = " "
for i in p:
    y = i.title()
    new_str = new_str +" "+y
print(new_str)
_________________________________________________
Read a string from User, convert each vowel of a string to upper case

n = input("Enter a string : ")
v = 'aeiouAEIOU'
for i in n:
    if i in v:
        n = n + i.swapcase()
    else:
        n = n + i
print(n)
_________________________________________________"Funtions"___________________________________________
create functions for areaofcircle, areaofsquare, areaofrectangle, simpleinterest execute check the inputs against invalid inputs
 e.g if he enters zero, you should ask user to enter value greater than zero and calculate. you should not leave that method till he enters the value greater than zero. 
def areaofcircle():
    pi = 3.14
    r=int(input("Enter the radius : "))
    value=pi*r*r
    print(value)
    
def areaofsqur():
    a = int(input("Enter the area : "))
    value = a**2
    print(value)
    
def areaofrectangle():
    w = int(input("Enter the width : "))
    l = int(input("Enter the length : "))
    value = w*l
    print(value)
    
def simpleinterest():
    p = int(input("Enter the principal amount : "))
    r = int(input("Enter the rate of interest : "))
    t = int(input("Enter the number of years : "))
    value = (p*r*t)/100
    print(value)

option=-1
while option<=0:
    print("1=areaofcircle()\n2=areaofrectangle()\n3=areaofsqur()\n4=simpleinterest()")
    option=int(input("Enter the option :"))
    if option==1:
        areaofcircle()
    elif option==2:
        areaofrectangle()
    elif option==3:
        areaofsqur()
    elif option==4:
        simpleinterest()
    else:
        print("choose the valid option ")
_____________________________________________________________
#print the sum of given number and display the value in a pyiramid

def dosum():
    sum = int(input("enter the number :"))
    a = input("enter the design :")
    value = sum*(sum+1)/2
    print(value)
    for i in range(1,int(value)+1):
      for j in range(1,i+1):
        print(a, end='\t')
      print('\n')
  
dosum()
__________________________________________________________
#print the sum of given number and display the value in a pyiramid
def dosum(value):
    for i in range(1,int(value)+1):
      for j in range(1,i+1):
        print(a, end='\t')
      print('\n')

sum = int(input("enter the number :"))
a = input("enter the design :")
value = sum*(sum+1)/2
dosum(value)

_______________________________________
#finding the amount for the meter

def charge(used_reading):
    if used_reading<=100:
        amount = used_reading*5
    elif used_reading<=500:
        amount = 100*5+(used_reading-100)*10
    else:
        amount = (100*5)+(400*10)+(used_reading-500)*15
    print(amount)

prev_month_reading = int(input("enter the prev reading :"))
current_month_reading = int(input("enter the current reading :"))
meter_number = int(input("enter the meter number :"))
used_reading = current_month_reading - prev_month_reading

charge(used_reading)

___________________________________________________
#write a function in python to find the factorial of a given number
def fact():
    factorial = 1
    num =int (input("enter the num :"))
    if num<0:
        print("factorial will not work for -ve numbers")
    if num>0:
        for i in range(1,num + 1):
           factorial = factorial*i
        print(factorial)
    
    
fact()
____________________________________________________________
#write a function in python to find the number of upper and lower case letters in a given string.
def casefun():
    enter_string = input("enter the string :")
    upper = 0
    lower = 0
    for i in enter_string:
        if i >='A' and i <= 'Z':
            upper += 1
        elif i >= 'a' and i <= 'z':
            lower += 1
    print("the upper case letters are {}".format(upper))
    print("the lower case letters are {}".format(lower))

casefun()
_________________________________________________________________________
#write a function in python to find the number of special characters in a given string
def splchar():
    msg =input("enter the statemant :")
    for i in msg:
        if not i.isalnum() :
            print(i)

splchar()
_________________________________________________________________________
recursive funtion:
#sum of 'n' numbers using def function
def sum(n):
    if n<=1:
        return n
    else:
        return n+sum(n-1)

p = sum(3)
print("sum of 3 numbers is {}".format(p))
_______________________________________________________________________________
#write a function in python to print the squares of the numbers till 'n' where n is the integer value given by the user.
def suare_number():
    number = int(input("enter the number :"))
    for i in range(0,number+1):
        i = i**2
        print(i)
        
suare_number()
________________________________________________________
#write a function to print the multiplication table of given number
def mul_number():
    given_number = int(input("enter the number :"))
    n = given_number
    print(n*1,n*2,n*3,n*4,n*5,n*6,n*7,n*8,n*9,n*10 )
    

mul_number()
______________________________________________________________________
# write a function in python to accept employee's name and salary as function arguments and display them.function should be designed in such a way that when we don't pass salary, it should print the default salary as 9000.00
def emp_name_sal(name,salary=9000.0):
    print(name)
    print(salary)    
    
emp_name_sal('swetha')
________________________________________________________________
#sum of 'n' numbers using recursive function
def mul(n):
    if n<=1:
        return n
    else:
        return n*mul(n-1)

p = mul(4)
print("mul of 4 numbers is {}".format(p))
______________________________________________
#print the even numbers ina given list
list_num = [1,25,32,44,84,56,47,28,49]
for i in list_num:
    if i%2==0:
        print(i)
    
______________________________________________
#find all the strings which contain a letter 'w' from the list
n = ["water","waste","air","raw","swetha"]
for i in n:
    if "w" in i:
        print(i)
________________________________________________
#find the string which has more than 2 volwes and print
words = ['apple', 'orange', 'pear', 'my', 'sky', 'why', 'iguana','tiger', 'eagle']
vowel="aeiou"
for w in words:
    cnt = 0
    for l in w:
        if l in vowel:
            cnt= cnt+1
    if (cnt>2):        
        print(w)
___________________________________________________________________________
#find the nymber which is greater than 500
num_list = [235,345,456,674, 135,384, 895,567, 607]
for i in num_list:
    if i>500:
        print(i)
 
_________________________________________________________________
#print the middle element in the list
num_list = [235,345,456,674,135,384,895,567]
print(len(num_list))
midd_num =(len(num_list))/2
print(num_list.index(midd_num))

______________________________________________
#print the biggest and smallest element in the list
num_list = [235,345,456,674,135,384,895,567]
print(min(num_list))
print(max(num_list))
_________________________________________________
#print the biggest and smallest element in the list
num_list = ["swetha","air","rama"]
print(min(num_list))
print(max(num_list))    
___________________________________________
#find the squrs which are less than in 
num_list = [10,2,8,12,34,5,6,4,30]
for i in num_list:
    if i<10:
        i=i**2
        print(i)
________________________________________________
#print the students record in list format
def school_record():
    n = int(input("How many students you want to enter :"))
    all_stud = []
    for x in range(0,n):
        name_stud  = input("Enter the name of the student :")
        age_stud   = int(input("Enter the age of the student :"))
        class_stud = int(input("Enter the class of the student :"))
        grade_stud = (input("Enter the grade of the student :"))
        sub = int(input("how many sub you want to enter :"))
        sub_marks = []
        for i in range(0,sub):
            marks = int(input("enter the sub marks :"))
            sub_marks.append(marks)
        Grade = " "
        sum = 0
        for i in sub_marks:
            sum = sum+i
        record_stud = []
        for x in range(0,n):
            per = (sum/sub)*100
            if per>=80:
              Grade = "A"
            elif per>=60:
               Grade = "B"
            elif per>=55:
               Grade = "C"
            else:
                Grade = "Failed" 
        record_stud.append(name_stud)
        record_stud.append(age_stud)
        record_stud.append(class_stud)
        record_stud.append(grade_stud)
        record_stud.append(sum)
        all_stud.append(record_stud)
    print(all_stud)

school_record()

_________________________________________________________________________
def validation_name(Name):
    if  ( Name.isalpha() or not Name.isalnum() ) and (len(Name) >= 4):
        return True
    else :
        return False
    
    
def get_name():
    for x in range (0,2):
        Name = input("Enter the Name : ")
        if validation_name(Name):
            return Name
        else:
            print("Name not valid")
    return "Null"
    
def validation_age(Age):
    if  ( Age.isnumeric ) and (len(Age) <= 2) and (int(Age) < 15):
        return True
    else :
        return False

def get_age():
    for x in range (0,2):
        Age = input("Enter the Age : ")
        if validation_age(Age):
            return Age
        else:
            print("Age not valid")
    return "Null"
        
        
def validation_class(Class):
    if  ( Class.isnumeric ) and (int(Class) <= 10):
        return True
    else :
        return False

def get_class():
    for x in range (0,2):
        Class = input("Enter the Class : ")
        if validation_class(Class):
            return Class
        else:
            print("Class not valid")
    return "Null"
    
    
def validation_grade(Grade):
    if  ( Grade.isalpha ) and (len(Grade) = 1):
        return True
    else :
        return False
        
def get_grade():
    for x in range (0,2):
        Grade = input("Enter the Grade : ")
        if validation_grade(Grade):
            return Grade
        else:
            print("Grade not valid")
    return "Null"

print(get_grade())   