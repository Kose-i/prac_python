#! /usr/bin/env python3
import tkinter as tk
import tkinter.ttk as ttk

class Window(ttk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        helloLabel = ttk.Label(self, text="Hello World!")
        quitButton = ttk.Button(self, text="Quit", command=self.quit)
        helloLabel.pack()
        quitButton.pack()
        self.pack()

if __name__=='__main__':
    window = Window()
    window.master.title("Hello")
    window.master.mainloop()
