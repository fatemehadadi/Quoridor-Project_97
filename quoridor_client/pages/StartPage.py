# startpage of app
import tkinter as tk
from tkinter import *
from tkinter import font
from functools import partial
from tkinter.ttk import *
import requests
import web_urls
import json
from quoridor_client import *

class StartPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        # build labels and buttons for it
        label = Label(self, text="Welcome To The Quoridor Gameapp",
                      font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        loginbutton = Button(self, text="Log In",
                             command=lambda: controller.show_frame("LogInPage"))
        registerbutton = Button(self, text="Register",
                                command=lambda: controller.show_frame("RegisterPage"))
        quitbutton = tk.Button(self, text="Quit", bg="red",
                            command=self.quit)

        loginbutton.pack()
        registerbutton.pack()
        quitbutton.pack()

    def quit(self):
        self.destroy()
        exit()
