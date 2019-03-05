#!/usr/bin/env python3

import tkinter as tk

root = tk.Tk()
root.geometry('800x460')
root.title('test')

frame = tk.Frame(
    root,
    relief=tk.RIDGE,
    borderwidth = 4
)

font = ('Helvetica, 14')

root.mainloop()
