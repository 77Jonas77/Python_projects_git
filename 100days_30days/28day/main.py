import math
from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_EMOJI = '✅'
reps = 0
count_timer = 0
timer = None


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_label, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_label, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)


if __name__ == '__main__':
    window = Tk()
    window.title("Pomodoro")
    window.config(padx=150, pady=100, bg=YELLOW)

    # tomato with timer
    canvas = Canvas(width=300, height=300, bg=YELLOW, highlightthickness=0)
    img = PhotoImage(file="tomato.png")
    canvas.create_image(150, 150, image=img)
    timer_label = canvas.create_text(150, 165, text="00:00", fill="white",
                                     font=(FONT_NAME, 35, "bold"))
    canvas.grid(column=1, row=1)

    # Button start and reset
    start_button = Button(window, text="Start", command=start_timer,
                          highlightthickness=0)
    reset_button = Button(window, text="Reset", command=reset_timer,
                          highlightthickness=0)
    start_button.grid(column=0, row=2)
    reset_button.grid(column=3, row=2)

    # Label marks + title
    title_label = Label(window, text="Pomodoro Timer", fg=GREEN, bg=YELLOW,
                        font=(FONT_NAME, 50, "bold"))
    title_label.grid(column=1, row=0)

    check_marks = Label(window, text="✅", fg=GREEN, bg=YELLOW)
    check_marks.grid(column=1, row=2)
    window.mainloop()
