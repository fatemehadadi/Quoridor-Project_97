# pages of App
import tkinter as tk
from tkinter import *
from tkinter import font
from functools import partial
from tkinter.ttk import *
from quoridor_client import *

class OfflinePage(Frame):
    def __init__(self, parent, controller, **kw):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="You Are In Game!",
                      font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        # creating game variables
        self.player2 = [8, 4]
        self.buttons = [[""] * 9] * 9
        self.lines = [[""] * 8] * 9
        self.walls = [[""] * 9] * 8
        self.player1 = [0, 4]

        # build buttons of the boardgame
        for i in range(1, 10):
            for j in range(1, 10):
                self.buttons[i - 1][j - 1] = tk.Button(self, bg="lightblue", state="normal",
                                                       command=partial(self.on_click_place, i-1, j-1))
                self.buttons[i - 1][j - 1].place(relx=i * 0.09, rely=j * 0.09, height=30, width=30)
                self.buttons[i - 1][j - 1].bind("<Button-1>",
                                                lambda e: self.on_click_place(e, i - 1, j - 1))

        for i in range(1, 10):
            for j in range(1, 9):
                self.lines[i - 1][j - 1] = tk.Button(self, state="normal")
                self.lines[i - 1][j - 1].place(relx=i * 0.09, rely=(j + 0.65) * 0.09, height=15, width=30)
                self.lines[i - 1][j - 1].bind("<Button-1>",
                                              lambda e, a=i - 1, b=j - 1: self.on_click_wall(e, i - 1, j - 1))

        for i in range(1, 9):
            for j in range(1, 10):
                self.walls[i - 1][j - 1] = tk.Button(self, state="normal")
                self.walls[i - 1][j - 1].place(relx=(i + 0.65) * 0.09, rely=j * 0.09, height=30, width=15)
                #self.walls[i - 1][j - 1].bind("<Button-1>",pass)


        backbutton = Button(self, text="back",
                            command=lambda: controller.show_frame("MenuPage"))
        backbutton.pack(side="bottom", fill="x", pady=10)
        Button(self, text="start").pack(side="bottom", fill="x", pady=10)

        
        
    def on_click_place(self, i, j):
        pass

    def on_click_wall(self, e, i, j):

        pass
        
