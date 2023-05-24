
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import SystemSettings as sett

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/divaskararulmozhi/PycharmProjects/CV_Analyser/build/assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.title('CV Analyser')
window.geometry("862x519")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 519,
    width = 862,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    94.0,
    259.0,
    image=image_image_1
)

canvas.create_text(
    335.0,
    36.0,
    anchor="nw",
    text="WELCOME TO CV ANALYSER",
    fill="#000000",
    font=("RobotoRoman Bold", 28 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    524.0,
    161.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#EEEEEE",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=271.0,
    y=134.0+15,
    width=506.0,
    height=35.0
)

canvas.create_text(
    248.0+20,
    134.0,
    anchor="nw",
    text="USERNAME",
    fill="#000000",
    font=("RobotoRoman Bold", 16 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    523.0,
    254.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#EEEEEE",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=270.0,
    y=227.0+15,
    width=506.0,
    height=35.0
)

canvas.create_text(
    247.0+20,
    227.0,
    anchor="nw",
    text="PASSWORD",
    fill="#000000",
    font=("RobotoRoman Bold", 16 * -1)
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    523.0,
    348.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    show="*",
    bg="#CCCCCC",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=270.0,
    y=321.0+15,
    width=506.0,
    height=35.0
)

canvas.create_text(
    265.0+3,
    321.0,
    anchor="nw",
    text="APPLICANT / ADMIN",
    fill="#000000",
    font=("RobotoRoman Bold", 16 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print(sett.loginCheck(entry_1.get(),entry_2.get(),entry_3.get())),
    relief="flat"
)
button_1.place(
    x=429.4512939453125,
    y=425.0,
    width=179.097412109375-10,
    height=37.0
)
window.resizable(False, False)
window.mainloop()