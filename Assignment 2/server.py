# importing socket and hashlib modules
import socket            
import hashlib

userfound=False

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
        print(list[i].username," ",list[i].num," ",list[i].hashpassword)



# Creating a socket
s = socket.socket()        
print ("Socket successfully created")


#port assigning
port = 12350              


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
list.append(detail('prashanth',2,'prashanth'))
list.append(detail('vasanth',11,'vasanth'))
list.append(detail('abhinav',23,'kathuri'))
list.append(detail('karthik',9,'karthik'))


#defining a searh function to find and return the number and password of the user
def search(user):
    for i in range(0,len(list)):
        if list[i].username==user:
            userfound=True
            return i,list[i].num,list[i].hashpassword

    

while True:
 
  # Accepting the connection from client.
  c, addr = s.accept()    
  print ('Connection accepted from', addr )



  #receive username from the client program
  rec=c.recv(1024).decode()
  print (rec)
  
    
  #searching for the user and returning the index,number and  hashedpassword
  index,number,hashpassword=search(rec)
  sentnum=number
  numbe=str(number)

  #   c.send('Thank you for connecting'.encode())
  #sending the number to client program
  c.send(str(sentnum).encode())


#   hashed=hash(number,hashedpass) 
  #printing the hashed password present in the list 
  print("/////////////////////")
  print(hashpassword)

  #receive hashed password from client program
  hp=c.recv(1024).decode()
  print (hp)


  #hashing the received hashed password once again to authenticate
  temp=hash(1,hp)

  #checking if the hashed password sent by client matches with the password present in the list
  result = (temp==hashpassword)
  print(result)


  #updating the hashed passsword and number in the list of the respective user when access is success
  if result:
      c.send('Login successfull'.encode())
      list[index].num=list[index].num-1
      list[index].hashpassword=hp
  else:
      c.send('Login Failed'.encode())
      continue



  printlist(list)
#   if(result):
      
  # Close the connection with the client
  c.close()
   
  # Breaking once connection closed
#   break