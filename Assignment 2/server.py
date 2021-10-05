# importing socket and hashlib modules
import socket            
import hashlib

userfound=0

#defining a hashfunction sha256.
def hash(n,password):
    temp=password
    for i in range(0,n):
        temp=hashlib.sha256(temp.encode())
        temp=temp.hexdigest()
        # print(temp)
    return temp

#def printlist function
def printlist(list):
    for i in range(0,len(list)):
        print(list[i].username,"   ",list[i].num,"   ",list[i].hashpassword)

# Creating a socket
s = socket.socket()        
print ("Socket successfully created")

#port assigning
port = 3000        


#binding port to the socket
s.bind(('', port))        
print ("socket binded to %s" %(port))


# socket set to listen
s.listen(3)    
print ("socket is listening")           

#creating a mini-data
class detail:
    def __init__(self,username,num,password):
        self.username=username
        self.num=num
        self.password=password
        self.hashpassword=hash(num,password)

list =[]
list.append(detail('gopal',4,'gopal'))
list.append(detail('harsha',3,'harsha'))
list.append(detail('prasanth',2,'prasanth'))
list.append(detail('vasanth',11,'vasanth'))
list.append(detail('abhinav',23,'abhinav'))
list.append(detail('karthik',9,'karthik'))

#defining a searh function to find and return the number and password of the user
def search(user):
    found=False
    for i in range(0,len(list)):
        if list[i].username==user:
            global userfound
            # userfound=1
            found=True
            return found,i,list[i].num,list[i].hashpassword
        
    return found,i,list[i].num,list[i].hashpassword

while True:
 
  # Accepting the connection from client.
  c, addr = s.accept()    
  print ('Connection accepted from', addr )

  #receive username from the client program
  rec=c.recv(1024).decode()
  print(rec + " Trying to login")
  
  #searching for the user and returning the index,number and  hashedpassword
  found,index,number,hashpassword=search(rec)
  #print(hashpassword)
  #print(found)
  if found:
    sentnum=number
    #sending the number to client program
    c.send(str(sentnum).encode())

    #printing the hashed password present in the list 
    print("Password Stored in Record : " + hashpassword)

    #receive hashed password from client program
    hp=c.recv(1024).decode()
    print("Password received from client : " + hp)

    #hashing the received hashed password once again to authenticate
    temp=hash(1,hp)

    #checking if the hashed password sent by client matches with the password present in the list
    result = (temp==hashpassword)
    if(result):
        print("Login Successfull")
    else:
        print("Login Failed")

    #updating the hashed passsword and number in the list of the respective user when access is success
    if result:
        c.send('Login successfull'.encode())
        list[index].num=list[index].num-1
        list[index].hashpassword=hp
    else:
        c.send('Login Failed'.encode())
        continue

    print("---------UPDATED LIST--------")
    printlist(list)
    #If user not found Close the connection with the client
  else:
        c.send('User Not Found'.encode())
        c.close()

  c.close()
  print("Connection with client closed")
