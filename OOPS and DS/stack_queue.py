
#Stack
# - LIFO - Last In First Out
# - implemented using List, LifoQueue 
from queue import LifoQueue

s = LifoQueue(maxsize=5)
print(s.qsize())
s.put(10)
print(s.qsize())
print(s.put(20))
print(s.get())
print(s.full())
print(s.empty())

#Queue
# - FIFO
# - implementing using List, Queue
from queue import Queue

q = Queue()
q.put(10)
q.put(20)
print(q.qsize())
print(q.full())
print(q.empty())

# operations - insert, delete, display, 
'''
queue = []

x = 10
queue.append(x)
queue.append(20)
queue.append(30)
queue.append(40)
print(queue)
ele = queue.pop(0)
print(ele)
queue.append(50)
print(queue)
'''