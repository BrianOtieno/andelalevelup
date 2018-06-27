from tkinter import*
#I don't know why tkinter messagebox has to be imported separately after importing the whole library
from tkinter import messagebox
#user class
class user():
    def __init__(self, username, password, valid_user, valid_password):
        username = username
        password = password
        valid_user = valid_user
        valid_password = valid_password

        if (username == valid_user and password==valid_password):
            print("You username and password has been succefully validated")
        else:
            print("Invalid login Credentials")

print ("*************Enter Credentials To Register ***************")
username = input("UserName: ")
password = input("Password: ")
#access = {username : password}
print ("*************Enter Credentials To Login ***************")
valid_user = input("UserName: ")
valid_password = input("Password: ")
#access.update({valid_user: valid_password})
user(username, password, valid_user, valid_password)


root=Tk()
root.geometry("800x400")
root.title("Andela LevelUp Sign In")

SunKenTop=Frame(root, width=800,relief=SUNKEN)
SunKenTop.pack(side=TOP)

lblInfo=Label(SunKenTop,font=('arial',50,'bold'),text="Andela LevelUp Login ",fg="Steel Blue",bd=10,anchor='w')
lblInfo.grid(row=0,column=0)

f1=Frame(root,width=800,height=300,relief=SUNKEN)
f1.pack(side=LEFT)
#Declare Variables
entereduser = StringVar()
enteredpassword = StringVar()

#Define Form Functions
def formExit():
    root.destroy()

def Reset():
    entereduser.set("")
    enteredpassword.set("")

def submit():
    if (entereduser == username and enteredpassword == password):
        messagebox.showinfo("Login Info", "Login Succesful!")
    else:
        messagebox.showinfo("Login Info", "Invalid Login Credentials!")

lblUsername= Label(f1, font=('arial', 16, 'bold'),text="Enter Username",bd=16,anchor="w")
lblUsername.grid(row=0, column=0)

txtUsername=Entry(f1, font=('arial',16,'bold'),textvariable=entereduser,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtUsername.grid(row=0,column=1)


lblPassword= Label(f1, font=('arial', 16, 'bold'),text="Enter Password",bd=16,anchor="w")
lblPassword.grid(row=1, column=0)

txtPassword=Entry(f1, font=('arial',16,'bold'),textvariable=enteredpassword,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtPassword.config(show="*")
txtPassword.grid(row=1,column=1)

btnLogin=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Login",bg="green",command=submit).grid(row=2,column=1)
btnExit=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Exit",bg="brown",command=formExit).grid(row=4,column=1)
#I'll validate this if need be. Wasn't part of assignment

root.mainloop()
