from graphics import *

PlayerX = [0, 16]
PlayerY = [8, 8]
Table = []
PlayerColor = ["red", "blue"]
WinPos = [16, 0]
win = ""
marked = []


def init():
    global Table
    Table = [['O' for i in range(17)] for j in range(17)]
    Table[0][8] = 'A'
    Table[16][8] = 'B'
    for i in range(1, 17, 2):
        for j in range(17):
            Table[i][j] = '*'
    for i in range(17):
        for j in range(1, 17, 2):
            Table[i][j] = '*'




def show_board():
    global Table
    for i in range(0, 17):
        for j in range(0, 17):
            if i % 2 == 0 and j % 2 == 0:
                c = Table[i][j]
                i2 = i / 2
                j2 = j / 2
                x1 = 60 / 2 + i2 * 100 / 2
                y1 = 60 / 2 + j2 * 100 / 2
                x1, y1 = y1, x1
                cell = Rectangle(Point(x1, y1), Point(x1 + 70 / 2, y1 + 70 / 2))

                if c == 'O':
                    pass
                elif c == 'A':
                    player = Circle(Point(x1 + 35 / 2, y1 + 35 / 2), 20 / 2)
                    player.setFill(PlayerColor[0])
                    player.draw(win)
                else:
                    player = Circle(Point(x1 + 35 / 2, y1 + 35 / 2), 20 / 2)
                    player.setFill(PlayerColor[1])
                    player.draw(win)
                cell.draw(win)
            elif i % 2 == 1 and j % 2 == 1:
                x = 60 + 50 * (i + 1) - 30
                y = 60 + 50 * (j + 1) - 30
                x /= 2
                y /= 2
                x, y = y, x
                wall = Rectangle(Point(x, y), Point(x + 30 / 2, y + 30 / 2))
                wall.setFill("red")
                if Table[i][j] == '#':
                    wall.draw(win)
            elif i % 2 == 1:
                x = 60 + 50 * (i - 1) + 70
                y = 60 + 50 * j
                x /= 2
                y /= 2
                x, y = y, x
                wall = Rectangle(Point(x, y), Point(x + 70 / 2, y + 30 / 2))
                wall.setFill("red")
                if Table[i][j] == '#':
                    wall.draw(win)
            else:
                y = 60 + 50 * (j - 1) + 70
                x = 60 + 50 * i
                x /= 2
                y /= 2
                x, y = y, x
                wall = Rectangle(Point(x, y), Point(x + 30 / 2, y + 70 / 2))
                wall.setFill("brown")
                if Table[i][j] == '#':
                    wall.draw(win)
def connected():
    return True

def show(i, j):
    i2 = i / 2
    j2 = j / 2
    x1 = 60 + i2 * 100
    y1 = 60 + j2 * 100
    x1 /= 2
    y1 /= 2
    x1, y1 = y1, x1
    c = Circle(Point(x1 + 35 / 2, y1 + 35 / 2), 20 / 2)
    c.setFill("gray")
    c.setOutline("gray")
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
                x1 /= 2
                y1 /= 2
                x1, y1 = y1, x1
                if x1 <= x <= x1 + 70 / 2 and y1 <= y <= y1 + 70 / 2:
                    if abs(PlayerX[player] - i) + abs(PlayerY[player] - j) == 4 and (PlayerX[player] != i and PlayerY[player] != j) and Table[(PlayerX[player] + i) // 2][(PlayerY[player] + j) // 2] != '#':
                        show(PlayerX[player], PlayerY[player])
                        Table[PlayerX[player]][PlayerY[player]] = 'O'
                        PlayerX[player] = i
                        PlayerY[player] = j
                        if player == 0:
                            Table[PlayerX[player]][PlayerY[player]] = 'A'
                        else:
                            Table[PlayerX[player]][PlayerY[player]] = 'B'
                        return True
                    if (abs(PlayerX[player] - i) + abs(PlayerY[player] - j) == 4) and (PlayerX[player] == i or PlayerY[player] == j) and Table[(PlayerX[player] + i) // 2][(PlayerY[player] + j) // 2] != 'O':
                        show(PlayerX[player], PlayerY[player])
                        Table[PlayerX[player]][PlayerY[player]] = 'O'
                        PlayerX[player] = i
                        PlayerY[player] = j
                        if player == 0:
                            Table[PlayerX[player]][PlayerY[player]] = 'A'
                        else:
                            Table[PlayerX[player]][PlayerY[player]] = 'B'
                        return True

                    if abs(PlayerX[player] - i) + abs(PlayerY[player] - j) > 2:
                        continue
                    if Table[(PlayerX[player] + i) // 2][(PlayerY[player] + j) // 2] == '#':
                        continue
                    if Table[i][j] != 'O':
                        continue
                    show(PlayerX[player], PlayerY[player])
                    Table[PlayerX[player]][PlayerY[player]] = 'O'
                    PlayerX[player] = i
                    PlayerY[player] = j
                    if player == 0:
                        Table[PlayerX[player]][PlayerY[player]] = 'A'
                    else:
                        Table[PlayerX[player]][PlayerY[player]] = 'B'
                    return True
            elif i % 2 == 1 and j % 2 == 1:
                continue
            elif i % 2 == 1:
                x1 = 60 + 50 * (i - 1) + 70
                y1 = 60 + 50 * j
                x1 /= 2
                y1 /= 2
                x1, y1 = y1, x1
                if x1 <= x <= x1 + 70 / 2 and y1 <= y <= y1 + 30 / 2:
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
                y1 = 30 + 25 * (j - 1) + 70 / 2
                x1 = 30 + 25 * i
                x1, y1 = y1, x1
                if x1 <= x <= x1 + 15 and y1 <= y <= y1 + 35:
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
    show_board()
    s = ""
    if player == 0:
        s = "First Player"
    else:
        s = "Second Player"
    message = Text(Point(475 / 2, 10 / 2), s)
    message.draw(win)
    done = False
    while done == False:
        done = play(player)

    message.undraw()


def game_over():
    for player in range(2):
        if PlayerX[player] == WinPos[player]:
            win.close()
            respage = GraphWin("Result", 500, 1000 / 2)
            respage.setBackground(PlayerColor[player])
            message = Text(Point(475 / 2, 10 / 2), "Click To Continue")
            message.draw(respage)
            respage.getMouse()
            return True
    return False


def main():
    global win
    win = GraphWin("Game Board", 500, 500)
    win.setBackground("gray")
    init()
    curplayer = 0
    while True:
        if game_over():
            exit()
        turn(curplayer)
        curplayer = curplayer ^ 1
