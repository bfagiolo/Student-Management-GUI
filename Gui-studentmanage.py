from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import student

student_list = []
id = 1001
window = Tk()
window.geometry("900x700")
window.title("Simple Student Management System")

Label(text = "First Name", font = ("Arial", 16)).grid(row = 1, column = 1, padx= 150, pady = 8)
Label(text = "Last Name", font = ("Arial", 16)).grid(row = 2, column = 1, pady = 8)
Label(text = "Date of birth", font = ("Arial", 16)).grid(row = 3, column = 1, pady = 8)
Label(text = "Major", font = ("Arial", 16)).grid(row = 4, column = 1, pady = 8)

firstnameValue = StringVar()
lastnameValue = StringVar()
birthdateValue = StringVar()
majorValue = StringVar()

firstnameEntry = Entry(window, textvariable = firstnameValue)
lastnameEntry = Entry(window, textvariable = lastnameValue)
birthdateEntry = Entry(window, textvariable = birthdateValue)
majorEntry = Entry(window, textvariable = majorValue)

firstnameEntry.grid(row = 1, column = 2, pady = 8)
lastnameEntry.grid(row = 2, column = 2, pady = 8)
birthdateEntry.grid(row = 3, column = 2, pady = 8)
majorEntry.grid(row = 4, column = 2, pady = 8)
count=0
def add_student_button():
    global count
    if firstnameEntry.get()=='':
        messagebox.showerror('error', 'First Name is required')
        return
    if lastnameEntry.get()=='':
        messagebox.showerror('error', 'Last Name is required')
        return
    if birthdateEntry.get()=='':
        messagebox.showerror('error', 'Date of birth is required')
        return

    global id
    if len(majorEntry.get()) == 0:
        major = "Undefined"
    else:
        major = majorEntry.get()
    instance = student.Student(id, firstnameEntry.get(), lastnameEntry.get(), birthdateEntry.get(), major)
    student_list.append(instance)
    count+=1
    id+=1
    messagebox.showinfo('Information', 'Student added')
    firstnameEntry.delete(0, END)
    lastnameEntry.delete(0, END)
    birthdateEntry.delete(0,END)
    majorEntry.delete(0, END)

def search_name_button():
    frame.delete('1.0', 'end')
    results = 0
    for instance in student_list:
        if SearchNameEntry.get() == instance.first_name or SearchNameEntry.get() == instance.last_name:
            if results == 0:
                frame.insert(END, f'{"ID":<10s}{"First Name":<20s}{"Last Name":<20s}{"Date of birth":<20s}{"Major":<20s}\n')
                frame.insert(END, f'{"-"*107}\n')
            frame.insert(END, instance.get_info())
            results += 1
    if results == 0:
        messagebox.showerror('error', f"No student found in the name of '{SearchNameEntry.get()}' ")
    SearchNameEntry.delete(0, END)

def remove_button():
    matches = 0
    for instance in student_list:
        if RemoveEntry.get() == str(instance.id):
            student_list.remove(instance)
            messagebox.showinfo('Information', f'Student id {instance.id} is removed')
            matches += 1
    if matches == 0:
        messagebox.showerror('error', 'No matching id found')
    RemoveEntry.delete(0, END)

AddStudentButton = Button(text = "Add Student", command = add_student_button)
AddStudentButton.grid(row = 5, column = 2, pady = 6)
separator = ttk.Separator(window, orient='horizontal')
separator.place(relx =0, rely = .33, relwidth = 1.8, relheight = .005)

SearchButton = Button(text = "Search by name", command = search_name_button)
SearchButton.grid(row = 6, column = 1, pady = 28)

SearchNameValue = StringVar()
SearchNameEntry = Entry(window, textvariable = SearchNameValue, width = 16)
SearchNameEntry.place(relx = .29, rely = .353)


def view_all_button():
    frame.delete('1.0', 'end')
    global student_list
    if len(student_list) == 0:
        messagebox.showerror('error', 'No student found')
        return
    frame.insert(END, f'{"ID":<10s}{"First Name":<20s}{"Last Name":<20s}{"Date of birth":<20s}{"Major":<20s}\n')
    frame.insert(END, f'{"-"*107}\n')
    for student in student_list:
        frame.insert(END, student.get_info())


ViewButton = Button(text = "View All", command = view_all_button)
ViewButton.place(relx = .60, rely = .347)

frame = tk.Text(window, width = 107, height = 23, highlightbackground ="white", highlightthickness = 3)
frame.place(relx = .11, rely = .415)

separator = ttk.Separator(window, orient='horizontal')
separator.place(relx = 0, rely = .88, relwidth = 1.8, relheight = .005)

RemoveButton = Button(window, text = "Remove by id", command = remove_button)
RemoveButton.grid(column = 1, pady = 330)

RemoveValue= StringVar()
RemoveEntry = Entry(window, textvariable = RemoveValue, width = 15)
RemoveEntry.place(relx = .282, rely = .905)


window.mainloop()
