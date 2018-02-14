# menu page
import tkinter as tk
from tkinter import *
from tkinter import font
from functools import partial
from tkinter.ttk import *
import requests
import web_urls
import json
from quoridor_client import *


class MenuPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.controller = controller
        label = Label(self, text="You Are Logged in!",
                      font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        loginbutton = Button(self, text="Log Out",
                             command=lambda: controller.show_frame("StartPage"))
        registerbutton = Button(self, text="Quoridor2",
                                command=lambda: controller.show_frame("Quoridor2"))
        rankingbutton = Button(self, text="Quoridor4",
                               command=lambda: controller.show_frame("Quoridor4"))
        quitbutton = Button(self, text="Quit",
                            command=self.quit)

        loginbutton.pack()
        registerbutton.pack()
        rankingbutton.pack()
        quitbutton.pack()

    def quit(self):
        self.destroy()
        exit()

