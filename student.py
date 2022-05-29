from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import pymysql
import cv2





class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("FACE RECOGNITION")

        

        # _________Variables___
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        
        
        self.var_email=StringVar()
        self.var_phone=StringVar()
        
        


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


        img3=Image.open(r"C:\Users\91921\OneDrive\Pictures\Face images\IMG1.png")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3) 
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1300,height=450)

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",30,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1295,height=45)


        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=0,y=50,width=1400,height=650)

        # left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=600,height=700)
        
        img_left=Image.open(r"C:\Users\91921\OneDrive\Pictures\Face images\IMG1.png")
        img_left=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        f_lbl=Label(self.root,image=self.photoimg_left)
        f_lbl.place(x=1000,y=0,width=500,height=130)

        # current course
        current_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current course information",font=("times new roman",12,"bold"))
        current_frame.place(x=10,y=10,width=600,height=110)
        # Department
        dep_label=Label(current_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=5,sticky=W)

        dep_combo=ttk.Combobox(current_frame,textvariable=self.var_dep, font=("times new roman",12,"bold"),state="read only")
        dep_combo["values"]=("Select Department","Computer","IT","Civil","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        
        # Course
        course_label=Label(current_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=5,sticky=W)

        course_combo=ttk.Combobox(current_frame,textvariable=self.var_course, font=("times new roman",12,"bold"),state="read only")
        course_combo["values"]=("Select Course","EE","PH","HS","CS")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

       # Year
        year_label=Label(current_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_frame,textvariable=self.var_year, font=("times new roman",12,"bold"),state="read only")
        year_combo["values"]=("Select Year","2018","2019","2020","2021")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        # Semester
        semester_label=Label(current_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=6,sticky=W)

        semester_combo=ttk.Combobox(current_frame,textvariable=self.var_semester, font=("times new roman",12,"bold"),state="read only")
        semester_combo["values"]=("Select Semester","1","2","3","4","5","6","7","8")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        # Student information
        class_student_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=25,y=160,width=750,height=400)

        student_name_label=Label(class_student_frame, text=" Name",font=("times new roman",12,"bold"),bg="white")
        student_name_label.grid(row=0,column=0,padx=10,sticky=W)

        student_name_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name , width=20,font=("times new roman",13,"bold"))
        student_name_entry.grid(row=0,column=2,padx=20,sticky=W)

       

        studentId_label=Label(class_student_frame,text="Entry number",font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=1,column=0,padx=10,sticky=W)

        studentId_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id, width=20,font=("times new roman",13,"bold"))
        studentId_entry.grid(row=1,column=2,padx=20,pady=5,sticky=W)


        student_phone_label=Label(class_student_frame,text="Phone number",font=("times new roman",12,"bold"),bg="white")
        student_phone_label.grid(row=2,column=0,padx=10,sticky=W)

        student_phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone, width=20,font=("times new roman",13,"bold"))
        student_phone_entry.grid(row=2,column=2,padx=20,pady=5,sticky=W)

        student_email_label=Label(class_student_frame,text="Email",font=("times new roman",12,"bold"),bg="white")
        student_email_label.grid(row=3,column=0,padx=10,sticky=W)

        student_email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email, width=20,font=("times new roman",13,"bold"))
        student_email_entry.grid(row=3,column=2,padx=20,pady=5,sticky=W)





        
        

        
        # right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=600,y=10,width=660,height=700)

        #radio buttons
        self.var_radio1=StringVar()
        radio1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1 ,text="Take Photo Sample",value="Yes")
        radio1.grid(row=7,column=0)

        self.var_radio2=StringVar()
        radio2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1 ,text="No Photo Sample",value="Notextvariable=self.var_radio1 ")
        radio2.grid(row=7,column=2)

        #buttons frame
        bt_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        bt_frame.place(x=0,y=160,width=600,height=35)

        save_btn=Button(bt_frame,text="Save",command=self.add_data, width=7,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(bt_frame,text="Update",command=self.update_data ,width=8,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(bt_frame,text="Delete",command=self.delete_data, width=8,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(bt_frame,text="Reset",command=self.reset_data, width=8,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)
        
        take_photo_btn=Button(bt_frame,text="Take photo",command=self.generate_dataset,width=10,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=4)

        take_photo_btn=Button(bt_frame,text="Update photo",width=10,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=5)
        
        img_right=Image.open(r"C:\Users\91921\OneDrive\Pictures\Face images\IMG1.png")
        img_right=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)
        f_lbl=Label(self.root,image=self.photoimg_right)
        f_lbl.place(x=0,y=0,width=500,height=130)

        

        #gggggggg Table frame*
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=22,width=640,height=350)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","email","phone"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
      
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="ID")
        self.student_table.heading("name",text="Name")
        #self.student_table.heading("gender",text="Gender")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
       # self.student_table.heading("photo",text="Photo")
       
        self.student_table.column("dep",width=100)

      
        self.student_table.pack(fill=BOTH,expand=2)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
      

#_________________Generate data set or take photo samples__________________ 

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="YES",database="management")
                my_cursor=con.cursor()
                my_cursor.execute("Insert into student values(%s,%s,%s,%s,%s,%s,%s,%s)",    (
                                                                                                self.var_dep.get(),
                                                                                                self.var_course.get(),
                                                                                                self.var_year.get(),
                                                                                              # self.var_roll.get(),
                                                                                                self.var_semester.get(),
                                                                                                self.var_std_id.get(),
                                                                                                self.var_std_name.get(),
                                                                                                
                                                                                              #  self.var_gender.get(),
                                                                                                self.var_email.get(),
                                                                                                self.var_phone.get(),
                                                                                             #   self.var_dob.get(),
                                                                                            ))
                con.commit()
                self.fetch_data()
                con.close()
                message.box.showinfo("Success","Student details has been added successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)          


        #..........Fetch dta_________
    def fetch_data(self):
        con=pymysql.connect(host="localhost",user="root",password="YES",database="management")
        my_cursor=con.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            con.commit()
        con.close()

    #____get cursor___
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]), 
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_phone.set(data[6]),
        self.var_email.set(data[7]),
        self.var_radio1.set()
    # update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                update=messagebox.askyesno("Update","Do you want to update ",parent=self.root)
                if update>0:
                    con=pymysql.connect(host="localhost",user="root",password="YES",database="management")
                    my_cursor=con.cursor()
                    my_cursor.execute("update student set  dep=%s, course=%s, year=%s,semester =%s,name=%s,email=%s,phone=%s where id=%s",(
                                                                                                                                    self.var_dep.get(),
                                                                                                                                    self.var_course.get(),
                                                                                                                                    self.var_year.get(),
                                                                                              #                                     self.var_roll.get(),
                                                                                                                                    self.var_semester.get(),
                                                                                                                                    self.var_std_name.get(),
                                                                                                                                    
                                                                                              #                                     self.var_gender.get(),
                                                                                                                                    self.var_email.get(),
                                                                                                                                    self.var_phone.get(),
                                                                                                                                    self.var_std_id.get(),
                                                                                             #                                      self.var_dob.get(),
                                                                                                                                ))
                else:
                    if not update:
                        return
                messagebox.showinfo("Success","Student details successfully update ", parent=self.root)
                con.commit()
                self.fetch_data()
                con.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}",parent=self.root)
                    
    #_____delete function
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delet=messagebox.askyesno("Student Delete page","Do you want to delete",parent=self.root)
                if delet>0:
                    con=pymysql.connect(host="localhost",user="root",password="YES",database="management")
                    my_cursor=con.cursor()
                    my_cursor.execute("delete from student where id=%s", self.var_std_id.get())
                else:
                    if not delet:
                        return
                con.commit()
                self.fetch_data()
                con.close()
                messagebox.showinfo("Delete","Successfully deleted student deleted",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}",parent=self.root)
            
    #_____reset
    def reset_data(self):
        self.var_dep.set("Select Department"),
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"), 
        self.var_semester.set("Select Semester"),
        self.var_std_id.set(""),
        self.var_std_name.set(""),
        self.var_phone.set(""),
        self.var_email.set(""),
        self.var_radio1.set("")
                    
       
#___________Generate data set or photo samples
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
                messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="YES",database="management")
                my_cursor=con.cursor()
                my_cursor.execute("select *from student")
                myresult=my_cursor.fetchall()
                idi=0
                for x in myresult:
                    idi+=1
                my_cursor.execute("update student set  dep=%s, course=%s, year=%s,semester =%s,name=%s,email=%s,phone=%s where id=%s",(
                                                                                                                                        self.var_dep.get(),
                                                                                                                                        self.var_course.get(),
                                                                                                                                        self.var_year.get(),
                                                                                            #                                         self.var_roll.get(),
                                                                                                                                        self.var_semester.get(),
                                                                                                                                        self.var_std_name.get(),
                                                                                                                                    
                                                                                            #                                         self.var_gender.get(),
                                                                                                                                        self.var_email.get(),
                                                                                                                                        self.var_phone.get(),
                                                                                                                                        self.var_std_id.get()==idi
                                                                                            #                                          self.var_dob.get(),
                                                                                                                                    ))
                                                                                                                                    
                con.commit()
                self.fetch_data()
                self.reset_data()
                con.close()
        #_____Load predefined data on face frontals from opencv_________-

                face_classifier=cv2.CascadeClassifier(r"C:\Users\91921\Downloads\.vscode\.vscode\Programs\Face recognition\haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    # scaling factor=1.3 , Minimum neighbour=5

                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="C:/Users/91921/Downloads/.vscode/.vscode/Programs/Face recognition/data/user."+ str(idi) + "." + str(img_id) +".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Fce",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed")
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}",parent=self.root)








        




if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()










  