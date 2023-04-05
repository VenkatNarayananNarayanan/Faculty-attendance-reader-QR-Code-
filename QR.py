import cv2
import numpy as np
import tkinter.messagebox as mb
from pyzbar.pyzbar import decode
import cx_Oracle as cx
import mysql.connector as mc
from datetime import datetime

#img = cv2.imread('EnjoyEnjammi.png')
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

#with open('mydatafile.text') as f:
  #  mydatalist = f.read().splitlines()

i=0
while i==0:
    success,img = cap.read()
    for barcode in decode(img):
        mydata = barcode.data.decode('utf-8')
        print(mydata)

        con = mc.connect(host="localhost", user="root", passwd="venkat", database="dbms_project")
        mycursor = con.cursor()
        sql_query = """select * from test where name = %s"""
        mycursor.execute(sql_query,(mydata,))
        row = mycursor.fetchone()

        print("the row is:",row)
        
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
            mb.showinfo("Attendance", "Attendance given")
        else:
            mb.showinfo("Attendance", "Attendance not given and Your name is not in the register so do request Admin to add your name")

        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,mycol,5)
        pts2 = barcode.rect
        cv2.putText(img,myout,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,0.5,mycol,2)
        con = mc.connect(host="localhost", user="root", passwd="venkat", database="dbms_project")


        i=i+1

    cv2.imshow('Result',img)
    cv2.waitKey(4)






