import tkinter as tk

class Frame(tk.Frame):
    def __init__(self,root = None):
        super().__init__(root, width=480,  height=320)
        self.root = root
        self.pack()
        self.config(bg='green')