#!/usr/bin/env python3

import tkinter as tk

def callback():
  print('a')

root = tk.Tk()
root.geometry('800x460')
root.title('menubar')

menubar = tk.Menu(root)
root.config(menu = menubar)

filemenu = tk.Menu(menubar)
menubar.add_cascade(label='ファイル', menu=filemenu)
filemenu.add_command(label='閉じる', command=callback)

root.mainloop()
