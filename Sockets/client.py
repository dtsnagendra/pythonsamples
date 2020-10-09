import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = socket.gethostname()                           
port = 9999
print(f"host name is {host}")

# connection to hostname on the port.
print(f"connecting to  {host}")
s.connect((host, port))

while True:
    msg = input("Enter a message : ")
    s.send(msg.encode('ascii'))
    msg2 = s.recv(1024) 
    print(f"received data ...")
    txt = msg2.decode('ascii')
    print(txt)
    if txt.find("Bye") >= 0:
        break

s.close()
