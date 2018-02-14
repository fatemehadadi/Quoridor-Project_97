# register page
import tkinter as tk
from tkinter import *
from tkinter import font
from functools import partial
from tkinter.ttk import *
import requests
import web_urls
import json
from quoridor_client import *

class RegisterPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        # build the page buttons and labels and entrys
        self.text_font = font.Font(size=12, slant="italic")
        label = Label(self, text="Fill In The Data", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        Label(self, text="Name", font=self.text_font).pack()
        self.input1 = StringVar()
        Entry(self, textvariable=self.input1).pack()
        Label(self, text="Username", font=self.text_font).pack()
        self.input2 = StringVar()
        Entry(self, textvariable=self.input2).pack()
        Label(self, text="password", font=self.text_font).pack()
        self.input3 = StringVar()
        Entry(self, textvariable=self.input3).pack()
        Label(self, text="confirme password", font=self.text_font).pack()
        self.input4 = StringVar()
        Entry(self, textvariable=self.input4).pack()
        self.text = ""
        self.status = tk.Label(self, text=self.text, font=self.text_font).pack()
        Label(self, font=self.text_font).pack()

        button1 = tk.Button(self, text="Back",
                            command=lambda: self.controller.show_frame("StartPage"), bg="red")
        button1.pack()
        button = Button(self, text="Register", command=lambda: self.is_ok())
        button.pack()

    def is_valid_name(self, name): #to see if entried name is valid
        if 0 <= len(name) <= 100:
            return True
        return False

    def is_valid_username(self, username): # to see if entried username is valid
        if (3 <= len(username) <= 100
            and username.replace('_', '').isalnum()
            and (username[0].isalpha() or username[0] == '_')
            ):
            return True
        return False

    def is_valid_password(self, password): # to see if entried password is valid
        if len(password) >= 8:
            return True
        return False

    def is_ok(self): #sending datas to webserver
        name = self.input1.get()
        username = self.input2.get()
        password = self.input3.get()
        cpassword = self.input4.get()
        if (not (self.is_valid_name(name) or self.is_valid_username(username) or self.is_valid_password(
                password) or password == cpassword)):
            self.text = "Wrong input."
        else:
            payload = dict(action="signup", name=name, username=username, password=password)
            try:
                requests.post(web_urls.urls['signup'], data=payload)
                self.controller.show_frame("StartPage")
            except requests.exceptions.ConnectionError:
                self.text = "Connection failed! Try again."


