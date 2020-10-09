

#Request and Response
#client - will send request to server
#server - will receive the requests and sends response.
#e.g gmail.com - request will be sent to google server
# data formats - 
# 1. Raw text
# e.g.  Hello --> How are you ? 
# e.g.  "this is swetha" -> how many vowels are present in this text ?

# 2. XML 
# e.g 
#      <Books>
#           <Book-id>1001</Book-id>
#           <Book-name> The great india </Book-name>
#      </Books>

# 3. csv
#       12,23,34,56,'nice to see you'

#IPC Mechanisms- Interprocess communication
# - Socket Programming
# - RPC - Remote Procedure Call
# - Shared Memory 

#Socket Programming 
# 
# socket - 
# server socket 
#  - we will create a socket
#  - listening on some port, ipaddress

#client 
# create a socket
# connect to server socket using port, ipaddress
 
import socket

s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostname = socket.gethostname()
port = 9999
print(f"host name is {hostname}")
s_socket.bind((hostname,port))
s_socket.listen(5)
print(f"server is listening ...")
c_socket,addr = s_socket.accept()
print(f"client connected ....{addr}")

while True:
    msg2 = c_socket.recv(1024)
    print(msg2.decode('ascii'))
    count = numofvowels(msg2)
    msg = str(count)
    c_socket.send(msg.encode('ascii'))
    t = msg.find("Bye")
    if  t >= 0:
        break

print(f"exiting ...")
c_socket.close()
s_socket.close()

