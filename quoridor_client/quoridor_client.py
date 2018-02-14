import tkinter as tk
from tkinter import *
from tkinter import font
from functools import partial
from tkinter.ttk import *
import requests
import web_urls
import json
from pages.StartPage import StartPage
from pages.LogInPage import LogInPage
from pages.RegisterPage import RegisterPage
from pages.MenuPage import MenuPage
from pages.Quoridor2 import Quoridor2
from pages.Quoridor4 import Quoridor4
from pages.RankingPage import RankingPage
from pages.OfflinePage import OfflinePage

# here is the main QuoridorApp

class QuoridorApp(Tk):
    def __init__(self):
        Tk.__init__(self)

        self.title_font = font.Font(size=18, slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in [StartPage, LogInPage, RegisterPage, MenuPage, OfflinePage, Quoridor2, RankingPage, Quoridor4]:
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("StartPage")

    def show_frame(self, page_name): # to get the page to top and show it
        frame = self.frames[page_name]
        frame.tkraise()
