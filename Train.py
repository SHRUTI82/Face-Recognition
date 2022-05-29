from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import pymysql
import cv2
import numpy as np
import os

 



class train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("FACE RECOGNITION")


        title_lbl=Label(self.root,text="Train dataset",font=("times new roman",30,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1295,height=45)
        
        img_top=Image.open(r"C:\Users\91921\OneDrive\Pictures\Face images\IMG1.png")
        img_top=img_top.resize((500,130),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=500,height=130)

        b1_1=Button(self.root,text="TRAIN DATA",cursor="hand2",command=self.train_classifier, font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=0,y=350,width=1300,height=30)




        img_bottom=Image.open(r"C:\Users\91921\OneDrive\Pictures\Face images\IMG1.png")
        img_bottom=img_top.resize((500,130),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)
        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=400,width=500,height=130)

    def train_classifier(self):
        data_dir=(r"C:\Users\91921\Downloads\.vscode\.vscode\Programs\Face recognition\data")
    
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]
        for image in path:
            img=Image.open(image).convert('L') #Gray scale
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        
        ids=np.array(ids)

        #_____ Train the classifier______
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training dataset completed")







      



if __name__=="__main__":
    root=Tk()
    obj=train(root)
    root.mainloop()



        