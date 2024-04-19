import time
from tkinter import *
from tkinter import messagebox
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"


def x_clicked():
    next_card()


def check_clicked():
    loaded_dict.remove(curr)
    next_card()


def save_progress():
        df = pd.DataFrame(loaded_dict)
        df.to_csv("progress.csv", index=False)


def next_card():
    global timex
    curr = random.choice(loaded_dict)
    window.after_cancel(timex)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=curr["French"])
    canvas.itemconfig(main_card, image=photo_img)
    canvas.itemconfig(card_title, text="French")
    timex = window.after(3000, func=flip_card)


def flip_card():
    photo_back = PhotoImage(file="card_back.png")
    canvas.itemconfig(main_card, image=photo_back)
    canvas.itemconfig(card_title, text="English")
    canvas.itemconfig(card_word, text=curr["English"])
    window.config(padx=50, pady=50, bg='white')


window = Tk()
window.title("Flash Card Project")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
timex = window.after(3000, func=flip_card)
loaded_dict = pd.read_csv(
    "/Users/jonaszsojka/PycharmProjects/100days_40days/31day/flash-card-project-start/data/french_words.csv").to_dict(
    orient="records")

curr = random.choice(loaded_dict)

canvas = Canvas(window, width=800, height=526)
photo_img = PhotoImage(file="card_front.png")
main_card = canvas.create_image(400, 263, image=photo_img)
canvas.grid(row=0, column=0, columnspan=2)
card_title = canvas.create_text(400, 150, text="French",
                                font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text=f"{curr["French"]}",
                               font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

photo_img2 = PhotoImage(file="wrong.png")
button_x = Button(image=photo_img2, command=next_card)
button_x.grid(row=1, column=0)

photo_img3 = PhotoImage(file="right.png")
button_check = Button(image=photo_img3, command=next_card)
button_check.grid(row=1, column=1)

save_progress()
window.mainloop()
