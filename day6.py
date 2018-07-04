from tkinter import *
from tkinter import messagebox
import requests
from requests.auth import HTTPBasicAuth
import time;
import os # If you have to validate secret key without using base64encode.org - os.environ["SECRET_KEY"]


root=Tk()
root.geometry("800x600")
root.title("Andela LevelUp C2B")

SunKenTop=Frame(root, width=800,relief=SUNKEN)
SunKenTop.pack(side=TOP)

lblInfo=Label(SunKenTop,font=('arial',50,'bold'),text="Andela LevelUp C2B ",fg="Steel Blue",bd=10,anchor='w')
lblInfo.grid(row=0,column=0)

f1=Frame(root,width=800,height=400,relief=SUNKEN)
f1.pack(side=LEFT)


#assign to dictionary

#Define Form Functions
def formExit():
    root.destroy()

def Reset():
    access_token.set("")
    api_url.set("")
    ShortCode.set("")
    ResponseType.set("")
    ConfirmationURL.set("")
    ValidationURL.set("")

#Declare Variables
access_token = StringVar()
api_url = StringVar()
ShortCode = StringVar()
ResponseType = StringVar()
ConfirmationURL = StringVar()
ValidationURL = StringVar()

Timestamp = time.time()




def submit():
    def __init__(self, access_token, api_url, ShortCode, ResponseType, ConfirmationURL, ValidationURL, PartyA, PartyB, PhoneNumber, CallBackURL):
        self.access_token = txt_access_token.get("1.0", "end-1c")
        self.api_url = api_url
        self.ShortCode = ShortCode
        self.ResponseType = ResponseType
        self.ConfirmationURL = ConfirmationURL
        self.ValidationURL = ValidationURL
        self.AccountReference = "Test" #This may be an input field on the interface
        self.TransactionDesc = "Test" #This may be an input field on the interface

        request = {
            "BusinessShortCode": "",
            "Password" : "",
            "Timestamp" : "",
            "TransactionType" : "",
            "Amount" : "3500",
            "PartyA" : PartyA,
            "PartyB" : PartyB,
            "PhoneNumber" : +254723328969,
            "CallBackURL" : "http://mpesa-requestbin.herokuapp.com/1mrwy3n1",
            "AccountReference" : AccountReference,
            "TransactionDesc" : TransactionDesc
        }
        if not validators.validurl:
            RaiseError('Invalid URL')
        else:
            pass
        if empty(access_token):
            RaiseError("Invalid Access Token")
        else:
            pass


    output = {"CallBack":{"CallBackURL": "http://mpesa-requestbin.herokuapp.com/1mrwy3n1"}  }
    lbl_Response.configure(text=output)





lbl_access_token= Label(f1, font=('arial', 16, 'bold'),text="Access Token",bd=16,anchor="w")
lbl_access_token.grid(row=0, column=0)

txt_access_token=Entry(f1, font=('arial',16,'bold'),textvariable=access_token,bd=10,insertwidth=4,bg="powder blue",justify='right')
txt_access_token.config(show="*")
txt_access_token.grid(row=0,column=1)
#api URL
lbl_api_url= Label(f1, font=('arial', 16, 'bold'),text="API URL",bd=16,anchor="w")
lbl_api_url.grid(row=1, column=0)

txt_api_url=Entry(f1, font=('arial',16,'bold'),textvariable=api_url,bd=10,insertwidth=4,bg="powder blue",justify='right')
txt_api_url.grid(row=1,column=1)

#Short ShortCode
lbl_ShortCode= Label(f1, font=('arial', 16, 'bold'),text="Short Code",bd=16,anchor="w")
lbl_ShortCode.grid(row=2, column=0)

txt_ShortCode=Entry(f1, font=('arial',16,'bold'),textvariable=ShortCode,bd=10,insertwidth=4,bg="powder blue",justify='right')
txt_ShortCode.grid(row=2,column=1)

#Response Type
lbl_ResponseType= Label(f1, font=('arial', 16, 'bold'),text="ResponseType",bd=16,anchor="w")
lbl_ResponseType.grid(row=3, column=0)

txt_ResponseType=Entry(f1, font=('arial',16,'bold'),textvariable=ResponseType,bd=10,insertwidth=4,bg="powder blue",justify='right')
txt_ResponseType.grid(row=3,column=1)

lbl_Response= Label(f1, font=('arial', 16, 'bold'),text="Response: ",bd=16,anchor="w")
lbl_Response.grid(row=5, column=1)


#=====================================Add Some Buttons============================================================
btnReset=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Reset",bg="grey",command=Reset).grid(row=1,column=3)
btnExit=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Exit",bg="brown",command=formExit).grid(row=2,column=3)
btnPost=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="POST",bg="green",command=submit).grid(row=4,column=1)
#I'll validate this if need be. Wasn't part of assignment

root.mainloop()
