from tkinter import Tk, ttk
from PIL import ImageTk, Image
from pathlib import Path
import csv
from PIL import ImageTk, Image
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import *
from tkinter import Tk, ttk
import tkinter.ttk as ttk
import pandas as pd

window = Tk()
window.title('Applicant List')
window.geometry("579x529")

# Load the background image

background_image = PhotoImage(file="bgcv.png")

# Create a label widget with the background image
background_label = ttk.Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create the Treeview widget
tree_frame = ttk.Frame(background_label)
tree_frame.place(x=50, y=50, width=500, height=300)

tree = ttk.Treeview(columns=("Username", "Expected Job Post", "Resume Score"), height=400, selectmode="extended")
tree.heading('Username', text="Username", anchor=W)
tree.heading('Expected Job Post', text="Expected Job Post", anchor=W)
tree.heading('Resume Score', text="Resume Score", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=120)
tree.column('#2', stretch=NO, minwidth=0, width=350)
tree.column('#3',stretch=NO,minwidth=0,width=90)
tree.pack()
with open('ApplicantRecord.csv') as f:
  reader = csv.DictReader(f)
  for row in reader:
    name = row['Username']
    job = row['Expected Job Post']
    score = row['Resume Score']
    tree.insert("", 0, values=(name,job,score))
# Create a button to close the window
close_button = ttk.Button(window, text="Close", command=lambda: exit())
close_button.place(x=275, y=400)

window.mainloop()
