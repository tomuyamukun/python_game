from tkinter import *
import pandas as pd
from random import choice, randint, shuffle
from time import sleep

BACKGROUND_COLOR = "#B1DDC6"

word_list = {}
current_card = {}

# pandasでデータ抽出

try:
    data = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    origin_data = pd.read_csv("./data/french_words.csv")
    word_list = origin_data.to_dict(orient="records")
else:
    word_list = data.to_dict(orient="records")


# French -- English

def change_english():

    canvas.itemconfig(card_title, text="English", fill="white")

    canvas.itemconfig(card_list, text=current_card["English"], fill="white")

    canvas.itemconfig(canvas_image, image=card_back)


def is_known():
    word_list.remove(current_card)
    data = pd.DataFrame(word_list)
    data.to_csv("data/words_to_learn.csv", index=False)

    next_card()


# CreateCard

def next_card():
    global current_card, flip_timer

    window.after_cancel(flip_timer)

    current_card = choice(word_list)

    canvas.itemconfig(canvas_image, image=card_front)

    canvas.itemconfig(card_title, text="French", fill="black")

    canvas.itemconfig(card_list, text=current_card["French"], fill="black")

    flip_timer = window.after(3000, change_english)

    # new_list = pd.io.json.json_normalize(current_card)

    # new_list.to_csv("filename.csv", mode="a", index=False, header=False)


#   UI
window = Tk()
window.title("Flash_Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=change_english)


canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(
    400, 150, text="", font=(
        "Arial", 40, "italic"))

card_list = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)


bad_image = PhotoImage(file="./images/wrong.png")
bad_button = Button(
    image=bad_image,
    highlightthickness=0,
    command=next_card)
bad_button.grid(row=1, column=0)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(
    image=right_image,
    highlightthickness=0,
    command=is_known)
right_button.grid(row=1, column=1)


next_card()


window.mainloop()
