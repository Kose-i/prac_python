#!/usr/bin/env python3

import tkinter as tk

root = tk.Tk()
root.geometry('800x460')
root.title('button')

frame = tk.Frame(
    root,
    relief=tk.RIDGE,
    borderwidth=4
)

button_text_variable = tk.StringVar()
def update_button_text():
    button_text_variable.set("b")

button = tk.Button(
    frame,
#    width=15,
    textvariable=button_text_variable,
    command=update_button_text
)

button_text_variable.set("a")

button.pack(side=tk.LEFT)

frame.place(x=10, y=20)
root.mainloop()
