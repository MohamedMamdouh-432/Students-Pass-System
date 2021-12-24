from tkinter import *
from tkinter import messagebox as msgx
from ExcelData import *
from classes import Student, Lecturer
import sys

class CollegeSystem(object):
    def __init__(self, parent):
        self.students = []
        self.lecturers = []
        self.root = parent

        AddButton = Button(self.root, text="Add", bg='green', fg='yellow', padx=15, pady=10, command=self.AddManager).place(x=80, y=200)
        CheckButton = Button(self.root, text="Check", bg='green', fg='yellow', padx=15, pady=10, command=self.CheckManager).place(x=180, y=200)
        DeleteButton = Button(self.root, text="Delete", bg='green', fg='yellow', padx=15, pady=10, command=self.DeleteManager).place(x=280, y=200)
        ShowButton = Button(self.root, text="Show", padx=15, bg='green', fg='yellow', pady=10, command=self.ShowManager).place(x=380, y=200)
        ExitButton = Button(self.root, text="Exit From College Pass System",  bg='yellow', fg='black', padx=20, pady=10, command=self.ExitManager).place(x=180, y=300)

    def AddManager(self):
        self.root.withdraw()

        QuesFrame = Toplevel()
        QuesFrame.geometry("300x150")
        QuesFrame.title("Question Manager")
        QuesFrame.configure(background="maroon")
        QuesLabel = Label(QuesFrame, text="Choose your classification", fg="maroon", width=30, height=1).place(x=40, y=20)
        isStudent = Button(QuesFrame, text='Student', bg='green', fg='yellow', command=lambda m='std': Add(m)).place(x=60, y=60)
        isLecturer = Button(QuesFrame, text='Lecturer', bg='green', fg='yellow', command=lambda m='lec': Add(m)).place(x=160, y=60)
        
        def Add(which):
            QuesFrame.destroy()
            AddFrame = Toplevel()
            AddFrame.geometry("600x400")
            AddFrame.title("Adding Frame Manager")
            AddFrame.configure(background="maroon")

            NameLabel = Label(AddFrame, text="Name : ", fg="maroon", width=20, height=1).place(x=10, y=10)
            nameInput = StringVar()
            NameEntry = Entry(AddFrame, textvariable=nameInput, fg="blue", width=30).place(x= 200, y=10)

            Nat_IdLabel = Label(AddFrame, text="National Id : ", fg="maroon", width=20, height=1).place(x=10, y=50)
            Nat_IdInput = StringVar()
            Nat_IdEntry = Entry(AddFrame, textvariable=Nat_IdInput, fg="blue", width=30).place(x= 200, y=50)

            Cge_IdLabel = Label(AddFrame, text="College Id : ", fg="maroon", width=20, height=1).place(x=10, y=90)
            Cge_IdInput = StringVar()
            Cge_IdEntry = Entry(AddFrame, textvariable=Cge_IdInput, fg="blue", width=30).place(x= 200, y=90)

            DepLabel = Label(AddFrame, text="Departement : ", fg="maroon", width=20, height=1).place(x=10, y=130)
            DepInput = StringVar()
            DepEntry = Entry(AddFrame, textvariable=DepInput, fg="blue", width=30).place(x= 200, y=130)

            IsVacLabel = Label(AddFrame, text="Is Vaccinated : ", fg="maroon", width=20, height=1).place(x=10, y=170)
            isVac = IntVar()
            TrueVac = Radiobutton(AddFrame, text='True', variable=isVac, value=1).place(x=200, y=170)
            FalseVac = Radiobutton(AddFrame, text='False', variable=isVac, value=2).place(x=300, y=170)

            if which == 'std' :
                Curr_yearLabel = Label(AddFrame, text="Current year : ", fg="maroon", width=20, height=1).place(x=10, y=210)
                Curr_yearInput = StringVar()
                Curr_yearEntry = Entry(AddFrame, textvariable=Curr_year, fg="blue", width=30).place(x= 200, y=210)

                Grade_yearLabel = Label(AddFrame, text="Grade year : ", fg="maroon", width=20, height=1).place(x=10, y=250)
                Grade_yearInput = StringVar()
                Grade_yearEntry = Entry(AddFrame, textvariable=Grade_yearInput, fg="blue", width=30).place(x= 200, y=250)

                CatgLabel = Label(AddFrame, text="Category : ", fg="maroon", width=20, height=1).place(x=10, y=290)
                Catg = IntVar()
                mainStream = Radiobutton(AddFrame, text='Main Stream', variable=Catg, value=1).place(x=200, y=290)
                credit = Radiobutton(AddFrame, text='Credit', variable=Catg, value=2).place(x=300, y=290)
                
            elif which == 'lec' :
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
                    if Kind.get() == 1 : catg = 'Main Stream'
                    elif Kind.get() == 2 : catg = 'Credit'
                    new_std = Student(nameInput.get(), Nat_IdInput.get(), Cge_IdInput.get(), DepInput.get(), vac, GradeInput.get(), Grade_yearInput.get(), catg)
                    self.students.append(new_std)
                    new_row = [nameInput.get(), Nat_IdInput.get(), Cge_IdInput.get(), DepInput.get(), vac, GradeInput.get(), Grade_yearInput.get(), catg]
                elif which == 'lec' :
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
        self.root.withdraw()
        QuesFrame = Toplevel()
        QuesFrame.geometry("300x150")
        QuesFrame.title("Question Manager")
        QuesFrame.configure(background="maroon")
        QuesLabel = Label(QuesFrame, text="Choose your classification", fg="maroon", width=30, height=1).place(x=40, y=20)
        isStudent = Button(QuesFrame, text='Student', bg='green', fg='yellow', command=lambda m='std': Check(m)).place(x=60, y=60)
        isLecturer = Button(QuesFrame, text='Lecturer', bg='green', fg='yellow', command=lambda m='lec': Check(m)).place(x=160, y=60)
        
        def Check(which):
            QuesFrame.destroy()
            id = '21665749'
            CheckExcel(which, id)
            self.root.update()
            self.root.deiconify()

    def DeleteManager(self):
        self.root.withdraw()
        QuesFrame = Toplevel()
        QuesFrame.geometry("300x150")
        QuesFrame.title("Question Manager")
        QuesFrame.configure(background="maroon")
        QuesLabel = Label(QuesFrame, text="Choose your classification", fg="maroon", width=30, height=1).place(x=40, y=20)
        isStudent = Button(QuesFrame, text='Student', bg='green', fg='yellow', command=lambda m='std': Delete(m)).place(x=60, y=60)
        isLecturer = Button(QuesFrame, text='Lecturer', bg='green', fg='yellow', command=lambda m='lec': Delete(m)).place(x=160, y=60)
           
        def Delete(which):
            QuesFrame.destroy()
            IdInputFrame = Toplevel()
            IdInputFrame.geometry("300x150")
            IdInputFrame.title("Id Getter")
            IdInputFrame.configure(background="maroon")
            question = StringVar()
            id = StringVar()
            if which == 'std':
                question.set('Enter Student College id')
            elif which == 'lec':
                question.set('Enter Lecturer College id')
            handler1 = lambda: self.CloseThisFrame(IdInputFrame)
            QuesLabel = Label(IdInputFrame, textvariable=question, fg="maroon", width=30, height=1).place(x=40, y=20)
            id_Entry = Entry(IdInputFrame, textvariable=id,fg="blue", width=25).place(x=70 , y=55)
            InputButton = Button(IdInputFrame, text='Delete', bg='green', fg='yellow', command=lambda : Continue(), width=15).place(x=20, y=90)
            CancelButton = Button(IdInputFrame, text="Cancel", bg='green', fg='yellow', command=handler1, width=15).place(x=160, y=90)
            
            def Continue():
                IdInputFrame.destroy()
                DeleteExcel(which, id.get())
                self.CloseThisFrame()

    def ShowManager(self):
        self.root.withdraw()
        QuesFrame = Toplevel()
        QuesFrame.geometry("300x150")
        QuesFrame.title("Question Manager")
        QuesFrame.configure(background="maroon")
        QuesLabel = Label(QuesFrame, text="Choose your classification", fg="maroon", width=30, height=1).place(x=40, y=20)
        isStudent = Button(QuesFrame, text='Student', bg='green', fg='yellow', command=lambda m='std': Show(m)).place(x=60, y=60)
        isLecturer = Button(QuesFrame, text='Lecturer', bg='green', fg='yellow', command=lambda m='lec': Show(m)).place(x=160, y=60)
        
        def Show(which): 
            QuesFrame.destroy()
            IdInputFrame = Toplevel()
            IdInputFrame.geometry("300x150")
            IdInputFrame.title("Id Getter")
            IdInputFrame.configure(background="maroon")
            question = StringVar()
            id = StringVar()
            if which == 'std':
                question.set('Enter Student College id')
            elif which == 'lec':
                question.set('Enter Lecturer College id')
            handler1 = lambda: self.CloseThisFrame(IdInputFrame)
            QuesLabel = Label(IdInputFrame, textvariable=question, fg="maroon", width=30, height=1).place(x=40, y=20)
            id_Entry = Entry(IdInputFrame, textvariable=id,fg="blue", width=25).place(x=70 , y=55)
            InputButton = Button(IdInputFrame, text='Show', bg='green', fg='yellow', command=lambda : Continue(), width=15).place(x=20, y=90)
            CancelButton = Button(IdInputFrame, text="Cancel", bg='green', fg='yellow', command=handler1, width=15).place(x=160, y=90)

            def Continue():
                IdInputFrame.destroy()
                data = ShowExcel(which, id.get())
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

        lb1 = Label(ExitFrame, text='Team Members',bg='black', fg='gold' , width=40).place(x=70, y=10)
        lb2 = Label(ExitFrame, text='Ammar Mohamed', bg='light blue').place(x=70, y=50)
        lb3 = Label(ExitFrame, text='Michael Metry', bg='light blue').place(x=240, y=50)
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