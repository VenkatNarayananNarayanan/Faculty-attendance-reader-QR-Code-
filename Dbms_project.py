from tkinter import *
from tkinter import ttk
import tkinter.messagebox as mb
from PIL import ImageTk,Image #pip install pillow
import mysql.connector as mc
import cv2
import numpy as np
from pyzbar.pyzbar import decode
from datetime import datetime


class homepage:
    def __init__(self,root):
        self.root = root
        self.root.geometry("380x380")
        self.root.resizable(False, False)
        self.bg = ImageTk.PhotoImage(file="att.jpg")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        Frame_login = Frame(self.root, bg="white")
        Frame_login.place(x=90, y=250, width=200, height=160)

        stu = Button(self.root, text="Admin Login", font=("Times new roman", 12, "bold"),bd = 0, fg="white", bg="#4568dc", command= self.admin_login)
        stu.place(x=140, y=280)

        fac = Button(self.root, text="Faculty Login", font=("Times new roman", 12, "bold"),bd=0 ,fg="white", bg="#4568dc",command=self.Faculty_login)
        fac.place(x=136, y=330)

    def admin_login(self):
        self.root.title("Admin Login Page")
        self.root.geometry("380x380")
        self.root.resizable(False, False)

        #background image

        self.bg=ImageTk.PhotoImage(file="att.jpg")
        self.bg_image=Label(self.root, image=self.bg).place(x=0,y=0, relwidth=1, relheight=1)

        #Login Frame

        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=90,y=110, width= 200,height=240)

        #Title & subtitle

        title = Label(Frame_login,text="Login Here",font=("Times new roman",11,"bold"),fg="#6162FF",bg="white").place(x=70,y=20)
        subtitle = Label(Frame_login, text="Admin login area", font=("Times new roman", 9, "bold"), fg="#1d1d1d",bg="white").place(x=55, y=40)

        #username


        lbl_user=Label(Frame_login,text="Username:",font=("Times new roman",11,"bold"),fg="grey",bg="white").place(x=5,y=65)
        self.username=Entry(Frame_login,font=("Times new roman",9,"bold"),bg="#E7E6E6")
        self.username.place(x=5,y=95,width=170)

        #password

        lbl_password = Label(Frame_login, text="Password:", font=("Times new roman", 11, "bold"), fg="grey", bg="white").place(x=5, y=115)
        self.password = Entry(Frame_login,show = "*", font=("Times new roman", 9, "bold"), bg="#E7E6E6")
        self.password.place(x=5, y=145, width=170)

        #Button
        self.var = IntVar()

        submit=Button(Frame_login, text="Login", command=self.check,font=("Times new roman", 9, "bold"),bd=0, fg="white", bg="blue").place(x=80, y=195)
        check1 = Checkbutton(Frame_login,text = "show password",command = self.show_pass,variable = self.var,offvalue = 0,onvalue =1,font=("Times new roman", 9, "bold"),bd=0, fg="black").place(x=5, y=165)
        back=Button(root, text="Back",bd=0,font=("Times new roman", 9, "bold"), fg="white", bg="blue").place(x=10, y=10)

    def show_pass(self):
        if self.var.get() == 1:
            self.password.configure(show="")
        elif self.var.get() == 0:
            self.password.configure(show="*")

    def check(self):
         if self.username.get()==" " or self.password.get()== "":
            mb.showerror("Error","All fields are required")
         elif self.username.get() == "Admin" and self.password.get() == "SRMIST":
            mb.showinfo("Welcome",f"welcome {self.username.get()}",command = self.adminpage())
         else:
            mb.showerror("Error","Invalid Username or Password")

    def adminpage(self):
        self.root.title("Admin Page")
        self.root.geometry("380x380")
        self.root.resizable(False, False)

        self.bg = ImageTk.PhotoImage(file="att.jpg")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        Frame_login = Frame(self.root, bg="white")
        Frame_login.place(x=90, y=110, width=200, height=240)

        present = Button(Frame_login,text = "Present Status",command=self.present,bd=0,font=("Times new roman", 9, "bold"), fg="black").place(x=55, y=30)
        absent = Button(Frame_login,text = "Absent Status",command=self.absent,bd=0,font=("Times new roman", 9, "bold"), fg="black").place(x=55,y=70)
        add = Button(Frame_login, text="Add Faculty",command = self.add_faculty, bd=0, font=("Times new roman", 9, "bold"), fg="black").place(x=60, y=110)
        remove = Button(Frame_login, text="Remove Faculty",command = self.remove_faculty, bd=0, font=("Times new roman", 9, "bold"), fg="black").place(x=50, y=150)
        request = Button(Frame_login, text=" Request ", command=self.faculty_request, bd=0, font=("Times new roman", 9, "bold"),fg="black").place(x=65, y=190)
        back = Button(root, text="Logout", bd=0,command=self.admin_login, font=("Times new roman", 9, "bold"), fg="white", bg="blue").place(x=10,y=10)



    def present(self):
        self.root.title("Present Status Page")
        self.root.geometry("800x500")
        self.root.resizable(False, False)
        self.bg = ImageTk.PhotoImage(file="present.jpg")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        Frame_login = Frame(self.root, bg="white")
        Frame_login.place(x=200, y=80, width=400, height=350)
        self.trv = ttk.Treeview(Frame_login, columns=(1, 2), show="headings", height="20")
        self.trv.pack()

        self.trv.heading(1, text="Faculty Name")
        self.trv.heading(2, text="Date and Time")

        con = mc.connect(host="localhost", user="root", passwd="venkat", database="dbms_project")
        mycursor = con.cursor()

        query = "select name, Date_Time from attendance"
        mycursor.execute(query)
        self.rows = mycursor.fetchall()

        Status = Button(root, text="Status",  command=self.present_status, font=("Times new roman", 9, "bold"),fg="black").place(x=375, y=450)
        remove = Button(root, text="Remove", command=self.remove1, font=("Times new roman", 9, "bold"), fg="black").place(x=600, y=450)
        back = Button(root, text="Back",command=self.adminpage, font=("Times new roman", 9, "bold"), fg="black").place(x=150,y=450)



    def present_status(self):
       for i in self.rows:
            self.trv.insert('', 'end', values=i)


    def remove1(self):
        self.root.title("Remove Faculty  Page")
        self.root.geometry("200x200")
        self.root.resizable(False, False)
        self.bg = ImageTk.PhotoImage(file="request1.png")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        name = Label(root, text="Faculty Name:")

        name.place(x=30, y=80)

        self.nameentry = Entry(root, font=("Times new roman", 9, "bold"), bg="#E7E6E6")

        self.nameentry.place(x=30, y=100)

        Button(root, text="change", command=self.attrem, fg="black").place(x=65, y=150)
        Button(root, text="Back", command=self.present, fg="black").grid(row=11, column=3)

    def attrem(self):
        try:
            if self.nameentry.get() == " ":
                print("Faculty Name is required")

            else:
                name = self.nameentry.get()
                if mb.askyesno("Confirm Delete?",f"Are you sure you want to give absent for {self.nameentry.get()}?"):
                      con = mc.connect(host="localhost", user="root", passwd="venkat", database="dbms_project")
                      mycursor = con.cursor()
                      name = self.nameentry.get()
                      query = "DELETE FROM attendance where name = '{}' ".format(name)
                      mycursor.execute(query)
                      con.commit()
                      print("Row Deleted")
                      mb.showinfo("Message",f"Given Absent for {self.nameentry.get()}",command = self.remove1())
                else:
                    return True

        except mc.DatabaseError as e:
            mb.showerror("error in the database", e)

    def absent(self):
        self.root.title("Faculty Absent Page")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        self.bg = ImageTk.PhotoImage(file="present.jpg")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        Frame_login = Frame(self.root, bg="white")
        Frame_login.place(x=100, y=80, width=200, height=350)
        self.trv1 = ttk.Treeview(Frame_login, columns=(1), show="headings", height="20")
        self.trv1.pack()

        self.trv1.heading(1, text="Faculty Name")


        con = mc.connect(host="localhost", user="root", passwd="venkat", database="dbms_project")
        mycursor = con.cursor()

        query = "select name from checklist where name not in(select name from attendance);"
        mycursor.execute(query)
        self.rows1 = mycursor.fetchall()

        Status = Button(root, text="Status", command=self.absent_status, font=("Times new roman", 9, "bold"),fg="black").place(x=175, y=450)
        back = Button(root, text="Back", command=self.adminpage, font=("Times new roman", 9, "bold"), fg="black").place(x=10, y=10)

    def absent_status(self):
        for i in self.rows1:
            self.trv1.insert('', 'end', values=i)

    def add_faculty(self):
        self.root.title("Add Faculty page")
        self.root.geometry("200x200")
        self.root.resizable(False, False)
        self.bg = ImageTk.PhotoImage(file="request1.png")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        name = Label(root, text="Faculty Name:")

        name.place(x=30, y=80)

        self.nameentry = Entry(root, font=("Times new roman", 9, "bold"), bg="#E7E6E6")

        self.nameentry.place(x=30, y=100)

        Button(root, text="Add Faculty", command=self.facadd, fg="black").place(x=65, y=150)
        Button(root, text="Back", command=self.adminpage, fg="black").place(x=10, y=10)

    def facadd(self):
         try:
             if self.nameentry.get() == " ":
                 print("Faculty Name is required")

             else:
                 con = mc.connect(host="localhost", user="root", passwd="venkat", database="dbms_project")
                 mycursor = con.cursor()
                 name = self.nameentry.get()
                 query = "INSERT INTO checklist values('{}')".format(name)
                 mycursor.execute(query)
                 con.commit()
                 print("Row Inserted")
                 mb.showinfo("Message","Faculty name is added successfully",command = self.add_faculty())

         except mc.DatabaseError as e:
              mb.showinfo("error in the database",e)


    def remove_faculty(self):
        self.root.title("Remove Faculty  Page")
        self.root.geometry("200x200")
        self.root.resizable(False, False)
        self.bg = ImageTk.PhotoImage(file="request1.png")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        name = Label(root, text="Faculty Name:")

        name.place(x=30, y=80)

        self.nameentry = Entry(root, font=("Times new roman", 9, "bold"), bg="#E7E6E6")

        self.nameentry.place(x=30, y=100)

        Button(root, text="Remove Faculty", command=self.facrem, fg="black").place(x=65, y=150)
        Button(root, text="Back", command=self.adminpage, fg="black").grid(row=11, column=3)

    def facrem(self):
        try:
            if self.nameentry.get() == " ":
                print("Faculty Name is required")

            else:
                name = self.nameentry.get()
                if mb.askyesno("Confirm Delete?","Are you sure you want to remove the faculty from the checklist?"):
                      con = mc.connect(host="localhost", user="root", passwd="venkat", database="dbms_project")
                      mycursor = con.cursor()
                      name = self.nameentry.get()
                      query = "DELETE FROM checklist where name = '{}' ".format(name)
                      mycursor.execute(query)
                      con.commit()
                      print("Row Deleted")
                      mb.showinfo("Message","Faculty name is removed successfully",command = self.remove_faculty())
                else:
                    return True

        except mc.DatabaseError as e:
            mb.showerror("error in the database", e)

    def faculty_request(self):
        self.root.title("Request Page")
        self.root.geometry("500x500")
        self.root.resizable(False, False)
        self.bg = ImageTk.PhotoImage(file="present.jpg")
        self.bg_image = Label(root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        Frame_login = Frame(self.root, bg="white")
        Frame_login.place(x=60, y=80, width=400, height=350)
        self.trv2 = ttk.Treeview(Frame_login,columns=(1,2), show="headings", height="20")
        self.trv2.pack()

        self.trv2.heading(1, text="Faculty Name")
        self.trv2.heading(2, text = "Request")
        con = mc.connect(host="localhost", user="root", passwd="venkat", database="dbms_project")
        mycursor = con.cursor()

        query = "select * from request"
        mycursor.execute(query)
        self.rows2 = mycursor.fetchall()
        view = Button(root, text="View Request", command=self.view_request, font=("Times new roman", 9, "bold"),fg="black").place(x=100, y=450)
        remove = Button(root, text="remove Request", command=self.delete_request, font=("Times new roman", 9, "bold"),fg="black").place(x=300, y=450)
        back = Button(root, text="Back", command=self.adminpage, font=("Times new roman", 9, "bold"), fg="black").place(x=10, y=10)

    def view_request(self):
        for i in self.rows2:
            self.trv2.insert('', 'end', values=i)

    def delete_request(self):
        self.root.title("Remove Request  Page")
        self.root.geometry("200x200")
        self.root.resizable(False, False)
        self.bg = ImageTk.PhotoImage(file="request1.png")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        name = Label(root, text="Faculty Name:")

        name.place(x=30, y=80)

        self.nameentry = Entry(root, font=("Times new roman", 9, "bold"), bg="#E7E6E6")

        self.nameentry.place(x=30, y=100)

        Button(root, text="change", command=self.reqrem, fg="black").place(x=65, y=150)
        Button(root, text="Back", command=self.faculty_request, fg="black").grid(row=11, column=3)

    def reqrem(self):
        try:
            if self.nameentry.get() == " ":
                print("Faculty Name is required")

            else:
                name = self.nameentry.get()
                if mb.askyesno("Confirm Delete?",f"Are you sure you want to remove request given by  {self.nameentry.get()}?"):
                      con = mc.connect(host="localhost", user="root", passwd="venkat", database="dbms_project")
                      mycursor = con.cursor()
                      name = self.nameentry.get()
                      query = "DELETE FROM request where name = '{}' ".format(name)
                      mycursor.execute(query)
                      con.commit()
                      print("Row Deleted")
                      mb.showinfo("Message",f"Request removed which is given by {self.nameentry.get()}",command = self.delete_request())
                else:
                    return True

        except mc.DatabaseError as e:
            mb.showerror("error in the database", e)
    def Faculty_login(self):
        self.root.title("Faculty Login Page")
        self.root.geometry("380x380")
        self.root.resizable(False, False)

        #background image

        self.bg=ImageTk.PhotoImage(file="att.jpg")
        self.bg_image=Label(self.root, image=self.bg).place(x=0,y=0, relwidth=1, relheight=1)

        #Login Frame

        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=90,y=110, width= 200,height=240)

        #Title & subtitle

        title = Label(Frame_login,text="Login Here",font=("Times new roman",11,"bold"),fg="#6162FF",bg="white").place(x=70,y=20)
        subtitle = Label(Frame_login, text="Faculty login area", font=("Times new roman", 9, "bold"), fg="#1d1d1d",bg="white").place(x=55, y=40)

        #username

        lbl_user=Label(Frame_login,text="Username:",font=("Times new roman",11,"bold"),fg="grey",bg="white").place(x=5,y=65)
        self.username=Entry(Frame_login,font=("Times new roman",9,"bold"),bg="#E7E6E6")
        self.username.place(x=5,y=95,width=170)

        #password

        lbl_password = Label(Frame_login, text="Password:", font=("Times new roman", 11, "bold"), fg="grey", bg="white").place(x=5, y=115)
        self.password = Entry(Frame_login,show = "*", font=("Times new roman", 9, "bold"), bg="#E7E6E6")
        self.password.place(x=5, y=145, width=170)

        #Button
        self.var = IntVar()
        forget=Button(Frame_login, text="forgot?",bd=0,command=self.forgot_pass, font=("Times new roman", 9, "bold"), fg="#6162FF", bg="white").place(x=130, y=165)
        check1 = Checkbutton(Frame_login, text="show password", command=self.show_pass1, variable=self.var, offvalue=0,onvalue=1, font=("Times new roman", 9, "bold"), bd=0, fg="black").place(x=5,y=165)
        submit=Button(Frame_login, text="Login", command=self.check1,font=("Times new roman", 9, "bold"),bd=0, fg="white", bg="blue").place(x=40, y=195)
        register = Button(Frame_login, text="Signup",command=self.Faculty_signup, font=("Times new roman", 9, "bold"),bd=0, fg="white", bg="blue").place(x=110, y=195)
        back = Button(root, text="Back", bd=0, font=("Times new roman", 9, "bold"),fg="white", bg="blue").place(x=10,y=10)

    def forgot_pass(self):
        self.root.title("Add Faculty page")
        self.root.geometry("200x220")
        self.root.resizable(False, False)
        self.bg = ImageTk.PhotoImage(file="request1.png")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        name = Label(root, text="Name:")
        name.place(x=30, y=50)
        newpass = Label(root, text="New password:")
        newpass.place(x=30, y=90)
        confirmpass = Label(root, text="Confirm password:")
        confirmpass.place(x=30, y=130)

        self.name = Entry(root, font=("Times new roman", 9, "bold"), bg="#E7E6E6")
        self.name.place(x=30, y=70)

        self.npass = Entry(root, font=("Times new roman", 9, "bold"), bg="#E7E6E6")
        self.npass.place(x=30, y=110)

        self.cpass = Entry(root, font=("Times new roman", 9, "bold"), bg="#E7E6E6")
        self.cpass.place(x=30, y=150)

        Button(root, text="change", command=self.change_pass, fg="black").place(x=70, y=180)
        Button(root, text="Back", command=self.Faculty_login, fg="black").place(x=10, y=10)

    def change_pass(self):
        try:


            if self.npass.get() == self.cpass.get():
                name = self.name.get()
                npass = self.npass.get()
                cpass = self.cpass.get()
                con = mc.connect(host="localhost", user="root", passwd="venkat", database="dbms_project")
                mycursor = con.cursor()

                sql =  "UPDATE faculty_signup SET passwd = '{}',cpasswd = '{}' WHERE name = '{}';".format(npass,cpass,name)

                mycursor.execute(sql)

                con.commit()
                print(mycursor.rowcount, "Updated Successfully.")

                mb.showinfo("Message", "Password changed",command = self.Faculty_login())


            else:
                    mb.showerror("ERROR","Password doesn't match")

        except mc.DatabaseError as e:
            print("Oracle error",e)
        finally:
            con.close()
            mycursor.close()


    def show_pass1(self):
        if self.var.get() == 1:
            self.password.configure(show= "")
        elif self.var.get() == 0:
            self.password.configure(show = "*")

    def check1(self):
      try:
         name = self.username.get()
         passwd = self.password.get()
         con = mc.connect(host="localhost", user="root", passwd="venkat", database="dbms_project")
         mycursor = con.cursor()
         sql_query = """select name , passwd from faculty_signup where name = %s and passwd = %s"""
         mycursor.execute(sql_query, (name,passwd))
         row = mycursor.fetchone()
         print(row)

         if self.username.get()==" " or self.password.get()== "" :
            mb.showerror("Error","All fields are required")

         elif self.username.get() == row[0]  and self.password.get() == row[1]:
            mb.showinfo("Welcome",f"welcome {self.username.get()}",command = self.ML_page())

         else:
            mb.showerror("Error","Invalid Username or Password")
      except :
          mb.showerror("Error", "Invalid Username or Password")







    def Faculty_signup(self):
        self.root.title("Faculty Login Page")
        self.root.geometry("380x380")
        self.root.resizable(False, False)

        self.bg = ImageTk.PhotoImage(file="att.jpg")
        self.bg_image=Label(self.root, image=self.bg).place(x=0,y=0, relwidth=1, relheight=1)

        Frame_login = Frame(self.root, bg="white")
        Frame_login.place(x=50, y=110, width=290, height=270)


        Label(Frame_login, text="SIGN UP", font="ar 13 bold").place(x = 120, y=20)

        # Fields name

        name = Label(Frame_login, text="username:")
        email = Label(Frame_login, text="email Id:")
        passw = Label(Frame_login, text="Password:")
        cpassw = Label(Frame_login, text="Confirm Pass:")
        facno = Label(Frame_login, text="Faculty ID:")
        phone = Label(Frame_login, text="Phone no:")
        Ad=Label(Frame_login, text="Faculty code:")

        # packing Fields

        name.place(x=20, y=60)
        email.place(x=20, y=80)
        passw.place(x=20, y=100)
        cpassw.place(x=20, y=120)
        facno.place(x=20, y=140)
        phone.place(x=20, y=160)
        Ad.place(x=20, y=180)

        # Creating entry Fields

        self.nameentry = Entry(Frame_login,font=("Times new roman", 9, "bold"), bg="#E7E6E6")
        self.emailentry = Entry(Frame_login, font=("Times new roman", 9, "bold"), bg="#E7E6E6")
        self.passwentry = Entry(Frame_login,show ="*",font=("Times new roman", 9, "bold"), bg="#E7E6E6")
        self.cpasswentry = Entry(Frame_login,show = "*", font=("Times new roman", 9, "bold"), bg="#E7E6E6")
        self.facnoentry = Entry(Frame_login, font=("Times new roman", 9, "bold"), bg="#E7E6E6")
        self.phoneentry = Entry(Frame_login, font=("Times new roman", 9, "bold"), bg="#E7E6E6")
        self.adentry = Entry(Frame_login, font=("Times new roman", 9, "bold"), bg="#E7E6E6")

        # Packing Entry Fields
        self.nameentry.place(x=120, y=60)
        self.emailentry.place(x=120, y=80)
        self.passwentry.place(x=120, y=100)
        self.cpasswentry.place(x=120, y=120)
        self.facnoentry.place(x=120, y=140)
        self.phoneentry.place(x=120, y=160)
        self.adentry.place(x=120, y=180)

        # Creating Checkbox
        self.var = IntVar()
        checkbtn = Checkbutton(Frame_login,command = self.show_pass2,offvalue = 0,onvalue = 1,variable = self.var,text="Show Password")
        checkbtn.place(x=120, y=200)

        # Submit Button
        Button(Frame_login,text="SUBMIT",bd=0, command=self.getvals1,fg="white", bg="blue").place(x=120, y=240)
        Button(root,text="Back",bd=0,command=self.Faculty_login,fg="white", bg="blue").grid(row=11, column=3)


    def show_pass2(self):
        if self.var.get() == 1:
            self.passwentry.configure(show = "")
            self.cpasswentry.configure(show = "")
        elif self.var.get() == 0:
            self.passwentry.configure(show="*")
            self.cpasswentry.configure(show="*")





    def getvals1(self):
        try:
            con = mc.connect(host="localhost", user="root", passwd="venkat", database="dbms_project")
            mycursor = con.cursor()

            if self.passwentry.get() == self.cpasswentry.get():
                if self.adentry.get() == "SRMFACT1822":
                            name = self.nameentry.get()
                            email = self.emailentry.get()
                            passw = self.passwentry.get()
                            cpassw = self.cpasswentry.get()
                            fac_id = self.facnoentry.get()
                            phone = self.phoneentry.get()
                            fac_code =  self.adentry.get()

                            sql = "INSERT INTO  faculty_signup(name,email,passwd,cpasswd,fac_id,phone,Fac_code) VALUES (%s,%s,%s,%s,%s,%s,%s)"
                            val = (name, email, passw,cpassw,fac_id,phone,fac_code)
                            mycursor.execute(sql, val)
                            #sql2 = "INSERT INTO checklist VAlUES ('{}')".format(name)
                            #mycursor.execute(sql2)
                            con.commit()
                            print(mycursor.rowcount, "record inserted.")
                            mb.showinfo("SIGNUP", "Register successfully",command = self.Faculty_login())


                else:
                    mb.showerror("ERROR","Invalid Faculty Code")
            else:
                mb.showerror("ERROR","Password Doesn't Match")
        except mc.DatabaseError as e:
            print("Oracle error",e)
        finally:
            con.close()
            mycursor.close()

    def ML_page(self):
        self.root.title("Faculty Attendance page")
        self.root.geometry("800x500")
        self.root.resizable(False, False)

        self.bg = ImageTk.PhotoImage(file="loginfac.jpg")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        Frame_login = Frame(self.root, bg="white")
        Frame_login.place(x=40, y=140, width=200, height=250)

        Frame_login1 = Frame(self.root, bg="white")
        Frame_login1.place(x=570, y=140, width=200, height=250)

        self.bg1 = ImageTk.PhotoImage(file="qr.png")
        self.bg_image1 = Label(Frame_login, image=self.bg1).place(x=0, y=0)

        self.bg2 = ImageTk.PhotoImage(file="request.jpg")
        self.bg_image2 = Label(Frame_login1, image=self.bg2).place(x=-12, y=0)

        Button(Frame_login, text="Attendance", command=self.attendance, fg="white",bg="#4568dc").place(x=65, y=215)
        Button(root, text="Logout",command=self.Faculty_login, fg="white",bg="#4568dc").grid(row=11, column=3)

        Button(Frame_login1, text="Request",command=self.request, fg="white",bg="#4568dc").place(x=75, y=215)

    def attendance(self):
        cap = cv2.VideoCapture(0)
        cap.set(3, 640)
        cap.set(4, 480)

        i = 0
        while i == 0:
            success, img = cap.read()
            for barcode in decode(img):
                mydata = barcode.data.decode('utf-8')
                print(mydata)

                con = mc.connect(host="localhost", user="root", passwd="venkat", database="dbms_project")
                mycursor = con.cursor()
                sql_query = """select name from checklist where name = %s"""
                mycursor.execute(sql_query, (mydata,))
                row = mycursor.fetchone()

                print("the row is:", row)

                if row is None:
                    myout = "Un-Authorized"
                    mycol = (0, 0, 255)

                else:
                    if mydata in row:
                        myout = "Authorized"
                        mycol = (0, 255, 0)

                    else:
                        myout = "Un-Authorized"
                        mycol = (0, 0, 255)

                if myout == "Authorized":
                    con = mc.connect(host="localhost", user="root", passwd="venkat", database="dbms_project")
                    mycursor = con.cursor()
                    e = mydata
                    b = "Present"
                    c = datetime.now()
                    sql = "INSERT INTO attendance (name, Date_Time,status) VALUES (%s,%s,%s)"
                    val = (e, c, b)
                    mycursor.execute(sql, val)
                    con.commit()
                    print(mycursor.rowcount, "record inserted.")
                    mb.showinfo("Attendance", "Attendance given",command=self.ML_page())
                else:
                    mb.showinfo("Attendance",
                                "Attendance not given and Your name is not in the register so do request Admin to add your name",
                                command=self.ML_page())
                    myout = "Un-Authorized"
                    mycol = (0, 0, 255)
                    pts = np.array([barcode.polygon], np.int32)
                    pts = pts.reshape((-1, 1, 2))
                    cv2.polylines(img, [pts], True, mycol, 5)
                    pts2 = barcode.rect
                    cv2.putText(img, myout, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, mycol, 2)

                pts = np.array([barcode.polygon], np.int32)
                pts = pts.reshape((-1, 1, 2))
                cv2.polylines(img, [pts], True, mycol, 5)
                pts2 = barcode.rect
                cv2.putText(img, myout, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, mycol, 2)
                con = mc.connect(host="localhost", user="root", passwd="venkat", database="dbms_project")

                i = i + 1
                
            cv2.imshow('Result', img)
            cv2.waitKey(4)

    def request(self):
        self.root.title("Request Page")
        self.root.geometry("200x200")
        self.root.resizable(False, False)
        self.bg = ImageTk.PhotoImage(file="request1.png")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        name = Label(root, text="Username:")
        req = Label(root, text="Request:")

        name.place(x=10, y=80)
        req.place(x=10, y=100)

        self.nameentry = Entry(root, font=("Times new roman", 9, "bold"), bg="#E7E6E6")
        self.reqentry = Entry(root, font=("Times new roman", 9, "bold"), bg="#E7E6E6")

        self.nameentry.place(x=70, y=80)
        self.reqentry.place(x=70, y=100)

        Button(root, text="Send Request", command=self.sendrequest, fg="black").place(x=65, y=150)
        Button(root, text="Back",command=self.ML_page, fg="black").grid(row=11, column=3)

    def sendrequest(self):

        if self.nameentry.get() == " " or self.reqentry.get() == "":
            mb.showerror("Error", "All fields are required")
        else:
            con = mc.connect(host="localhost", user="root", passwd="venkat", database="dbms_project")
            mycursor = con.cursor()


            name = self.nameentry.get()
            req = self.reqentry.get()
            sql = "INSERT INTO request (name, request) VALUES (%s,%s)"
            val = (name,req)
            mycursor.execute(sql, val)
            con.commit()
            print(mycursor.rowcount, "record inserted.")
            mb.showinfo("Request", "Request sent to the Admin", command=self.ML_page())




root = Tk()
obj=homepage(root)
root.mainloop()

