import os
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
from PIL import ImageTk, Image
import psutil
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Label, Entry, Text, Button, PhotoImage, END, messagebox
import tkinter.filedialog as filedialog
import pyresparser as p
import csv
import pandas as pd
import warnings
warnings.filterwarnings(action='ignore',category=UserWarning)
from subprocess import Popen,PIPE
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/divaskararulmozhi/PycharmProjects/CV_Analyser/build/assets/frame1")
output_path=""
resS=0
def rel_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)



def uploadFile():
    global output_path
    output_path = filedialog.askopenfilename()
    cv_entry.delete(0, END)
    cv_entry.insert(0, output_path)

def writeJobDetails(skillset):
    global resS
    wrongcount=0
    totskills=len(skillset)
    namefile = open('name.txt', 'r')
    keywordfile=open('Keywords.txt','r')
    # df = pd.read_csv('ApplicantRecord.csv',index_col='Username')
    with open('Keywords.txt') as keywordfile:
        words=keywordfile.read().split('\n')
        words=[w.lower() for w in words]
        skillset=[s.lower() for s in skillset]
        for skill in skillset:
            if skill not in words:
                wrongcount += 1
                skillset.remove(skill)
    resScore = (totskills - wrongcount)
    resScore=resScore*7.5
    if resScore>100:
        while(resScore>100):
            resScore=resScore-1.5*sum([totskills,wrongcount])
    resS=resScore
    #thahir said dont do this :: df.to_csv('ApplicantRecord.csv', mode='a', index=False, header=False)
    cvs_entry.delete(0, END)
    cvs_entry.insert(0, resScore)
    print('Paste the below list in colab, after job prediction, paste job post in gui.')
    print(skillset)
    print('\n')
    print('Applicant Skills :\n')
    for skill in skillset:
        print(skill)


def predictPost():
    global output_path
    if len(output_path)==0:
        messagebox.showinfo('Error','Upload your CV')
    else:
        data=p.ResumeParser(output_path).get_extracted_data()
        writeJobDetails(data['skills'])

def writeandexit():
    global resS
    file = open('name.txt', 'r')
    username = file.read().strip()  # Remove leading/trailing whitespaces
    file.close()

    df = pd.read_csv('ApplicantRecord.csv')

    new_row_data = pd.DataFrame([
        {'Username': username,
         'Expected Job Post': exj_entry.get(),
         'Resume Score': resS
         }
    ])
    new_row = pd.DataFrame(new_row_data)
    new_row.to_csv('ApplicantRecord.csv', mode='a', index=False, header=False)
    exit()

# Create the main window
window = Tk()
window.title("Applicant Window")

# Set window size and disable window resizing
window.geometry("899x529")
window.resizable(False, False)

# Set window background image
bg_image = ImageTk.PhotoImage(Image.open("bg9.png"))
bg_image1 = ImageTk.PhotoImage(Image.open("pbg.png"))
bg_label = Label(window, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create login panel
panel_frame = Label(window, bd=5, relief="groove", image=bg_image1)
panel_frame.place(relx=0.5, rely=0.5, anchor="center")


# Create username label and entry
cv_label = Label(panel_frame, text="Uplaod CV :", font=("GothamBold.ttf", 12))
cv_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
cv_entry = Entry(panel_frame, font=("GothamBold.ttf", 12))
cv_entry.grid(row=1, column=1, padx=10, pady=10)

# Create login button
sb_button = Button(panel_frame, text="Submit", command=lambda: predictPost(), font=("GothamBold.ttf", 12))
sb_button.grid(row=2, columnspan=1, padx=10, pady=10)

sb_button = Button(panel_frame, text="Upload", command=lambda: uploadFile(), font=("GothamBold.ttf", 12))
sb_button.grid(row=2, columnspan=3, padx=10, pady=10)

exj_label = Label(panel_frame, text="Expected Job:", font=("GothamBold.ttf", 12))
exj_label.grid(row=3, column=0, padx=10, pady=10, sticky="e")
exj_entry = Entry(panel_frame, font=("GothamBold.ttf", 12))
exj_entry.grid(row=3, column=1, padx=10, pady=10)

# Create password label and entry
cvs_label = Label(panel_frame, text="Your CV Score:", font=("GothamBold.ttf", 12))
cvs_label.grid(row=4, column=0, padx=10, pady=10, sticky="e")
cvs_entry = Entry(panel_frame, font=("GothamBold.ttf", 12))
cvs_entry.grid(row=4, column=1, padx=10, pady=10)

# Create login button
close_button = Button(panel_frame, text="Save & Exit", command=lambda: writeandexit(), font=("GothamBold.ttf", 12))
close_button.grid(row=5, columnspan=2, padx=10, pady=10)

# Start the GUI main loop
window.mainloop()