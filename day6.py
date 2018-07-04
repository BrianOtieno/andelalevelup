from tkinter import *
from tkinter import messagebox
import requests
from requests.auth import HTTPBasicAuth
import time;
import os # If you have to validate secret key without using base64encode.org - os.environ["SECRET_KEY"]

#sudo apt-get install python python-tk - to install TK interface in Ubuntu. This comes set in windows after installing python


root=Tk()
root.geometry("1200x800")
root.title("Andela LevelUp C2B")

SunKenTop=Frame(root, width=800,relief=SUNKEN)
SunKenTop.pack(side=TOP)

lblInfo=Label(SunKenTop,font=('arial',50,'bold'),text="Andela LevelUp C2B ",fg="Steel Blue",bd=10,anchor='w')
lblInfo.grid(row=0,column=0)

f1=Frame(root,width=800,height=400,relief=SUNKEN)
f1.pack(side=LEFT)

#Assign current Timestamp
Timestamp = time.time()

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
    txt_amount.set("")
    PartyA.set("")
    PartyB.set("")
    PhoneNumber.set("")

#Declare Variables
access_token = StringVar()
api_url = StringVar()
ShortCode = StringVar()
ResponseType = StringVar()
ConfirmationURL = StringVar()
ValidationURL = StringVar()
txt_amount = StringVar()
PartyA = StringVar()
PartyB = StringVar()
PhoneNumber = StringVar()







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
        if not validators.url(CallBackURL):
            RaiseError('Invalid CallBack URL')
        else:
            pass
        if empty(access_token):
            RaiseError("Invalid Access Token")
        else:
            pass


    output = {"CallBack":{"CallBackURL": "http://mpesa-requestbin.herokuapp.com/1mrwy3n1"}  }
    lbl_Response.configure(text=output)

    response = requests.post(api_url, request= json, headers=access_token)




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

#Amount
lbl_amount= Label(f1, font=('arial', 16, 'bold'),text="Amount",bd=16,anchor="w")
lbl_amount.grid(row=0, column=2)

txt_amount=Entry(f1, font=('arial',16,'bold'),textvariable=txt_amount,bd=10,insertwidth=4,bg="powder blue",justify='right')
txt_amount.config(show="*")
txt_amount.grid(row=0,column=3)

#PartyA
lbl_PartyA= Label(f1, font=('arial', 16, 'bold'),text="Party A",bd=16,anchor="w")
lbl_PartyA.grid(row=1, column=2)

txt_PartyA=Entry(f1, font=('arial',16,'bold'),textvariable=PartyA,bd=10,insertwidth=4,bg="powder blue",justify='right')
txt_PartyA.grid(row=1,column=3)

#PartyA
lbl_PartyB= Label(f1, font=('arial', 16, 'bold'),text="Party B",bd=16,anchor="w")
lbl_PartyB.grid(row=2, column=2)

txt_PartyB=Entry(f1, font=('arial',16,'bold'),textvariable=PartyB,bd=10,insertwidth=4,bg="powder blue",justify='right')
txt_PartyB.grid(row=2,column=3)

#PartyA
lbl_PartyB= Label(f1, font=('arial', 16, 'bold'),text="Party B",bd=16,anchor="w")
lbl_PartyB.grid(row=2, column=2)

txt_PartyB=Entry(f1, font=('arial',16,'bold'),textvariable=PartyB,bd=10,insertwidth=4,bg="powder blue",justify='right')
txt_PartyB.grid(row=2,column=3)

#PhoneNumber
lbl_PartyB= Label(f1, font=('arial', 16, 'bold'),text="Phone",bd=16,anchor="w")
lbl_PartyB.grid(row=3, column=2)

txt_Phonenumber=Entry(f1, font=('arial',16,'bold'),textvariable=PhoneNumber,bd=10,insertwidth=4,bg="powder blue",justify='right')
txt_Phonenumber.grid(row=3,column=3)

#=====================================Add Some Buttons============================================================
btnReset=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Reset",bg="grey",command=Reset).grid(row=1,column=4)
btnExit=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Exit",bg="brown",command=formExit).grid(row=2,column=4)
btnPost=Button(f1,padx=20,pady=14,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="POST",bg="green",command=submit).grid(row=4,column=2)
#I'll validate this if need be. Wasn't part of assignment

root.mainloop()
