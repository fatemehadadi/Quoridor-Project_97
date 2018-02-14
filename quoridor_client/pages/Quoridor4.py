# pages of App
import tkinter as tk
from tkinter import *
from tkinter import font
from functools import partial
from tkinter.ttk import *
import requests
import web_urls
import json
from quoridor_client import *

class Quoridor4(Frame):
    def __init__(self, parent, controller, **kw):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="You Are In Game!",
                      font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        backbutton = Button(self, text="back",
                            command=lambda: controller.show_frame("MenuPage"))
        backbutton.pack(side="bottom", fill="x", pady=10)
