def validation_name(Name):
    if  ( Name.isalpha() or not Name.isalnum() ) and (len(Name) >= 4):
        return True
    else :
        return False
    
    
def get_name():
    try:
        for x in range (0,2):
            Name = input("Enter the Name : ")
            if validation_name(Name):
                return Name
            else:
                print("Name not valid")
        return ""
    except:
        print("please enter the valid name more than 4 char ")
        get_name()
    
min_age = 10 

def validation_age(Age):
    if  (Age) >=min_age :
        return True
    else :
        return False

def get_age():
    try:
        Age = int(input("Enter the Age : "))
        if validation_age(Age):
            return Age
        else:
            print("min age should be 10")
            #get_age()
            return min_age
        #return ""
    except:
        print("enter the valid input ")
        #get_age()
        return min_age
        
        
def validation_class(Class):
    if  ( Class.isnumeric ) and (int(Class) <= 10) and (int(Class) > 0):
        return True
    else :
        return False

def get_class():
    try:
        for x in range (0,2):
            Class = input("Enter the Class : ")
            if validation_class(Class):
                return Class
            else:
                print("Class not valid")
        return ""
    except:
        print("the entered class value is invalid, please enter the valid class value between 1 to 10")
        get_class()
    
        
    
def validation_grade(Grade):
    list = ["A","B","C"]
    if  Grade in list:
        return True
    else :
        return False
        
def get_grade():
    try:
        for x in range (0,2):
            Grade = input("Enter the Grade : ")
            if validation_grade(Grade):
                return Grade
            else:
                print("Grade not valid")
        return ""
    except:
        print("enter the valid grade with char and must contain single char ")
        get_grade()
        
def validation_subject(Subject):
    if not Subject.isnumeric():
        return False 
    else:
        marks = int(Subject)
        if  marks >= 0 and marks <= 100 :
            return True
        else :
            return False

def get_subject():
    try:
        for x in range (0,2):
            Subject = input("Enter the marks : ")
            if Subject == "":
                Subject = "0"        
            if validation_subject(Subject):
                return int(Subject)
            else:
                print(" Not valid")
        return 0
    except:
        print("enter the valid marks in integer and  which is less than or equal to 100 and greater than 0")
        get_subject()

def get_all_marks():
    all_subjects = []
    for x in range (0,6):
        all_subjects.append(get_subject())
    return all_subjects
       

def get_final_grade(total_marks):
    Grade = " "
    per = (total_marks/6)*100
    if per>=80:
        Grade = "A"
    elif per>=60:
         Grade = "B"
    elif per>=55:
        Grade = "C"
    else:
        Grade = "Failed"
    return Grade

Student_count = int(input("Enter the number of students : "))
Student_list = []
for x in range (0,Student_count):
    Student_record ={}
    Student_record["Name"] = get_name()
    Student_record["Age"] = get_age()
    Student_record["Class"] = get_class()
    Student_record["Grade"] = get_grade()
    Student_record["Marks"] = get_all_marks()
    Student_list.append(Student_record)
print(Student_list)
