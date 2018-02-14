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

class Quoridor2(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.connection = False
        self.connection_status = "Wait To Connect!"
        label = Label(self, text=self.connection_status,
                      font=controller.title_font)
        label.pack(side="top", pady=10)

        self.board = [[0 for i in range(9)] for j in range(9)]
        self.player2 = [8, 4]
        self.buttons = [[""] * 9] * 9
        self.lines = [[""] * 8] * 9
        self.walls = [[""] * 9] * 8
        self.player1 = [0, 4]
        # self.user = LogInPage(parent=Frame(), controller=QuoridorApp()).input1.get()

        for i in range(1, 10):
            for j in range(1, 10):
                self.buttons[i - 1][j - 1] = tk.Button(self, bg="lightblue", state="normal")
                self.buttons[i - 1][j - 1].place(relx=i * 0.09, rely=j * 0.09, height=30, width=30)
                self.buttons[i - 1][j - 1].bind("<Button-1>",
                                                lambda e, a=i - 1, b=j - 1: self.on_click_place(e, i - 1, j - 1))

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
                self.walls[i - 1][j - 1].bind("<Button-1>",
                                              lambda e, a=i - 1, b=j - 1: self.on_click_wall(e, i - 1, j - 1))
        offlinebutton = Button(self, text="offline game",
                            command=lambda: controller.show_frame("OfflinePage"))
        offlinebutton.pack(side="bottom", fill="x", pady=10)
        backbutton = Button(self, text="back",
                            command=lambda: controller.show_frame("MenuPage"))
        backbutton.pack(side="bottom", fill="x", pady=10)
        self.player_name = 1

        if not self.connection:
            self.disable_buttons()
            self.data = dict(username="")
            self.data = json.JSONEncoder().encode(self.data)
            payload = dict(action="start_game", data=self.data)
            payload = json.JSONEncoder().encode(payload)
            try:
                requests.post(web_urls.urls['quoridor2'], data=payload)
                # self.connection, self.player_name = self.update()
            except requests.exceptions.ConnectionError:
                self.text = "Connection failed! Try again."

        if self.connection:
            self.enable_buttons()

    def disable_buttons(self):
        for i in range(1, 10):
            for j in range(1, 10):
                self.buttons[i - 1][j - 1].config(state="disabled")
        for i in range(1, 10):
            for j in range(1, 9):
                self.lines[i - 1][j - 1].config(state="disabled")
        for i in range(1, 9):
            for j in range(1, 10):
                self.walls[i - 1][j - 1].config(state="disabled")

    def enable_buttons(self):
        for i in range(1, 10):
            for j in range(1, 10):
                self.buttons[i - 1][j - 1].config(state="normal")
        for i in range(1, 10):
            for j in range(1, 9):
                self.lines[i - 1][j - 1].config(state="normal")
        for i in range(1, 9):
            for j in range(1, 10):
                self.walls[i - 1][j - 1].config(state="normal")

    def update(self):

        # request

        pass

    def on_click_place(self, e, i, j):

        pass

    def on_click_wall(self, e, i, j):

        pass

    def searching(self, player):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == player:
                    return i, j
        return -1, -1


