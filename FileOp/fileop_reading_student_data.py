
# **************************************************************************
#  Description : This program displays the student record
#  input : 
#  output : 
#  Author : Siva Nagendra
#  Date: 20 Aug 2020
#  Version : 1.0
# **************************************************************************

student_details = []

fn = open("D:\\sample\\pythonsamples\\fileop\\student.dat",'r')

while True:
      s = fn.readline()
      if s != "":
         r = dict(eval(s))
         student_details.append(r)
      else:
         break

for v in student_details:
      print(v)

fn.close()


