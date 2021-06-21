from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = [
        'a',
        'b',
        'c',
        'd',
        'e',
        'f',
        'g',
        'h',
        'i',
        'j',
        'k',
        'l',
        'm',
        'n',
        'o',
        'p',
        'q',
        'r',
        's',
        't',
        'u',
        'v',
        'w',
        'x',
        'y',
        'z',
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letters = [choice(letters) for _ in range(nr_letters)]
    password_symbols = [choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    entry_pass.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_info():
    web_info = entry_web.get()
    user_info = entry_user.get()
    pass_info = entry_pass.get()
    all_info = f"{web_info} | {user_info} | {pass_info}\n"

    if not web_info or not user_info or not pass_info:
        messagebox.showinfo(
            title="Oops",
            message="Please make sure you haven;t left any fields empty")
    else:
        is_ok = messagebox.askokcancel(
            title=web_info,
            message=f"These are details entered : {all_info}")

        if is_ok:
            with open("password_data.txt", mode="a") as data:
                data.write(all_info)
                pyperclip.copy(pass_info)
                entry_web.delete(0, END)
                entry_pass.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

label_website = Label(text="Website:")
label_website.grid(column=0, row=1)

label_user = Label(text="Email/Username:")
label_user.grid(column=0, row=2)

label_password = Label(text="Password:")
label_password.grid(column=0, row=3)

entry_web = Entry(width=35)
entry_web.grid(column=1, row=1, columnspan=2)
entry_web.focus()

entry_user = Entry(width=35)
entry_user.grid(column=1, row=2, columnspan=2)
entry_user.insert(0, "fakepractice@gmail.com")

entry_pass = Entry(width=21)
entry_pass.grid(column=1, row=3, sticky=W)

pass_button = Button(text="Generate Password", command=generate_password)
pass_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save_info)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
