# log in page
import tkinter as tk
from tkinter import *
from tkinter import font
from functools import partial
from tkinter.ttk import *
import requests
import web_urls
import json
from quoridor_client import *


class LogInPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="Fill In The Data", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        self.text_font = font.Font(size=12, slant="italic")
        Label(self, text="Username", font=self.text_font).pack()
        self.input1 = StringVar()
        Entry(self, textvariable=self.input1).pack()
        Label(self, text="password", font=self.text_font).pack()
        self.input2 = StringVar()
        Entry(self, textvariable=self.input2).pack()
        self.text = ""
        self.status = tk.Label(self, text=self.text, font=self.text_font).pack()
        button1 = Button(self, text="Back", command=lambda: self.controller.show_frame("StartPage"))
        button1.pack()
        button = Button(self, text="Log In",
                        command=lambda: self.checking())
        button.pack()

    def is_username_valid(self, username): # to see if username is valid
        if username:
            return True
        return False

    def is_password_valid(self, password):  # to see if password is valid
        if password:
            return True
        return False

    def checking(self):  # to check the whole data and send it to webserver
        username = self.input1.get()
        password = self.input2.get()
        if not (self.is_username_valid(username) and self.is_password_valid(password)):
            self.text = "Wrong input."
        else:
            payload = dict(action="signin", username=username, password=password)
            try:
                requests.post(web_urls.urls['signin'], data=payload)
                self.controller.show_frame("MenuPage")
            except requests.exceptions.ConnectionError:
                self.text = "Connection failed! Try again."

