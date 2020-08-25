
# **************************************************************************
#  Description : This program modifies the student record
#  input : roll number
#  output : modified record
#  Author : Siva Nagendra
#  Date: 20 Aug 2020
#  Version : 1.0
# **************************************************************************

fn = open("D:\\sample\\pythonsamples\\fileop\\student.dat",'r')
st = fn.readlines()
fn.close()

student_list = []

for ele in st:
    n = eval(ele)
    student_list.append(n)

rno = int(input("Enter roll number you want to modify "))

for e in student_list:
    if e['rno'] == rno:
        print("Record found ...")
        print("What do you want to modify ? 1. Rno 2. Name 3. Makrs")
        op = int(input())
        if op == 1:
            nrno = int(input("Enter new rno :"))
            student_list[5]['rno'] = nrno

for e in student_list:
    print((e))



