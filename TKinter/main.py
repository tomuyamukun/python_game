from tkinter import *

window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)

# Label


# def label_change(*args):
#     my_label.config(text=args)


mile = Label(text="Miles", font=("Arial", 24, "bold"))
mile.grid(column=2, row=0)

km = Label(text="km", font=("Arial", 24, "bold"))
km.grid(column=2, row=1)


is_equal = Label(text="is equal to", font=("Arial", 24, "bold"))
is_equal.grid(column=0, row=1)

equal = Label(text="0", font=("Arial", 24, "bold"))
equal.grid(column=1, row=1)
# Button


def button_clicked():
    new_text = float(miles_input.get())
    equal.config(text=round(new_text * 1.609))
    # label_change(new_text)


button = Button(text="Caluculate", command=button_clicked)
button.grid(column=1, row=2)

# Entry

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

window.mainloop()
