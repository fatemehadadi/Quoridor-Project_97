import wx
import pages

class QuoridorApp(wx.Frame):
    def __init__(self, *args, **kw):
        super(QuoridorApp, self).__init__(*args, **kw)
        self.pages = [
            "StartPage", "LogInPage", "RegisterPage", "RankingsPage", "MenuPage", "Quoridor2", "Quoridor4"]
        self.prepage = None
        self.page = pages.StartPage(self)
        self.page_name = "StartPage"

    def showpage(self, page):
        if page in self.pages:
            self.prepage = self.page_name
            self.page_name = page
            self.page.Destroy()
            if page == "StartPage":
                self.page = pages.StartPage(self)
            elif page == "LogInPage":
                self.page = pages.logInPage(self)
            elif page == "RegisterPage":
                self.page = pages.RegisterPage(self)
            elif page == "RankingsPage":
                self.page = pages.RankingsPage(self)
            elif page == "MenuPage":
                self.page = pages.MenuPage(self)
            elif page == "Quoridor2":
                self.page = pages.Quoridor2(self)
            elif page == "Quoridor4":
                self.page = pages.Quoridor4(self)
            self.page.SetSize((584, 568))

    def backtopage(self):
        self.showpage(self.prepage)


if __name__ == "__main__":
    app = wx.App()
    frame = QuoridorApp(None, title="Quoridor App", size=(600, 600))
    frame.Show()
    app.MainLoop()
