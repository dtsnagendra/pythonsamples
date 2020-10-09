

#Multi Threading

#- Process - it can be a executable(.exe) or any other component ( library, dll)
#- Thread

import  _thread

tstatus = {'t1':False,'t2':False}

def print_name(tname,pname):
      i = 0
      while i < 10:
          print(f"thread name is {tname} and person name is {pname}\n")
          i = i+1
      tstatus['t1'] = True

def fill_data(area):
    # fill the data into the list from file/database
    for i in area:
        print(f"item is {i}")
    tstatus['t2']= True

_thread.start_new_thread(print_name,("Thread-1","Swetha"))

larea = [11,22,33,44,55]

_thread.start_new_thread(fill_data,(larea,))

print("in main process .... executing something .... ")


while tstatus['t1']==False or tstatus['t2']==False:
   pass

#thread.start_new_thread(print_name,("Thread-1","Swetha"))

# create a thread - which takes list of vegetables and fruits and print vegetables or fruits 
# whose name starts with 'c' or 'm'

#create a thread - print the items whose length is greater than 'n' - n should be taken from user.
#create a thread - which has at least 2 vowels

#create a thread - which are having a letter/word given by user.
#create a thread to create a file - filename would be given by user. write some random content.



