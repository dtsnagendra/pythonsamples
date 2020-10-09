

import threading as t
import time
lname = []
pname = []

def greet(name,kname):
    print(f"hai ... welcome {name}")
    #tlock.acquire()
    #c = 0
    for i in range(0,10,2):
         kname.insert(i,i*2)
         time.sleep(1)
   # tlock.release()

tlock = t.Lock()

t1 = t.Thread(target=greet,args=('Swetha',lname))
t2 = t.Thread(target=greet,args=('India',pname))

t1.start()
t2.start()

print("main process content ... ")
#print(l) # i am trying to access the list

t1.join()
t2.join()

print("main content ....")
print(lname)
print(pname)

#create a thread to fill the list with alphabets
#create a thread to print the list of alphabets produced in the previous thread.
#create file operation - open a file, write some data, close the file - with lock, without lock
