#!/usr/bin/env python3

import tkinter as tk

root = tk.Tk()
root.geometry('800x460')
root.title('image')

root.add

canvas = tk.Canvas(
  root,
  width = 480,
  height = 480,
  relief = tk.RIDGE,
#  bg = 1,
  bd = 2,
)
canvas.place(x = 1, y = 0)

root.mainloop()
