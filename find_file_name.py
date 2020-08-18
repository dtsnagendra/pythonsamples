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
    
    
def files():
    try:
        file_name = input("enter the file name : ")
        file = open(file_name,"r")
        file.read()
        return True
    except:
        print("the file you enter is invalid please enter the valid name ")
        return False

for i in range(0,3):
    if files():
        break
files()     
