
# **************************************************************************
#  Description : This program adds the student record
#  input : student details
#  output : record saved to file
#  Author : Siva Nagendra
#  Date: 20 Aug 2020
#  Version : 1.0
# **************************************************************************

student_details = {}

fn = open("D:\\sample\\pythonsamples\\fileop\\student.dat",'a')

rno = int(input("Enter Roll Number : "))
name = input("Enter Name: ")
marks = int(input("Enter Marks: "))
student_details['rno'] = rno
student_details['name'] = name
student_details['marks'] = marks
fn.write("\n"+str(student_details))

print("inserted new student details ...")

fn.close()


