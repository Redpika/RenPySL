# Begin DEF

# directory path
# path of the current directory within the game
define THIS_PATH = 'snakesladders/'
define IMAGE_PATH = 'images/'

# file path
define IMG_BOARD = THIS_PATH + IMAGE_PATH + 'SL_TEMP.jpg'
define P1 = THIS_PATH + IMAGE_PATH + 'TempP1.jpg'
define P2 = THIS_PATH + IMAGE_PATH + 'TempP2.jpg'
define P3 = THIS_PATH + IMAGE_PATH + 'TempP3.jpg'
define P4 = THIS_PATH + IMAGE_PATH + 'TempP4.jpg'

# full-screen resolution
define SL_SCREEN_WIDTH = 1280
define SL_SCREEN_HEIGHT = 720
define SL_SIDE_LEN = SL_SCREEN_HEIGHT

define LOC_LEN = 90

define INDEX_MIN = 0
define INDEX_MAX = 9

define TEXT_SIZE = 26

# BEGIN STYLE

style control_button is button

# END STYLE

# BEGIN SCREEN

screen sl():

    default sl_displayable = SLDisplayable()
    add Solid('#000')

    fixed xpos 20 ypos 80 spacing 40:
        vbox:
            showif sl_displayable.winStat:
                text 'Player [sl_displayable.curPlayer] Wins!'
            else:
                text 'Player [sl_displayable.curPlayer]'

    fixed xpos 20 ypos 120 spacing 40:
        vbox:
            text "P1 pos: [sl_displayable.posList[0]]"
            text "P2 pos: [sl_displayable.posList[1]]"
            text "P3 pos: [sl_displayable.posList[2]]"
            text "P4 pos: [sl_displayable.posList[3]]"

    fixed xpos 20 ypos 240 spacing 40:
        vbox:
            text "Ladder"
            for start, end in sl_displayable.ladderPos.items():
                text "[start] -> [end]"

    fixed xpos 160 ypos 240 spacing 40:
        vbox:
            text "Snake"
            for start, end in sl_displayable.snakePos.items():
                text "[start] -> [end]"

    fixed xpos 20 ypos 440 spacing 40:
        vbox:
            text "Dice 1: [sl_displayable.diceResList[0]]"
            text "Dice 2: [sl_displayable.diceResList[1]]"

    fixed xpos 20 ypos 560:
        vbox:
            hbox spacing 5:
                textbutton 'Roll' action [
                    Function(sl_displayable.dice),
                    Function(sl_displayable.move),
                    Function(sl_displayable.check)
                ]

            hbox spacing 5:
                #showif sl_displayable.winStat:
                    textbutton 'Reset' action [
                        Function(sl_displayable.reset)
                    ]

            hbox spacing 5:
                textbutton 'Exit' action MainMenu()

    image IMG_BOARD:
        xpos 280
        zoom .9

    showif sl_displayable.maxPlayer > 0:
        image P1:
            xpos sl_displayable.gridCoord.get(sl_displayable.posList[0])[0]
            ypos sl_displayable.gridCoord.get(sl_displayable.posList[0])[1]
            zoom 0.5
    showif sl_displayable.maxPlayer > 1:
        image P2:
            xpos sl_displayable.gridCoord.get(sl_displayable.posList[1])[0]
            ypos sl_displayable.gridCoord.get(sl_displayable.posList[1])[1]
            zoom 0.5
    showif sl_displayable.maxPlayer > 2:
        image P3:
            xpos sl_displayable.gridCoord.get(sl_displayable.posList[2])[0]
            ypos sl_displayable.gridCoord.get(sl_displayable.posList[2])[1]
            zoom 0.5
    showif sl_displayable.maxPlayer > 3:
        image P4:
            xpos sl_displayable.gridCoord.get(sl_displayable.posList[3])[0]
            ypos sl_displayable.gridCoord.get(sl_displayable.posList[3])[1]
            zoom 0.5

# END SCREEN

init python:

    import os
    import sys
    import pygame
    import math
    import random

    class HoverDisplayable(renpy.Displayable):
        def __init__(self):
            super(HoverDisplayable, self).__init__()
            self.hover_coord = None
            self.hover_img = Solid(COLOR_HOVER, xsize=LOC_LEN, ysize=LOC_LEN)

        def render(self, width, height, st, at):
            render = renpy.Render(width, height)
            if self.hover_coord:
                render.place(self.hover_img,
                x=self.hover_coord[0], y=self.hover_coord[1],
                width=LOC_LEN, heigth=LOC_LEN)
            return render

        def event(self, ev, x, y, st):
            if 0 < x < SL_SIDE_LEN and 0 < y < SL_SIDE_LEN and ev.type == pygame.MOUSEMOTION:
                self.hover_coord = round_coord(x,y)
                renpy.redraw(self, 0)

    class SLDisplayable(renpy.Displayable):
        def __init__(self):
            super(SLDisplayable, self).__init__()
            self.posList = 4 * [0]
            self.curPlayer = 1
            self.maxPlayer = 4
            self.diceResList = 2 * [0]
            self.winStat = False
            self.ladderPos = {}
            self.snakePos = {}
            self.gridCoord = {}
            self.coordSetUp()
            random.seed()
            self.initiateSLPos()
            self.piece_img = {
            1: Image(P1),
            2: Image(P2),
            3: Image(P3),
            4: Image(P4)
            }

        def render(self, width, height, st, at):
            render = renpy.Render(width, height)

            return render

        def event(self, ev, x, y, st):
            pass

        def coordSetUp(self):
            self.gridCoord.update({0: [220, 660]})
            xBase = 290
            yBase = 660
            for i in range(0, 10):
                for j in range(1, 11):
                    if (i % 2) == 0:
                        xCoord = xBase + (72 * (j - 1))
                        yCoord = yBase - (72 * i)
                        gridNum = i * 10 + j
                        self.gridCoord.update({gridNum: [xCoord, yCoord]})
                    else:
                        xCoord = xBase + (72 * (10 - j))
                        yCoord = yBase - (72 * i)
                        gridNum = i * 10 + j
                        self.gridCoord.update({gridNum: [xCoord, yCoord]})

        def initiateSLPos(self):
            usedNumber = []
            for i in range(5):
                while True:
                    lStart = random.randint(1, 90)
                    if (lStart not in usedNumber):
                        while True:
                            newStart = self.round_up(lStart, -1)
                            lEnd = random.randint(newStart + 1, 99)
                            if (lEnd not in usedNumber):
                                self.ladderPos.update({lStart: lEnd})
                                usedNumber.append(lStart)
                                usedNumber.append(lEnd)
                                break
                        break
            for i in range(5):
                while True:
                    sStart = random.randint(11, 99)
                    if (sStart not in usedNumber):
                        while True:
                            newStart = self.round_down(sStart, -1)
                            sEnd = random.randint(1, newStart - 1)
                            if (sEnd not in usedNumber):
                                self.snakePos.update({sStart: sEnd})
                                usedNumber.append(sStart)
                                usedNumber.append(sEnd)
                                break
                        break

        def round_up(self, n, decimals=0):
            multiplier = 10 ** decimals
            return math.ceil(n * multiplier) / multiplier

        def round_down(self, n, decimals=0):
            multiplier = 10 ** decimals
            return math.floor(n * multiplier) / multiplier

        def dice(self):
            if not self.winStat:
                number1 = random.randint(1, 6)
                number2 = random.randint(1, 6)
                self.diceResList[0] = number1
                self.diceResList[1] = number2

        def move(self):
            if not self.winStat:
                diceTotal = self.diceResList[0] + self.diceResList[1]
                moveBack = False
                while diceTotal != 0:
                    if not moveBack:
                        self.posList[self.curPlayer - 1] = self.posList[self.curPlayer - 1] + 1
                    else:
                        self.posList[self.curPlayer - 1] = self.posList[self.curPlayer - 1] - 1
                    diceTotal-=1
                    if (self.posList[self.curPlayer - 1] == 100) and (diceTotal > 0):
                        moveBack = True

        def check(self):
            if self.posList[self.curPlayer - 1] in self.ladderPos:
                self.posList[self.curPlayer - 1] = self.ladderPos.get(self.posList[self.curPlayer - 1])
            elif self.posList[self.curPlayer - 1] in self.snakePos:
                self.posList[self.curPlayer - 1] = self.snakePos.get(self.posList[self.curPlayer - 1])
            if self.posList[self.curPlayer - 1] == 100:
                self.winStat = True
            else:
                self.curPlayer += 1
                if self.curPlayer > self.maxPlayer:
                    self.curPlayer = 1

        def reset(self):
            self.posList.clear()
            self.posList = 4 * [0]
            self.ladderPos.clear()
            self.snakePos.clear()
            self.diceResList.clear()
            self.diceResList = 2 * [0]
            self.winStat = False
            self.curPlayer = 1
            self.initiateSLPos()
