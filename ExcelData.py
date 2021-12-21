from openpyxl import workbook, load_workbook
from tkinter import messagebox as msgx

wb = load_workbook('CollegeData.xlsx')
ws = wb.active

def AddExcel(which, data):
    if which == 'std' :
        ws = wb["Students"]
    elif which == 'lec' :
        ws = wb["Lecturers"]
    ws.append(data)
    wb.save('CollegeData.xlsx')

def searchExcel(which, id):
    if which == 'std' :
        ws = wb['Students']
    elif which == 'lec' :
        ws = wb['Lecturers']

    for r in range(1,ws.max_row):
        com_id = ws.cell(row=r, column=3).value
        if com_id == id :
            return r

def checkExcel(which, id):
    r = search(which, id)
    #msgx.showinfo('Check Manager', f'Person is already Existed')
    c=1
    print(f'Name : {ws.cell(row=r, column=c).value}')
    c+=1
    print(f'National Id : {ws.cell(row=r, column=c).value}')
    c+=1
    print(f'College Id : {ws.cell(row=r, column=c).value}')
    c+=1
    print(f'Departement : {ws.cell(row=r, column=c).value}')
    c+=1
    print(f'Vaccination State : {ws.cell(row=r, column=c).value}')
    if which == 'std' :
        c+=1
        print(f'Grade : {ws.cell(row=r, column=c).value}')
        c+=1
        print(f'Graduation Year : {ws.cell(row=r, column=c).value}')
        c+=1
        print(f'Category : {ws.cell(row=r, column=c).value}')

    elif which == 'lec' :
        c+=1
        print(f'Speciality : {ws.cell(row=r, column=c).value}')
        c+=1
        print(f'Source University : {ws.cell(row=r, column=c).value}')
    wb.save('CollegeData.xlsx')

def DeleteExcel(which, id):
    r = search(which, id)
    ws.delete_rows(r)
    wb.save('CollegeData.xlsx')

def ShowExcel(which, id):
    r = search(which, id)
    c=1
    print(f'Name : {ws.cell(row=r, column=c).value}')
    c+=1
    print(f'National Id : {ws.cell(row=r, column=c).value}')
    c+=1
    print(f'College Id : {ws.cell(row=r, column=c).value}')
    c+=1
    print(f'Departement : {ws.cell(row=r, column=c).value}')
    c+=1
    print(f'Vaccination State : {ws.cell(row=r, column=c).value}')
    if which == 'std' :
        c+=1
        print(f'Grade : {ws.cell(row=r, column=c).value}')
        c+=1
        print(f'Graduation Year : {ws.cell(row=r, column=c).value}')
        c+=1
        print(f'Category : {ws.cell(row=r, column=c).value}')

    elif which == 'lec' :
        c+=1
        print(f'Speciality : {ws.cell(row=r, column=c).value}')
        c+=1
        print(f'Source University : {ws.cell(row=r, column=c).value}')
    wb.save('CollegeData.xlsx')