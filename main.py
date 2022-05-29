from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
import tkinter
from student import Student
from Train import train
from face_recog import Face_rec
from help import Help
import pymysql



class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("FACE RECOGNITION")
        

        img=Image.open(r"C:\Users\91921\OneDrive\Pictures\Face images\IMG1.png")
        img=img.resize((500,130),Image.ANTIALIAS)         
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        
        img1=Image.open(r"C:\Users\91921\OneDrive\Pictures\Face images\IMG1.png")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)


        img2=Image.open(r"C:\Users\91921\OneDrive\Pictures\Face images\IMG1.png")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=130)


        #background
        img3=Image.open(r"C:\Users\91921\OneDrive\Pictures\Face images\IMG1.png")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1300,height=450)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSYTEM SOFT/WARE ",font=("times new roman",30,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1295,height=45)

        #student button
        img4=Image.open(r"C:\Users\91921\OneDrive\Pictures\Face images\IMG1.png")
        img4=img4.resize((1530,710),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=200,height=220)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=200,y=300,width=140,height=30)

        #button2 detect face
        img5=Image.open(r"C:\Users\91921\OneDrive\Pictures\Face images\IMG1.png")
        img5=img5.resize((1530,710),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b2=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.open_img)
        b2.place(x=510,y=100,width=200,height=220)

        b2_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img, font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b2_1.place(x=510,y=300,width=140,height=30)

        #button3 detect face
        img6=Image.open(r"C:\Users\91921\OneDrive\Pictures\Face images\IMG1.png")
        img6=img6.resize((1530,710),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img4)

        b3=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.face_data )
        b3.place(x=850,y=100,width=200,height=220)

        b3_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data, font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b3_1.place(x=850,y=300,width=140,height=30)


        b4_1=Button(bg_img,text="Train data",cursor="hand2",command=self.train_data, font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b4_1.place(x=450,y=360,width=140,height=30)



        

    def open_img(self):
        os.startfile(r"C:\Users\91921\Downloads\.vscode\.vscode\Programs\Face recognition\data")

        #44444444444444444444444444444444444 Function buttons$$$$$$$$$$$$

    def student_details(self):
        self.new_window=Toplevel(self.root)
        
        self.app=Student(self.new_window)

    
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=train(self.new_window)
    
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_rec(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=train(self.new_window)

    
  
       
       







      



if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()

