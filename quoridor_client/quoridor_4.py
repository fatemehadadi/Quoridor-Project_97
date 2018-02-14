from graphics import *

PlayerX = [0, 16, 8, 8]

PlayerY = [8, 8, 16, 0]
Table = []
PlayerColor = ["red", "blue", "green", "yellow"]
WinPos = [16, 0, 0, 16]

marked = []
win=""

def init():
    global Table
    Table = [['O' for i in range(17)] for j in range(17)]
    Table[0][8] = 'A'
    Table[16][8] = 'B'
    Table[8][16] = 'C'
    Table[8][0] = 'D'
    for i in range(1, 17, 2):
        for j in range(17):
            Table[i][j] = '*'
    for i in range(17):
        for j in range(1, 17, 2):
            Table[i][j] = '*'


def ok(i1, j1, i, j):
    if i >= 0 and j >= 0 and i < 17 and j < 17 and (not marked[i][j]) and Table[(i + i1) // 2][
        (j + j1) // 2] != '#':
        return True
    return False


def dfs(i, j):
    global marked
    marked[i][j] = True
    if ok(i, j, i + 2, j):
        dfs(i + 2, j)
    if ok(i, j, i, j + 2):
        dfs(i, j + 2)
    if ok(i, j, i - 2, j):
        dfs(i - 2, j)
    if ok(i, j, i, j - 2):
        dfs(i, j - 2)


def connected():
    global marked
    marked = [[0 for i in range(17)] for j in range(17)]
    dfs(0, 0)
    for i in range(0, 17, 2):
        for j in range(0, 17, 2):
            if not marked[i][j]:
                return False
    return True


def Print_Table():
    global Table
    for i in range(0, 17):
        for j in range(0, 17):
            if i % 2 == 0 and j % 2 == 0:
                c = Table[i][j]
                i2 = i / 2
                j2 = j / 2
                x1 = 60 + i2 * 100
                y1 = 60 + j2 * 100
                x1, y1 = y1, x1
                cell = Rectangle(Point(x1, y1), Point(x1 + 70, y1 + 70))

                if c == 'O':
                    pass
                elif c == 'A':
                    player = Circle(Point(x1 + 35, y1 + 35), 20)
                    player.setFill(PlayerColor[0])
                    player.draw(win)
                elif c == 'B':
                    player = Circle(Point(x1 + 35, y1 + 35), 20)
                    player.setFill(PlayerColor[1])
                    player.draw(win)
                elif c == 'C':
                    player = Circle(Point(x1 + 35, y1 + 35), 20)
                    player.setFill(PlayerColor[2])
                    player.draw(win)
                else:
                    player = Circle(Point(x1 + 35, y1 + 35), 20)
                    player.setFill(PlayerColor[3])
                    player.draw(win)
                cell.draw(win)
            elif i % 2 == 1 and j % 2 == 1:
                x = 60 + 50 * (i + 1) - 30
                y = 60 + 50 * (j + 1) - 30
                x, y = y, x
                wall = Rectangle(Point(x, y), Point(x + 30, y + 30))
                wall.setFill("brown")
                if Table[i][j] == '#':
                    wall.draw(win)
            elif i % 2 == 1:
                x = 60 + 50 * (i - 1) + 70
                y = 60 + 50 * j
                x, y = y, x
                wall = Rectangle(Point(x, y), Point(x + 70, y + 30))
                wall.setFill("brown")
                if Table[i][j] == '#':
                    wall.draw(win)
            else:
                y = 60 + 50 * (j - 1) + 70
                x = 60 + 50 * i
                x, y = y, x
                wall = Rectangle(Point(x, y), Point(x + 30, y + 70))
                wall.setFill("brown")
                if Table[i][j] == '#':
                    wall.draw(win)


def UnDraw(i, j):
    i2 = i / 2
    j2 = j / 2
    x1 = 60 + i2 * 100
    y1 = 60 + j2 * 100
    x1, y1 = y1, x1
    c = Circle(Point(x1 + 35, y1 + 35), 20)
    c.setFill("lightblue")
    c.setOutline("lightblue")
    c.draw(win)


def play(player):
    global PlayerX
    global PlayerY
    global Table
    clickPoint = win.getMouse()
    x = clickPoint.getX()
    y = clickPoint.getY()
    for i in range(17):
        for j in range(17):
            if i % 2 == 0 and j % 2 == 0:
                i2 = i / 2
                j2 = j / 2
                x1 = 60 + i2 * 100
                y1 = 60 + j2 * 100
                x1, y1 = y1, x1
                if x1 <= x <= x1 + 70 and y1 <= y <= y1 + 70:
                    if (abs(PlayerX[player] - i) + abs(PlayerY[player] - j) == 4) and (
                            PlayerX[player] == i or PlayerY[player] == j) and Table[(PlayerX[player] + i) // 2][
                        (PlayerY[player] + j) // 2] != 'O' and Table[i][j] == 'O':
                        UnDraw(PlayerX[player], PlayerY[player])
                        Table[PlayerX[player]][PlayerY[player]] = 'O'
                        PlayerX[player] = i
                        PlayerY[player] = j
                        if player == 0:
                            Table[PlayerX[player]][PlayerY[player]] = 'A'
                        elif player == 1:
                            Table[PlayerX[player]][PlayerY[player]] = 'B'
                        elif player == 2:
                            Table[PlayerX[player]][PlayerY[player]] = 'C'
                        else:
                            Table[PlayerX[player]][PlayerY[player]] = 'D'
                        return True

                    if abs(PlayerX[player] - i) + abs(PlayerY[player] - j) > 2:
                        continue
                    if Table[(PlayerX[player] + i) // 2][(PlayerY[player] + j) // 2] == '#':
                        continue
                    if Table[i][j] != 'O':
                        continue
                    UnDraw(PlayerX[player], PlayerY[player])
                    Table[PlayerX[player]][PlayerY[player]] = 'O'
                    PlayerX[player] = i
                    PlayerY[player] = j
                    if player == 0:
                        Table[PlayerX[player]][PlayerY[player]] = 'A'
                    elif player == 1:
                        Table[PlayerX[player]][PlayerY[player]] = 'B'
                    elif player == 2:
                        Table[PlayerX[player]][PlayerY[player]] = 'C'
                    else:
                        Table[PlayerX[player]][PlayerY[player]] = 'D'
                    return True
            elif i % 2 == 1 and j % 2 == 1:
                continue
            elif i % 2 == 1:
                x1 = 60 + 50 * (i - 1) + 70
                y1 = 60 + 50 * j
                x1, y1 = y1, x1
                if x1 <= x <= x1 + 70 and y1 <= y <= y1 + 30:
                    if j + 2 <= 17 and Table[i][j] != '#' and Table[i][j + 1] != '#' and Table[i][j + 2] != '#':
                        Table[i][j] = '#'
                        Table[i][j + 1] = '#'
                        Table[i][j + 2] = '#'
                        if not connected():
                            Table[i][j] = '*'
                            Table[i][j + 1] = '*'
                            Table[i][j + 2] = '*'
                            return False
                        return True
            else:
                y1 = 60 + 50 * (j - 1) + 70
                x1 = 60 + 50 * i
                x1, y1 = y1, x1
                if x1 <= x <= x1 + 30 and y1 <= y <= y1 + 70:
                    if i + 2 <= 17 and Table[i][j] != '#' and Table[i + 1][j] != '#' and Table[i + 2][j] != '#':
                        Table[i][j] = '#'
                        Table[i + 1][j] = '#'
                        Table[i + 2][j] = '#'
                        if not connected():
                            Table[i][j] = '*'
                            Table[i + 1][j] = '*'
                            Table[i + 2][j] = '*'
                            return False
                        return True
    return False


def turn(player):
    Print_Table()
    s = ""
    if player == 0:
        s = "First Player Click To Place Wall Or To Move To A Cell"
    elif player == 1:
        s = "Second Player Click To Place Wall Or To Move To A Cell"
    elif player == 2:
        s = "Third Player Click To Place Wall Or To Move To A Cell"
    else:
        s = "Fourth Player Click To Place Wall Or To Move To A Cell"
    message = Text(Point(475, 10), s)
    message.draw(win)
    done = False
    while done == False:
        done = play(player)
    message.undraw()


def game_over():
    for player in range(2):
        if PlayerX[player] == WinPos[player]:
            win.close()
            respage = GraphWin("Result", 1000, 1000)
            respage.setBackground(PlayerColor[player])
            message = Text(Point(475, 10), "Click To Continue")
            message.draw(respage)
            respage.getMouse()
            return True
    for player in range(2, 4):
        if PlayerY[player] == WinPos[player]:
            win.close()
            respage = GraphWin("Result", 1000, 1000)
            respage.setBackground(PlayerColor[player])
            message = Text(Point(475, 10), "Click To Continue")
            message.draw(respage)
            respage.getMouse()
            return True
    return False


def main():
    global win
    win = GraphWin("Game Board", 1000, 1000)
    win.setBackground("lightblue")
    init()
    curplayer = 0
    while True:
        if game_over():
            exit()
        turn(curplayer)
        curplayer = (curplayer + 1) % 4
main()
