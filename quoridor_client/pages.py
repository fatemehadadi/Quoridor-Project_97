import wx

class StartPage(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.parent = parent
        wx.StaticText(self, label="Hello!")
        self.button = wx.Button(self, 1, label=" log in ", pos=(250, 100), size=(100, 50))
        self.Bind(wx.EVT_BUTTON, lambda e: self.parent.showpage("LogInPage"), id=1)
        self.button1 = wx.Button(self, 2, label=" register ", pos=(250, 150), size=(100, 50))
        self.Bind(wx.EVT_BUTTON, lambda e: self.parent.showpage("RegisterPage"), id=2)
        self.button2 = wx.Button(self, 3, label=" Rankings ", pos=(250, 200), size=(100, 50))
        self.Bind(wx.EVT_BUTTON, lambda e: self.parent.showpage("RankingsPage"), id=3)
        self.button3 = wx.Button(self, 4, label=" Quit ", pos=(250, 250), size=(100, 50))
        self.Bind(wx.EVT_BUTTON, lambda e: self.Close(True), id=4)


class logInPage(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.parent = parent
        self.label = wx.StaticText(self, label="Fill In The Data")
        self.button1 = wx.Button(self, label="Back", id=1, pos=(50, 50), size=(100, 50))
        self.button = wx.Button(self, label="Log In", id=2, pos=(50, 100), size=(100, 50))
        self.Bind(wx.EVT_BUTTON, lambda e: self.parent.showpage("StartPage"), id=1)
        self.Bind(wx.EVT_BUTTON, lambda e: self.checking(), id=2)

    def _is_valid(self):
        return True

    def checking(self):
        if self._is_valid():
            self.parent.showpage("MenuPage")


class RegisterPage(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.parent = parent


class MenuPage(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.parent = parent
        wx.StaticText(self, label="Hello!")
        wx.Button(self, 1, label=" log out ", pos=(250, 100), size=(100, 50))
        self.Bind(wx.EVT_BUTTON, lambda e: self.parent.showpage("StartPage"), id=1)
        wx.Button(self, 2, label=" Quoridor2 ", pos=(250, 150), size=(100, 50))
        self.Bind(wx.EVT_BUTTON, lambda e: self.parent.showpage("Quoridor2"), id=2)
        wx.Button(self, 3, label=" Quoridor4 ", pos=(250, 200), size=(100, 50))
        self.Bind(wx.EVT_BUTTON, lambda e: self.parent.showpage("Quoridor4"), id=3)
        wx.Button(self, 4, label=" Rankings ", pos=(250, 250), size=(100, 50))
        self.Bind(wx.EVT_BUTTON, lambda e: self.parent.showpage("RankingsPage"), id=4)


class Quoridor2(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.parent = parent



        self.button = wx.Button(self, 1, label=" back ", pos=(250, 500), size=(100, 50))
        self.Bind(wx.EVT_BUTTON, lambda e: self.parent.showpage("MenuPage"), id=1)

    def show_id(self, e):
        print(e.GetEventObject().GetId())


class Quoridor4(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.parent = parent


class RankingsPage(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.parent = parent
