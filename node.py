

class Node:
    def __init__(self,d):
        self.data = d
        self.name = 
        self.listma = [1,2,3,4,5]
        self.ma = (33,44,)
        self.next = None
    def __str__(self):
        return (f"--> {self.data},{self.next}")

root = None
last = None

while True:
    v = int(input("Enter node value: "))
    n = Node(v)

    if root == None:
        root = n
        last = n
    else:
        last.next = n
        last = n

    print("Do you want to continue ? (y/n)")
    ans = input()
    if ans == 'n':
        break

s = 0
while root != None:
       s = s + root.data
       root = root.next
print(s)

