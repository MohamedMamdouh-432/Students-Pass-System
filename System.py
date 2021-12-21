from tkinter import *
from tkinter import messagebox as msgx
from ExcelData import *
from classes import Student, Lecturer

class CollegeSystem(object):
    def __init__(self, parent):
        self.students = []
        self.lecturers = []
        self.root = parent
        self.root.title("College Pass System")
        self.root.iconbitmap('p3.ico')
        
        AddButton = Button(self.root, text="Add", padx=15, pady=10, command=self.AddManager).place(x=80, y=200)
        CheckButton = Button(self.root, text="Check", padx=15, pady=10, command=self.CheckManager).place(x=180, y=200)
        DeleteButton = Button(self.root, text="Delete", padx=15, pady=10, command=self.DeleteManager).place(x=280, y=200)
        ShowButton = Button(self.root, text="Show", padx=15, pady=10, command=self.ShowManager).place(x=380, y=200)
        ExitButton = Button(self.root, text="Exit From College Pass System", padx=20, pady=10, command=self.ExitManager).place(x=180, y=300)

    def AddManager(self):
        self.root.withdraw()
        AddFrame = Toplevel()
        AddFrame.geometry("600x400")
        AddFrame.title("Adding Frame Manager")
        AddFrame.configure(background="light green")
        AddFrame.withdraw()

        QuesFrame = Toplevel()
        QuesFrame.geometry("300x150")
        QuesFrame.title("Question Manager")
        QuesFrame.configure(background="light green")
        QuesLabel = Label(QuesFrame, text="Choose your classification", fg="maroon", width=30, height=1).place(x=40, y=20)
        
        isStudent = Button(QuesFrame, text='Student', command=lambda m='std': Add(m)).place(x=60, y=60)
        isLecturer = Button(QuesFrame, text='Lecturer', command=lambda m='lec': Add(m)).place(x=160, y=60)
        
        def Add(which):
            QuesFrame.destroy()
            AddFrame.update()
            AddFrame.deiconify()

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

            IsVacLabel = Label(AddFrame, text="Is Vaccinated", fg="maroon", width=20, height=1).place(x=10, y=170)
            isVac = IntVar()
            TrueVac = Radiobutton(AddFrame, text='True', variable=isVac, value=1).place(x=200, y=170)
            FalseVac = Radiobutton(AddFrame, text='False', variable=isVac, value=2).place(x=300, y=170)

            if which == 'std' :
                GradeLabel = Label(AddFrame, text="Grade : ", fg="maroon", width=20, height=1).place(x=10, y=210)
                GradeInput = StringVar()
                GradeEntry = Entry(AddFrame, textvariable=GradeInput, fg="blue", width=30).place(x= 200, y=210)

                Grade_yearLabel = Label(AddFrame, text="Grade year : ", fg="maroon", width=20, height=1).place(x=10, y=250)
                Grade_yearInput = StringVar()
                Grade_yearEntry = Entry(AddFrame, textvariable=Grade_yearInput, fg="blue", width=30).place(x= 200, y=250)

                KindLabel = Label(AddFrame, text="Kind : ", fg="maroon", width=20, height=1).place(x=10, y=290)
                Kind = IntVar()
                mainStream = Radiobutton(AddFrame, text='Main Stream', variable=Kind, value=1).place(x=200, y=290)
                credit = Radiobutton(AddFrame, text='Credit', variable=Kind, value=2).place(x=300, y=290)
                
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
                    new_std = Student(nameInput.get(), Nat_IdInput.get(), Cge_IdInput.get(), DepInput.get(), isVac.get(), GradeInput.get(), Grade_yearInput.get(), Kind.get())
                    self.students.append(new_std)
                    new_row = list([nameInput.get(), Nat_IdInput.get(), Cge_IdInput.get(), DepInput.get(), isVac.get(), GradeInput.get(), Grade_yearInput.get(), Kind.get()])
                elif which == 'lec' :
                    new_lec = Lecturer(nameInput.get(), Nat_IdInput.get(), Cge_IdInput.get(), DepInput.get(), isVac.get(), SpecInput.get(), Src_UnvInput.get())
                    self.lecturers.append(new_lec)
                    new_row = list([nameInput.get(), Nat_IdInput.get(), Cge_IdInput.get(), DepInput.get(), isVac.get(), SpecInput.get(), Src_UnvInput.get()])
                AddExcel(which, new_row)
                msgx.showinfo('Saving Message', 'Your Data have successfully been recorded')
                handler()
            SaveButton = Button(AddFrame, text="Save", bg='light blue', command=saveData).place(x=100, y=330)
            CancelButton = Button(AddFrame, text="Cancel", bg='light blue', command=handler).place(x=300, y=330)
        
    def CheckManager(self):
        self.root.withdraw()
        CheckFrame = Toplevel()
        CheckFrame.geometry("600x400")
        CheckFrame.title("Check Frame Manager")
        CheckFrame.configure(background="light green")
        CheckFrame.withdraw()

        QuesFrame = Toplevel()
        QuesFrame.geometry("300x150")
        QuesFrame.title("Question Manager")
        QuesFrame.configure(background="light green")
        QuesLabel = Label(QuesFrame, text="Choose your classification", fg="maroon", width=30, height=1).place(x=40, y=20)
        
        isStudent = Button(QuesFrame, text='Student', command=lambda m='std': Check(m)).place(x=60, y=60)
        isLecturer = Button(QuesFrame, text='Lecturer', command=lambda m='lec': Check(m)).place(x=160, y=60)
        
        def Check(which):
            if which == 'std' :
                pass
            elif which == 'lec' :
                pass

        handler = lambda: self.CloseThisFrame(CheckFrame)
        SaveButton = Button(CheckFrame, text="Close", command=handler).place(x=200, y=330)

    def DeleteManager(self):
        self.root.withdraw()
        DeleteFrame = Toplevel()
        DeleteFrame.geometry("600x400")
        DeleteFrame.title("Delete Frame Manager")
        DeleteFrame.configure(background="light green")
        DeleteFrame.withdraw()

        QuesFrame = Toplevel()
        QuesFrame.geometry("300x150")
        QuesFrame.title("Question Manager")
        QuesFrame.configure(background="light green")
        QuesLabel = Label(QuesFrame, text="Choose your classification", fg="maroon", width=30, height=1).place(x=40, y=20)
        
        isStudent = Button(QuesFrame, text='Student', command=lambda m='std': Delete(m)).place(x=60, y=60)
        isLecturer = Button(QuesFrame, text='Lecturer', command=lambda m='lec': Delete(m)).place(x=160, y=60)
           
        def Delete(which):
            if which == 'std' :
                pass
            elif which == 'lec' :
                pass

        handler = lambda: self.CloseThisFrame(DeleteFrame)
        SaveButton = Button(DeleteFrame, text="Close", command=handler).place(x=200, y=330)

    def ShowManager(self):
        self.root.withdraw()
        ShowFrame = Toplevel()
        ShowFrame.geometry("600x400")
        ShowFrame.title("Show Frame Manager")
        ShowFrame.configure(background="light green")
        ShowFrame.withdraw()

        QuesFrame = Toplevel()
        QuesFrame.geometry("300x150")
        QuesFrame.title("Question Manager")
        QuesFrame.configure(background="light green")
        QuesLabel = Label(QuesFrame, text="Choose your classification", fg="maroon", width=30, height=1).place(x=40, y=20)

        isStudent = Button(QuesFrame, text='Student', command=lambda m='std': Show(m)).place(x=60, y=60)
        isLecturer = Button(QuesFrame, text='Lecturer', command=lambda m='lec': Show(m)).place(x=160, y=60)
           
        def Show(which):
            if which == 'std' :
                pass
            elif which == 'lec' :
                pass

        handler = lambda: self.CloseThisFrame(ShowFrame)
        SaveButton = Button(ShowFrame, text="Close", command=handler).place(x=200, y=330)

    def ExitManager(self):
        self.root.withdraw()
        ExitFrame = Toplevel()
        ExitFrame.geometry("600x400")
        ExitFrame.title("Exit Frame Manager")
        ExitFrame.configure(background="light green")


        handler = lambda: self.CloseThisFrame(ExitFrame)
        SaveButton = Button(ExitFrame, text="Close", command=handler).place(x=200, y=330)

    def CloseThisFrame(self, ThisFrame):
        ThisFrame.destroy()
        self.root.update()
        self.root.deiconify()