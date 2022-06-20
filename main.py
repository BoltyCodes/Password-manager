

import sys
import smtplib
import random
from matplotlib.cbook import strip_math

from rsa import DecryptionError




username = input("Enter your name: ")
#Main = input(f"Welcome {username}, please enter your password to access your passwords: ")


    
choices = int(input(f"Hey {username} what would you like to do? \n 1. Add a password \n 2. View your passwords \n 3. Exit \n"))



def encode(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            index = ord(char) + shift
            if index > ord('z'):
                index -= 26
            ciphertext += chr(index)
        else:
            ciphertext += char
    return ciphertext
    
def decode(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            index = ord(char) - shift
            if index < ord('a'):
                index += 26
            plaintext += chr(index)
        else:
            plaintext += char
    return plaintext
    
shift = 7
def add_password():

    pwd = input("Enter a password:")

    if pwd:
        app = input("Enter what this password is for:")
        if app:
            True
        else:
            print("Please state what the password is for")
            pass
    else:
        pass


    f = open("password_manager\pwd.txt", "a+")
    encryption_txt = encode(pwd, shift)
    f.write(f"\n The password for {app} is {encryption_txt}")
    f.close()



    choices = int(input(f"Hey {username} what would you like to do? \n 1. Add a password \n 2. View your passwords \n 3. Exit \n"))
    
    if choices == 1:
     add_password() 
            
    if choices == 2:
     collect_password()

    if choices == 3:
     sys.exit
  
    
def collect_password():
 
    main = input("Hey! Enter the password here to get access: ")
    if main == "dhruva2007":

       try:

        recipient_email = input("Enter your email:")
        my_email = "dhruva.happiest@gmail.com"
        password = "mnlulmslwlbscrma"

        connection = smtplib.SMTP("smtp.gmail.com",587)
        connection.starttls()
        connection.login(user=my_email, password=password)

        connection.sendmail(from_addr=my_email, to_addrs=recipient_email,msg="sbdvhbsdybdesm")
        connection.close()

       except:
        raise TypeError 
       


       print("Almost done :)"," \n One last step: We sent an email, enter the pin below in NUMBERS" )
       message = str(input("Enter the message from the email:"))
       if message == "sbdvhbsdybdesm" or "HelloDude":
        
        print("Access fully granted, view passwords:")
        print("You can use this password for next time: HelloDude")
        


        '''with open("password_manager\pwd.txt", 'r') as f:
         decrypted_file = decode(f, shift)
            
            '''
         
            
        x = open("password_manager\pwd.txt", "r+")
        for i in x:
            #read every line in the file and decrypt it
            #Hello there! the problem I have: either everything in the gets decrypted except the pwd or only the password gets decrypted and the rest of the file does not.
            decrypted_file = decode(i, shift) #decrypts everything but password
            decrypted_pwd = decode(x, shift)# decrypts the password only 
            print(decrypted_file)  
        x.close
        sys.exit


            
        
         
        
         
        

       
       else:
        print("Oops didnt work, restart procedure to try again!")
        sys.exit
      

    
    

        
    else:
        print("Access denied")
        sys.exit
    

    choices = int(input(f"Hey {username} what would you like to do? \n 1. Add a password \n 2. View your passwords again, if it didnt work the first time \n 3. Exit \n"))
    
    if choices == 1:
      add_password() 
            
    if choices == 2:
     collect_password()

    if choices == 3:
     sys.exit
    
    



if choices == 1:
    add_password() 
            
if choices == 2:
    collect_password()

if choices == 3:
    sys.exit

