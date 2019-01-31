#!/usr/bin/env python3

import tkinter as tk


root = tk.Tk()
root.geometry('800x460')
root.title('menubar')

def finish_callback():
  root.destroy()

menubar = tk.Menu(root)
root.config(menu = menubar)

cmdmenu = tk.Menu(menubar)
menubar.add_cascade(label='コマンドメニュー', menu=cmdmenu)
cmdmenu.add_command(label='閉じる', command=finish_callback)

checkmenu = tk.Menu(menubar)
menubar.add_cascade(label='チェックメニュー', menu=checkmenu)
checkmenu.add_checkbutton(label='test1')

radiomenu = tk.Menu(menubar)
menubar.add_cascade(label='ラジオメニュー', menu=radiomenu)
radiomenu.add_radiobutton(
  label='test1',
  variable = tk.IntVar(),
  value = 0
)

separatormenu = tk.Menu(menubar)
menubar.add_cascade(label='区切り線', menu=separatormenu)
separatormenu.add_separator()

root.mainloop()
