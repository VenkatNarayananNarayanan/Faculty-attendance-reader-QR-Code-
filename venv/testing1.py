from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

def update(rows):
    for i in rows:
        trv.insert('','end',values = i)

con = mysql.connector.connect(host="localhost", user="root", passwd="venkat", database="dbms_project")
mycursor =  con.cursor()

root = Tk()

wrapper1 = LabelFrame(root,text="Faculty Present List ")
wrapper1.pack(fill="both",expand = "yes",padx=20,pady=10)

trv = ttk.Treeview(wrapper1, columns=(1,2), show = "headings", height = "6")
trv.pack()

trv.heading(1, text = "Faculty Name")
trv.heading(2, text = "Date and Time")

query = "select name, passwd from faculty_signup"
mycursor.execute(query)
rows = mycursor.fetchall()
update(rows)

root.title("My Application")
root.geometry("700x500")
root.mainloop()


