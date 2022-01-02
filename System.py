from tkinter import *
from tkinter import messagebox as msgx
from ExcelData import *
from classes import Student, Lecturer
import sys
from Capture_QR_Code import Decode_QR_Code

from Check_Student_QR_Code import Main_Check_QR_Code
from Detect_Mask_Video import Main_Check_Mask
from Face_Recognition_Folder.Face_Recognition import Main_Face_Reco

class CollegeSystem(object):
    def __init__(self, parent):
        self.students = []
        self.lecturers = []
        self.root = parent
        self.root.resizable(0, 0)

        def disable_event():
            msgx.showerror("Exit warning Window","Exit is Allowed only from Exit Button")

        self.root.protocol("WM_DELETE_WINDOW", disable_event)

        canvas = Canvas(width=479, height=200)
        canvas.pack()  # create canvas to hold the image
        self.welImg = PhotoImage(file='logo.png')  # load the image
        canvas.create_image(0, 0, image=self.welImg, anchor=NW)


        self.addImg = PhotoImage(file='add.png')
        AddButton = Button(self.root,activebackground='green',bd=4, relief="sunken", text="Add", padx=15, pady=10, image=self.addImg, command=self.AddManager).place(x=80, y=200)
        My_label1 = Label(self.root, text="Add New Student", padx=24, bg='green', fg='white').place(x=80, y=340)

        self.checkImg = PhotoImage(file='check.png')
        CheckButton = Button(self.root,activebackground='green',bd=4, relief="sunken", text="Check", padx=15, pady=10, image=self.checkImg, command=self.CheckManager).place(x=580, y=200)
        My_label1 = Label(self.root, text="Check To Pass    ", padx=24, bg='green', fg='white').place(x=580, y=340)

        self.delImg = PhotoImage(file='del.gif')
        DeleteButton = Button(self.root, activebackground='green',bd=4, relief="sunken",text="Delete", padx=15, pady=10, image=self.delImg, command=self.DeleteManager).place(x=80, y=400)
        My_label1 = Label(self.root, text="Delete A Person", padx=24, bg='red', fg='white').place(x=80, y=540)

        self.viewImg = PhotoImage(file='view.gif')
        ViewButton = Button(self.root,activebackground='green',bd=4, relief="sunken", text="View", padx=15,  pady=10, image=self.viewImg ,command=self.ShowManager).place(x=580, y=400)
        My_label1 = Label(self.root, text="      View Data      ", padx=24, bg='green', fg='white').place(x=580, y=540)

        self.exitImg = PhotoImage(file='exit.gif')
        ExitButton = Button(self.root,activebackground='red',bd=4, relief="sunken", text="Exit From College Pass System", image=self.exitImg ,padx=20, pady=10, command=self.ExitManager).place(x=320, y=300)
        My_label1 = Label(self.root, text="Exit of Program  ", padx=24, bg='red', fg='white').place(x=320, y=440)

    def AddManager(self):
        self.root.withdraw()

        QuesFrame = Toplevel()
        QuesFrame.resizable(0, 0)
        QuesFrame.geometry("300x150")
        QuesFrame.title("Question Manager")
        QuesFrame.configure(background="maroon")
        QuesLabel = Label(QuesFrame, text="Choose your classification", fg="maroon", width=30, height=1).place(x=40, y=20)
        isStudent = Button(QuesFrame, text='Student', bg='green', fg='yellow', command=lambda m='std': Add(m)).place(x=60, y=60)
        isLecturer = Button(QuesFrame, text='Lecturer', bg='green', fg='yellow', command=lambda m='lec': Add(m)).place(x=160, y=60)
        
        def Add(which):
            ID = Decode_QR_Code()
            if ID == False:
                QuesFrame.destroy()
                self.CloseThisFrame()
            elif ID != False:
                QuesFrame.destroy()
                AddFrame = Toplevel()
                AddFrame.geometry("600x400")
                AddFrame.title("Adding Frame Manager")
                AddFrame.configure(background="maroon")

                Cge_IdLabel = Label(AddFrame, text="College Id : ", fg="maroon", width=20, height=1).place(x=10, y=90)
                Cge_IdInput = StringVar(self.root, value=ID)
                Cge_IdEntry = Entry(AddFrame, textvariable=Cge_IdInput, fg="blue", width=30, state='disabled',foreground='white').place(x=200, y=90)

                NameLabel = Label(AddFrame, text="Name : ", fg="maroon", width=20, height=1).place(x=10, y=10)
                nameInput = StringVar()
                NameEntry = Entry(AddFrame, textvariable=nameInput, fg="blue", width=30).place(x= 200, y=10)

                Nat_IdLabel = Label(AddFrame, text="National Id : ", fg="maroon", width=20, height=1).place(x=10, y=50)
                Nat_IdInput = StringVar()
                Nat_IdEntry = Entry(AddFrame, textvariable=Nat_IdInput, fg="blue", width=30).place(x= 200, y=50)

                DepLabel = Label(AddFrame, text="Department : ", fg="maroon", width=20, height=1).place(x=10, y=130)
                DepInput = StringVar()
                DepEntry = Entry(AddFrame, textvariable=DepInput, fg="blue", width=30).place(x= 200, y=130)

                IsVacLabel = Label(AddFrame, text="Is Vaccinated : ", fg="maroon", width=20, height=1).place(x=10, y=170)
                isVac = IntVar()
                TrueVac = Radiobutton(AddFrame, text='YES', variable=isVac, value=1).place(x=200, y=170)
                FalseVac = Radiobutton(AddFrame, text='NO', variable=isVac, value=2).place(x=300, y=170)

                if which == 'std':
                    Curr_yearLabel = Label(AddFrame, text="Current Grade : ", fg="maroon", width=20, height=1).place(x=10, y=210)
                    Curr_yearInput = StringVar()
                    Curr_yearEntry = Entry(AddFrame, textvariable=Curr_yearInput, fg="blue", width=30).place(x= 200, y=210)

                    Grade_yearLabel = Label(AddFrame, text="Graduation year : ", fg="maroon", width=20, height=1).place(x=10, y=250)
                    Grade_yearInput = StringVar()
                    Grade_yearEntry = Entry(AddFrame, textvariable=Grade_yearInput, fg="blue", width=30).place(x= 200, y=250)

                    CatgLabel = Label(AddFrame, text="Category : ", fg="maroon", width=20, height=1).place(x=10, y=290)
                    Catg = IntVar()
                    mainStream = Radiobutton(AddFrame, text='Main Stream', variable=Catg, value=1).place(x=200, y=290)
                    credit = Radiobutton(AddFrame, text='Credit', variable=Catg, value=2).place(x=300, y=290)

                elif which == 'lec':
                    SpecLabel = Label(AddFrame, text="Speciality : ", fg="maroon", width=20, height=1).place(x=10, y=210)
                    SpecInput = StringVar()
                    SpecEntry = Entry(AddFrame, textvariable=SpecInput, fg="blue", width=30).place(x= 200, y=210)

                    Src_UnvLabel = Label(AddFrame, text="Source University : ", fg="maroon", width=20, height=1).place(x=10, y=250)
                    Src_UnvInput = StringVar()
                    Src_UnvEntry = Entry(AddFrame, textvariable=Src_UnvInput, fg="blue", width=30).place(x= 200, y=250)

                handler = lambda: self.CloseThisFrame(AddFrame)
                def saveData():
                    if which == 'std' :
                        vac = '' ; catg = ''
                        if isVac.get() == 1 : vac = 'vaccinated'
                        elif isVac.get() == 2 : vac = 'not vaccinated'
                        if Catg.get() == 1 : catg = 'Main Stream'
                        elif Catg.get() == 2 : catg = 'Credit'
                        new_std = Student(nameInput.get(), Nat_IdInput.get(), Cge_IdInput.get(), DepInput.get(), vac, Curr_yearInput.get(), Grade_yearInput.get(), catg)
                        self.students.append(new_std)
                        new_row = [nameInput.get(), Nat_IdInput.get(), Cge_IdInput.get(), DepInput.get(), vac, Curr_yearInput.get(), Grade_yearInput.get(), catg]
                    elif which == 'lec':
                        vac = ''
                        if isVac.get() == 1 : vac = 'vaccinated'
                        elif isVac.get() == 2 : vac = 'not vaccinated'
                        new_lec = Lecturer(nameInput.get(), Nat_IdInput.get(), Cge_IdInput.get(), DepInput.get(), vac, SpecInput.get(), Src_UnvInput.get())
                        self.lecturers.append(new_lec)
                        new_row = [nameInput.get(), Nat_IdInput.get(), Cge_IdInput.get(), DepInput.get(), vac, SpecInput.get(), Src_UnvInput.get()]
                    AddExcel(which, new_row)
                    msgx.showinfo('Saving Message', 'Your Data have successfully been recorded')
                    handler()
                SaveButton = Button(AddFrame, text="Save", fg='yellow', bg='light blue', command=saveData).place(x=100, y=330)
                CancelButton = Button(AddFrame, text="Cancel", fg='yellow', bg='light blue', command=handler).place(x=300, y=330)
        
    def CheckManager(self):

        def Check_QR_Code():
            Condition1 = Main_Check_QR_Code()

        def Face_Recognition():
            Condition2 = Main_Face_Reco()

        def Mask_Detection():
            Condition3 = Main_Check_Mask()

        self.root.withdraw()
        CheckFrame = Toplevel()
        CheckFrame.resizable(0, 0)
        def disable_event():
            msgx.showerror("Exit warning Window", "Exit is Allowed only from Exit Button")

        CheckFrame.protocol("WM_DELETE_WINDOW", disable_event)

        checkImg = PhotoImage(file='logo_check.png')  # load the image
        My_label1 = Label(CheckFrame,image=checkImg ,padx=24, bg='grey', fg='black').pack()

        CheckFrame.geometry("700x600")
        CheckFrame.configure(background="#17ad9e")
        CheckFrame.title("Pass this 3 Stages To Enter The College")
        face_recImg = PhotoImage(file='face_rec.gif')
        faceButton = Button(CheckFrame, activebackground='black', bd=4, relief="sunken", text="Check", padx=15, pady=10,
                            image=face_recImg, command=Face_Recognition).place(x=60, y=250)
        My_label1 = Label(CheckFrame, text="Face Recognition", padx=24, bg='grey', fg='black').place(x=60, y=390)

        QRImg = PhotoImage(file='qr_code.gif')
        QRButton = Button(CheckFrame, activebackground='blue', bd=4, relief="sunken", text="Delete", padx=15,
                          pady=10, image=QRImg, command=Check_QR_Code).place(x=280, y=250)
        My_label2 = Label(CheckFrame, text="Check QR-Code", padx=24, bg="#1865de", fg='white').place(x=280, y=390)

        maskImg = PhotoImage(file='mask.gif')
        maskButton = Button(CheckFrame, activebackground='green', bd=4, relief="sunken", text="View", padx=15, pady=10,
                            image=maskImg, command=Mask_Detection).place(x=490, y=250)
        My_label3 = Label(CheckFrame, text="  Mask Detection  ", padx=24, bg='green', fg='white').place(x=490,y=390)

        backImg = PhotoImage(file='back2.gif')
        handler = lambda f=CheckFrame: self.CloseThisFrame(f)
        backButton = Button(CheckFrame, activebackground='yellow', image=backImg, bd=4, relief="sunken", text="Back", padx=15, pady=10,
                            command=handler).place(x=280, y=430)
        My_label4 = Label(CheckFrame, text="           Back          ", padx=24, bg='#f5da0f', fg='black').place(x=280,y=570)
        CheckFrame.mainloop()


    def DeleteManager(self):
        self.root.withdraw()

        ID = Decode_QR_Code()
        if ID == False:
            self.CloseThisFrame()
        else:
            if ID[0:4] == '2166':
                DeleteExcel('std', ID)
            else:
                DeleteExcel('lec', ID)
            self.CloseThisFrame()


    def ShowManager(self):
        which = ''
        self.root.withdraw()

        ID = Decode_QR_Code()
        if ID == False:

            self.CloseThisFrame()
        else:
            if ID[0:4] == '2166':
                which = 'std'
                data = ShowExcel('std', ID)
            else:
                which = 'lec'
                data = ShowExcel('lec', ID)
            self.CloseThisFrame()
            if data != 0 :
                ShowFrame = Toplevel()
                ShowFrame.geometry("400x300")
                ShowFrame.title("Show Frame Manager")
                ShowFrame.configure(background="maroon")

                lb1 = Label(ShowFrame, text='Name', bg='light blue').place(x=50, y=10)
                lb2 = Label(ShowFrame, text=data['Name'], bg='light green').place(x=200, y=10)
                lb3 = Label(ShowFrame, text='National Id', bg='light blue').place(x=50, y=40)
                lb4 = Label(ShowFrame, text=data['National Id'], bg='light green').place(x=200, y=40)
                lb5 = Label(ShowFrame, text='College Id', bg='light blue').place(x=50, y=70)
                lb6 = Label(ShowFrame, text=data['College Id'], bg='light green').place(x=200, y=70)
                lb7 = Label(ShowFrame, text='Departement', bg='light blue').place(x=50, y=100)
                lb8 = Label(ShowFrame, text=data['Departement'], bg='light green').place(x=200, y=100)
                lb9 = Label(ShowFrame, text='Vaccination State', bg='light blue').place(x=50, y=130)
                lb10 = Label(ShowFrame, text=data['Vaccination State'], bg='light green').place(x=200, y=130)
                if which == 'std':
                    lb11 = Label(ShowFrame, text='Current Year', bg='light blue').place(x=50, y=160)
                    lb12 = Label(ShowFrame, text=data['Current Year'], bg='light green').place(x=200, y=160)
                    lb13 = Label(ShowFrame, text='Graduation Year', bg='light blue').place(x=50, y=190)
                    lb14 = Label(ShowFrame, text=data['Graduation Year'], bg='light green').place(x=200, y=190)
                    lb15 = Label(ShowFrame, text='Category', bg='light blue').place(x=50, y=220)
                    lb16 = Label(ShowFrame, text=data['Category'], bg='light green').place(x=200, y=220)
                elif which == 'lec':
                    lb11 = Label(ShowFrame, text='Speciality', bg='light blue').place(x=50, y=160)
                    lb12 = Label(ShowFrame, text=data['Speciality'], bg='light green').place(x=200, y=160)
                    lb13 = Label(ShowFrame, text='Source University', bg='light blue').place(x=50, y=190)
                    lb14 = Label(ShowFrame, text=data['Source University'], bg='light green').place(x=200, y=190)

                handler2 = lambda: self.CloseThisFrame(ShowFrame)
                ShowButton = Button(ShowFrame, text="OK",width=30 , bg='yellow', fg='black', command=handler2).place(x=100, y=250)
            else:
                self.CloseThisFrame()


    def ExitManager(self):
        self.root.withdraw()
        ExitFrame = Toplevel()
        ExitFrame.geometry("400x300")
        ExitFrame.title("Exit Frame Manager")
        ExitFrame.configure(background="maroon")
        def disable_event():
            msgx.showerror("Exit warning Window", "Exit is Allowed only from Close Button")

        ExitFrame.protocol("WM_DELETE_WINDOW", disable_event)
        ExitFrame.resizable(0, 0)

        lb1 = Label(ExitFrame, text='Team Members',bg='black', fg='gold' , width=40).place(x=70, y=10)
        lb2 = Label(ExitFrame, text='Ammar Mohamed', bg='light blue').place(x=70, y=50)
        lb3 = Label(ExitFrame, text='Michael Mettry', bg='light blue').place(x=240, y=50)
        lb4 = Label(ExitFrame, text='Mohamed Mamdouh', bg='light blue').place(x=70, y=80)
        lb5 = Label(ExitFrame, text='Mustafa Shoman', bg='light blue').place(x=240, y=80)
        lb6 = Label(ExitFrame, text='Mustafa Arabi', bg='light blue').place(x=70, y=110)
        lb7 = Label(ExitFrame, text='Mohamed Naser', bg='light blue').place(x=240, y=110)
        lb8 = Label(ExitFrame, text='Course Lecturers',bg='black', fg='gold' , width=40).place(x=70, y=150)
        lb8 = Label(ExitFrame, text='Dr. Sabah', bg='light blue').place(x=90, y=190)
        lb9 = Label(ExitFrame, text='Eng. Mahmoud Taha', bg='light blue').place(x=200, y=190)

        def EndSystem(thisFrame):
            thisFrame.destroy()
            sys.exit()
        ExitButton = Button(ExitFrame, text="Close",width=30 , bg='yellow', fg='black', command=lambda : EndSystem(ExitFrame)).place(x=100, y=250)

    def CloseThisFrame(self, ThisFrame=None):
        if ThisFrame != None :
            ThisFrame.destroy()
        self.root.update()
        self.root.deiconify()