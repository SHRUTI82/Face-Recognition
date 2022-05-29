from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from time import strftime
from datetime import datetime
import pymysql
import cv2
import numpy as np
import os


 



class Face_rec:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("FACE RECOGNITION")

        title_lbl=Label(self.root,text="RECOGNITION ",font=("times new roman",30,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1295,height=45)

        img1=Image.open(r"C:\Users\91921\OneDrive\Pictures\Face images\IMG1.png")
        img1=img1.resize((1530,710),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        Lbl=Label(self.root,image=self.photoimg1)
        Lbl.place(x=0,y=100,width=600,height=700)


        img3=Image.open(r"C:\Users\91921\OneDrive\Pictures\Face images\IMG1.png")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        f_Lbl=Label(self.root,image=self.photoimg3)
        f_Lbl.place(x=650,y=100,width=600,height=700)

        b2_1=Button(self.root,text="Face Recognition",cursor="hand2", command=self.face_r,  font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b2_1.place(x=350,y=455,width=200,height=30)


#___________________attendance

    def mark_attendance(self,i,r,n,d):
        with open(r"C:\Users\91921\Downloads\.vscode\.vscode\Programs\Face recognition\ansh.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list)and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Preset")


#_______Face_recog(self)________

    def face_r(self):
        def draw_boundary(img,classifier,scalefactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scalefactor,minNeighbors)
            coord=[]

            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                idx,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                con=pymysql.connect(host="localhost",user="root",password="YES",database="management")
                my_cursor=con.cursor()
                
                
                my_cursor.execute("select Name from student where id="+str(idx))
                con.commit()
                n=my_cursor.fetchone() 
                print(idx)
                n='+'.join(str(n))

                my_cursor.execute("select id from student where id="+str(idx))
                con.commit()
                r=my_cursor.fetchone()
               
                r='+'.join(str(r))

                my_cursor.execute("select dep from student where id="+str(idx))
                d=my_cursor.fetchone()
                d='+'.join(str(d))

                my_cursor.execute("select year from student where id="+str(idx))
                i=my_cursor.fetchone()
                i='+'.join(str(i))

                print(n)

                if confidence>77:
                    cv2.putText(img,f"Name:{n}",(x,y-65),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"ID:{r}",(x,y-45),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-25),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Year:{i}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d)                
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,f"Unkown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,h]
            
            return coord

        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier(r"C:\Users\91921\Downloads\.vscode\.vscode\Programs\Face recognition\haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read(r"C:\Users\91921\Downloads\.vscode\.vscode\Programs\classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to face recognition",img)
            
            if cv2.waitKey(1)==13:
                break
            
        video_cap.release()
        cv2.destroyAllWindows()











if __name__=="__main__":
    root=Tk()
    obj=Face_rec(root)
    root.mainloop()
