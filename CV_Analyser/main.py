# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from tkinter import *
from functools import partial

window = Tk()



def print_text():
    name=(n.get())
    p=(pwd.get())
    option=(str.get())
    print(name,p,option)
window.title("CV Analyser")
window.geometry('1920x1080')
window.resizable(height=None,width=None)
hello = Label(text="Login").place(x=700,y=5)
name = Label(window, text = "Username").place(x=550,y=30)
n = Entry(window)
n.place(x=800,y=30)
Pass=Label(window,text='Password').place(x=550,y=55)
pwd=Entry(window)
pwd.place(x=800,y=55)
str=StringVar()
str.set('Your choice')
opt=Label(window,text='Are you an applicant or an admin ?').place(x=550,y=85)
drop=OptionMenu(window,str,'Applicant','Admin')
drop.place(x=800,y=85)
button = Button(text="CONTINUE",command=print_text).place(x=670,y=115)
window.mainloop()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
