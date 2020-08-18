try:
    file = open("sample.txt","w")
    text = input("enter the statements : ")
    file.write(text)
    file.close()
except Exception as msg:
    print("Exception is",msg)


try:
    file = open("sample.txt","r")
    text = file.read()
    file2 = open("ram.txt","a")
    text2 = input("enter the statements : ")
    text += text2
    file2.write(text)
    file.close()
except Exception as msg:
    print("Exception is",msg)