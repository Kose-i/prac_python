#!/usr/bin/env python3

import tkinter as tk

root = tk.Tk()
root.geometry('800x460')
root.title('image')


canvas = tk.Canvas(
  root,
  width = 480,
  height = 480,
  relief = tk.RIDGE,
#  bg = 1,
  bd = 2,
)
image_path = tk.PhotoImage(file="img/senryuGirl.png")
canvas.create_image(
    0,
    0,
    image = image_path,
    anchor = tk.NW
)

#root.add
canvas.place(x = 1, y = 0)

root.mainloop()
