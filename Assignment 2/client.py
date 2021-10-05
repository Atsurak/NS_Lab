# importing socket and hashlib modules
import socket            
import hashlib 


#defining a hashfunction sha256.
def hash(n,password):
    temp=password
    for i in range(0,n):
        temp=hashlib.sha256(temp.encode())
        temp=temp.hexdigest()
        # print(temp)
    return temp


# Creating a socket
s = socket.socket()        


# defing the port number
port = 12350   
    
    
# connecting to the server(local)
s.connect(('127.0.0.1', port))


#taking username 
username=input("Enter username:")



#sending a username to server
s.send(username.encode())



# receive number from server
# print (s.recv(1024).decode())
rec=s.recv(1024).decode()
print(rec)
rec=int(rec)


#taking password from the user
password=input("\nEnter password:")

#hashing the password
msg=hash(rec-1,password) 

#sending the hashed password
s.send(msg.encode())


#receive messege from client
rec=s.recv(1024).decode()
print(rec)

# close the connection
s.close()    
    
     