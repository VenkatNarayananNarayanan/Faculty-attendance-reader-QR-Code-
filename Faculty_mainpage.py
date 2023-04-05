from tkinter import *
import tkinter.messagebox as mb
from PIL import ImageTk,Image

root = Tk()
root.title(" Faculty Mainpage")
root.geometry("300x150")
root.resizable(False, False)

Label(root, text="Fill Your Attendance", font="ar 15 bold").grid(row=0, column=3)
def getvals():
    mb.showinfo("Status","Fetching..........wait for few minutes")

name = Label(root, text="name:")
Subject = Label(root, text="Subject name:")

name.grid(row=1, column=2)
Subject.grid(row=2, column=2)

nameval = StringVar
subval = StringVar

nameentry = Entry(root, textvariable=nameval)
subentry = Entry(root, textvariable=subval)

nameentry.grid(row=1, column=3)
subentry.grid(row=2, column=3)

Button(root, text="Status", command=getvals).grid(row=3, column=3)
Button(root, text="Back").grid(row=4, column=3)

root = Tk()
root.mainloop()

