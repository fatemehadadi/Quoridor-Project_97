import tkinter as tk
from tkinter import *
from tkinter import font
from functools import partial
from tkinter.ttk import *


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
        for F in [StartPage, LogInPage, RegisterPage, MenuPage, Quoridor2, Quoridor4]:
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.controller = controller
        label = Label(self, text="Welcome To The Quoridor Gameapp",
                      font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        LogInButton = Button(self, text="Log In",
                             command=lambda: controller.show_frame("LogInPage"))
        RegisterButton = Button(self, text="Register",
                                command=lambda: controller.show_frame("RegisterPage"))
        RankingButton = Button(self, text="Rankings",
                               command=lambda: controller.show_frame("RankingPage"))
        QuitButton = Button(self, text="Quit",
                            command=self.quit)

        LogInButton.pack()
        RegisterButton.pack()
        RankingButton.pack()
        QuitButton.pack()

    def quit(self):
        self.destroy()
        exit()


class LogInPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="Fill In The Data", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button1 = Button(self, text="Back", command=lambda: self.controller.show_frame("StartPage"))
        button1.pack()
        button = Button(self, text="Log In",
                        command=lambda: self.checking())
        button.pack()

    def is_valid(self):
        return True

    def checking(self):
        if self.is_valid():
            self.controller.show_frame("MenuPage")
        else:
            label.config(text="Incorrect Data! Try Again:")


class RegisterPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.text_font = font.Font(size=12, slant="italic")
        label = Label(self, text="Fill In The Data", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label = Label(self, text="Name", font=self.text_font).pack()
        entry1 = Entry(self).pack()
        label = Label(self, text="Username", font=self.text_font).pack()
        entry2 = Entry(self).pack()
        label = Label(self, text="password", font=self.text_font).pack()
        entry3 = Entry(self).pack()
        label = Label(self, text="confirme password", font=self.text_font).pack()
        entry4 = Entry(self).pack()

        button1 = tk.Button(self, text="Back",
                            command=lambda: self.controller.show_frame("StartPage"), bg="red")
        button1.pack()
        button = Button(self, text="Register",
                        command=lambda: is_ok())
        button.pack()

    def is_ok(self,e):
        self.name=entry1.get()
        self.username=entry2.get()
        self.password=entry3.get()
        self.cpassword=entry4.get()
        if not is_valid_person()
        

    def is_valid_person(self):
        if is_valid():
            controller.show_frame("StartPage")
        else:
            label.config(text="Wrong Input! Try Again:")

    def is_valid(self):
        return True


class RankingPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="Here Is The Rankings:", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        self.list = import_rankings()
        for i in range(len(self.list)):
            Label(self, text=str(i)).pack()
        button = Button(self, text="OK", command=lambda: controller.show_frame("MenuPage"))
        button.pack()

    def import_rankings(self):
        a = ""
        return a


class MenuPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.controller = controller
        label = Label(self, text="You Are Logged in!",
                      font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        LogInButton = Button(self, text="Log Out",
                             command=lambda: controller.show_frame("StartPage"))
        RegisterButton = Button(self, text="Quoridor2",
                                command=lambda: controller.show_frame("Quoridor2"))
        RankingButton = Button(self, text="Quoridor4",
                               command=lambda: controller.show_frame("Quoridor4"))
        QuitButton = Button(self, text="Quit",
                            command=self.quit)

        LogInButton.pack()
        RegisterButton.pack()
        RankingButton.pack()
        QuitButton.pack()

    def quit(self):
        self.destroy()
        exit()


class FButton(tk.Button):
    def __init__(self, parent, x, y, bg=None):
        FButton.__init__(self, parent, bg=bg)
        self.x = x
        self.y = y


class Quoridor2(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.controller = controller
        label = Label(self, text="You Are In Game!",
                      font=controller.title_font)
        label.pack(side="top", pady=10)

        self.player2 = [8, 4]
        self.x = 0
        self.buttons = [[""] * 9] * 9
        self.lines = [[""] * 8] * 9
        self.walls = [[""] * 9] * 8
        self.player1 = [0, 4]

        def xy(i, j, buttons):
            print(self.player1)
            buttons[self.player1[0]][self.player1[1]].config(bg="lightblue")
            self.player1 = [i, j]
            print(self.player1)


        def coloring(event):
            event.widget.config(bg='red')

        for i in range(1, 10):
            for j in range(1, 10):
                self.buttons[i - 1][j - 1] = tk.Button(self, command=partial(xy, j - 1, i - 1, self.buttons),
                                                       bg="lightblue")
                self.buttons[i - 1][j - 1].place(relx=i * 0.09, rely=j * 0.09, height=30, width=30)
                self.buttons[i - 1][j - 1].bind("<Button-1>", partial(xy, j - 1, i - 1, self.buttons))

        for i in range(1, 10):
            for j in range(1, 9):
                self.lines[i - 1][j - 1] = tk.Button(self)
                self.lines[i - 1][j - 1].place(relx=i * 0.09, rely=(j + 0.65) * 0.09, height=15, width=30)

        for i in range(1, 9):
            for j in range(1, 10):
                self.walls[i - 1][j - 1] = tk.Button(self)
                self.walls[i - 1][j - 1].place(relx=(i + 0.65) * 0.09, rely=j * 0.09, height=30, width=15)

        BackButton = Button(self, text="back",
                            command=lambda: controller.show_frame("MenuPage"))
        BackButton.pack(side="bottom", fill="x", pady=10)

    def searching(self, buttons, key):
        for i in range(len(buttons)):
            for j in range(len(buttons[0])):
                print(buttons[i][j])
                if buttons[i][j] == key:
                    return i, j

        return -1, -1


class Quoridor4(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.controller = controller
        label = Label(self, text="You Are In Game!",
                      font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        BackButton = Button(self, text="back",
                            command=lambda: controller.show_frame("MenuPage"))
        BackButton.pack(side="bottom", fill="x", pady=10)


if __name__ == "__main__":
    app = QuoridorApp()
    app.geometry("500x500")
    app.mainloop()
    app.destroy()
