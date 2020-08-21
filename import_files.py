
import os
os.remove("sample.txt")

try:
    file_name = input("enter the file name : ")
    file_name2 = input("enter the file name2 : ")
    file = open(file_name,"w")
    file2 = open(file_name2,"w")
    text = input("enter the statements : ")
    text2 = input("enter the statements2 : ")
    file.write(text)
    file2.write(text2)
    file.close()
    file2.close()
except Exception as msg:
    print("Exception is",msg)
    
    
def validate_file(fname):
    import os
    if os.path.exists(fname):
       return True
    else:
       return False

def read_file():
    count =0
    for i in range(0,3):
        file_name = input("enter the file name : ")
        if validate_file(file_name):
            return file_name
        else:
            if count <3:
                count +=1
            else:
                return " "

f1 = read_file()
f2 = read_file()

# open both files in read mode and read the content.
text6 = ""
text7 = ""

if f1:
    f = open(f1,"r")
    text6 = f.read()
    f.close()
if f2:
    s = open(f2,"r")    
    text7 = s.read()
    s.close()

main_file = open("sample.txt","w")
text3 = text6 + text7
main_file.write(text3)
main_file.close()
