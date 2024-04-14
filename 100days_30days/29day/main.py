from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox

import pyperclip


def save_password():
    if password_entry.get() != "" and website_entry.get() != "":
        user_answer = messagebox.askokcancel(title=website_entry.get(),
                                             message="Are you sure you want to save this password?")
        if user_answer:
            with open('password.txt', 'a') as f:
                f.write(
                    f"{website_entry.get()} | {emial_entry.get()} | {password_entry.get()}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)

            messagebox.showinfo(title="State",
                                message="Your password has been saved.")
    else:
        messagebox.showerror(title="Error",
                             message="Please enter all data.")


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)  # copying generated pswd to our clipboard


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(window, width=200, height=200)
photo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo_img)
canvas.grid(row=0, column=1)

# labels
website_label = Label(window, text="Website")
website_label.grid(row=1, column=0)
email_label = Label(window, text="Email")
email_label.grid(row=2, column=0)
password_label = Label(window, text="Password ")
password_label.grid(row=3, column=0)

# entries
website_entry = Entry(window, width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
emial_entry = Entry(window, width=35)
emial_entry.insert(END, "moj.mail@gmail.com")
emial_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(window, width=20)
password_entry.grid(row=3, column=1)

# buttons
gen_password = Button(text="Generate Password", width=11,command=generate_password)
gen_password.grid(row=3, column=2)
add_password = Button(text="Add Password", width=33, command=save_password)
add_password.grid(row=4, column=1, columnspan=2)
window.mainloop()
