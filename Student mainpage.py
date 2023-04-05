from tkinter import *
import tkinter.messagebox as mb
from PIL import ImageTk,Image

root = Tk()
root.title("Student Mainpage")
root.geometry("380x250")
root.resizable(False, False)

Label(root, text="Fill Your Attendance", font="ar 15 bold").grid(row=0, column=3)
def getvals():
    mb.showinfo("Attendance","Attendance Filled Successfully")

# Fields name

name = Label(root, text="username:")
Subject = Label(root, text="Subject name:")
Faculty= Label(root, text="Faculty name")
regno = Label(root, text="Reg no:")
Status = Label(root, text="Present(Yes/No):")
# packing Fields

name.grid(row=1, column=2)
Subject.grid(row=2, column=2)
Faculty.grid(row=3, column=2)
regno.grid(row=4, column=2)
Status.grid(row=5, column=2)

# Variable for storing data

nameval = StringVar
subval = StringVar
facval = StringVar
regnoval = StringVar
statusval = StringVar


# Creating entry Fields

nameentry = Entry(root, textvariable=nameval)
subentry = Entry(root, textvariable=subval)
facentry = Entry(root, textvariable=facval)
regnoentry = Entry(root, textvariable=regnoval)
statusentry = Entry(root, textvariable=statusval)

# Packing Entry Fields
nameentry.grid(row=1, column=3)
subentry.grid(row=2, column=3)
facentry.grid(row=3, column=3)
regnoentry.grid(row=4, column=3)
statusentry.grid(row=5, column=3)


# Submit Button
Button(root, text="SUBMIT", command=getvals).grid(row=6, column=3)
Button(root, text="Back").grid(row=7, column=3)

root = Tk()
root.mainloop()

