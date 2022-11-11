# Begin DEF

# directory path
# path of the current directory within the game
define THIS_PATH = 'snakesladders/'
define IMAGE_PATH = 'images/'
define LADDER_START = 'LSt/'
define LADDER_END = 'LEn/'
define SNAKE_START = 'SSt/'
define SNAKE_END = 'SEn/'
define SFX_PATH = 'sfx/'

# Image
define IMG_BOARD = THIS_PATH + IMAGE_PATH + 'Board.png'
define P1 = THIS_PATH + IMAGE_PATH + 'P1.png'
define P2 = THIS_PATH + IMAGE_PATH + 'P2.png'
define P3 = THIS_PATH + IMAGE_PATH + 'P3.png'
define P4 = THIS_PATH + IMAGE_PATH + 'P4.png'
define P1BIG = THIS_PATH + IMAGE_PATH + 'P1Big.png'
define P2BIG = THIS_PATH + IMAGE_PATH + 'P2Big.png'
define P3BIG = THIS_PATH + IMAGE_PATH + 'P3Big.png'
define P4BIG = THIS_PATH + IMAGE_PATH + 'P4Big.png'
define DICE_SCREEN = THIS_PATH + IMAGE_PATH + 'dice_screen.png'
define WIN_SCREEN = THIS_PATH + IMAGE_PATH + 'win_screen.png'
define D1 = THIS_PATH + IMAGE_PATH + 'D1.png'
define D2 = THIS_PATH + IMAGE_PATH + 'D2.png'
define D3 = THIS_PATH + IMAGE_PATH + 'D3.png'
define D4 = THIS_PATH + IMAGE_PATH + 'D4.png'
define D5 = THIS_PATH + IMAGE_PATH + 'D5.png'
define D6 = THIS_PATH + IMAGE_PATH + 'D6.png'
define UIUL = THIS_PATH + IMAGE_PATH + 'ULeft.png'
define UIML = THIS_PATH + IMAGE_PATH + 'MLeft.png'
define UIBL = THIS_PATH + IMAGE_PATH + 'BLeft.png'
define UIUR = THIS_PATH + IMAGE_PATH + 'URight.png'
define UIMR = THIS_PATH + IMAGE_PATH + 'MRight.png'
define UIBR = THIS_PATH + IMAGE_PATH + 'BRight.png'
define ICON1 = THIS_PATH + IMAGE_PATH + 'icon1.png'
define ICON2 = THIS_PATH + IMAGE_PATH + 'icon2.png'
define ICON3 = THIS_PATH + IMAGE_PATH + 'icon3.png'
define ICON4 = THIS_PATH + IMAGE_PATH + 'icon4.png'
define ICON5 = THIS_PATH + IMAGE_PATH + 'icon5.png'
define ICON6 = THIS_PATH + IMAGE_PATH + 'icon6.png'
define ICON7 = THIS_PATH + IMAGE_PATH + 'icon7.png'
define ICON8 = THIS_PATH + IMAGE_PATH + 'icon8.png'
define ICON9 = THIS_PATH + IMAGE_PATH + 'icon9.png'
define ICON10 = THIS_PATH + IMAGE_PATH + 'icon10.png'
define SLIDE_SFX = THIS_PATH + SFX_PATH + 'piece-slide.mp3'
define PLACE_SFX = THIS_PATH + SFX_PATH + 'piece-place.wav'

# screen constant
define LOC_LEN = 72
define MAX_ZOOM = 0.1
define BIG_ZOOM = 0.2
define MOVEMENT = 2
define LAUNCH_COUNT = 36

# styles
style roll_text:
    color "#12ed4f"
    #hover_color "#0aff1d"
    hover_color "#00b00d"
    hover_bold True
style exit_text:
    color "#ff0004"
    #hover_color "#ff6466"
    hover_color "#c10003"
    hover_bold True
style again_text:
    color "#2d00ff"
    # hover_color "#6847ff"
    hover_color "#2000b6"
    hover_bold True
style p1_text:
    color "#FF0000"
style p2_text:
    color "#0070C0"
style p3_text:
    color "#548235"
style p4_text:
    color "#FFFF00"

# BEGIN SCREEN

screen sl(maxPlayer, p1, p2, p3, p4):

    default sl_displayable = SLDisplayable(
        maxPlayer = maxPlayer,
        p1 = p1,
        p2 = p2,
        p3 = p3,
        p4 = p4
    )
    add Solid('#000')

    fixed xpos 0 ypos 0:
        add Image(UIUL)
    fixed xpos 69 ypos 48:
        add sl_displayable.playerBig[sl_displayable.curPlayer]
    fixed xpos 20 ypos 20 spacing 40:
        vbox:
            if sl_displayable.playerStat[sl_displayable.curPlayer - 1] == 2:
                if sl_displayable.curPlayer == 1:
                    text '{=p1_text}Computer [sl_displayable.curPlayer]{/p1_text}'
                elif sl_displayable.curPlayer == 2:
                    text '{color=#0070C0}Computer [sl_displayable.curPlayer]{/p2_text}'
                elif sl_displayable.curPlayer == 3:
                    text '{color=#548235}Computer [sl_displayable.curPlayer]{/p3_text}'
                elif sl_displayable.curPlayer == 4:
                    text '{color=#FFFF00}Computer [sl_displayable.curPlayer]{/p4_text}'
            else:
                if sl_displayable.curPlayer == 1:
                    text '{color=#FF0000}Player [sl_displayable.curPlayer]{/p1_text}'
                elif sl_displayable.curPlayer == 2:
                    text '{color=#0070C0}Player [sl_displayable.curPlayer]{/p2_text}'
                elif sl_displayable.curPlayer == 3:
                    text '{color=#548235}Player [sl_displayable.curPlayer]{/p3_text}'
                elif sl_displayable.curPlayer == 4:
                    text '{color=#FFFF00}Player [sl_displayable.curPlayer]{/p4_text}'

    fixed xpos 0 ypos 240:
        add Image(UIML)
    fixed xpos 20 ypos 260 spacing 40:
        vbox:
            text "{=p1_text}P1 pos: [sl_displayable.posList[0]]{/p1_text}"
            text "{=p2_text}P2 pos: [sl_displayable.posList[1]]{/p2_text}"
            if sl_displayable.maxPlayer >= 3:
                text "{=p3_text}P3 pos: [sl_displayable.posList[2]]{/p3_text}"
            if sl_displayable.maxPlayer == 4:
                text "{=p4_text}P4 pos: [sl_displayable.posList[3]]{/p4_text}"

    fixed xpos 0 ypos 480:
        add Image(UIBL)
    fixed xpos 20 ypos 500 spacing 40:
        vbox:
            text "{color=#548235}Ladder{/color}"
            for start, end in sl_displayable.ladderPos.items():
                text "{color=#2D4D17}[start]{/color} {color=#548235}->{/color} {color=#A7C09C}[end]{/color}"
    fixed xpos 160 ypos 500 spacing 40:
        vbox:
            text "{color=#FF0000}Snake{/color}"
            for start, end in sl_displayable.snakePos.items():
                text "{color=#770000}[start]{/color} {color=#FF0000}->{/color} {color=#EA8C8C}[end]{/color}"

    fixed xpos 280:
        add Image(IMG_BOARD)
        add sl_displayable

    fixed xpos 1000 ypos 0:
        add Image(UIUR)
    fixed xpos 1020 ypos 20 spacing 40:
        $ distanceLeft = 100 - sl_displayable.posList[sl_displayable.curPlayer-1]
        vbox:
            text '{color=#000000}Distance Left:{/color}'
            text '{color=#000000}{b}[distanceLeft]{/b}'

    fixed xpos 1000 ypos 250:
        add Image(UIMR)
    fixed xpos 1020 ypos 270 spacing 40:
        if sl_displayable.diceTotal > 0:
            $ spaceLeft = sl_displayable.diceTotal
        else:
            $ spaceLeft = 0
        vbox:
            text '{color=#000000}Space Left:{/color}'
            text '{color=#000000}{b}[spaceLeft]{/b}{/color}'

    fixed xpos 1000 ypos 500:
        add Image(UIBR)
    fixed xpos 1020 ypos 520:
        vbox:
            if not sl_displayable.winStat:
                hbox spacing 5:
                    showif ((sl_displayable.diceTotal == 0 and not sl_displayable.onMove) or (sl_displayable.onLaunch)) and (sl_displayable.playerStat[sl_displayable.curPlayer - 1] != 2):
                        textbutton 'Roll' text_style "roll_text" action [
                            Function(sl_displayable.dice)
                        ]
                hbox spacing 5:
                    textbutton 'Exit' text_style "exit_text" action MainMenu()

screen rollerScreen(sl_displayable):
    fixed xpos 0 ypos 120:
        add Image(DICE_SCREEN)
    fixed xpos 250 ypos 143:
        add sl_displayable.curDiceImage[0]
    fixed xpos 680 ypos 143:
        add sl_displayable.curDiceImage[1]

screen winScreen(sl_displayable):
    fixed xpos 0 ypos 120:
        add Image (WIN_SCREEN)
    fixed ypos 165:
        vbox:
            hbox spacing 5:
                xpos 525
                text '{color=#00ff00}{b}CONGRATULATIONS!{/b}{/color}'
            hbox spacing 5:
                if sl_displayable.playerStat[sl_displayable.curPlayer - 1] == 2:
                    xpos 543
                    if sl_displayable.curPlayer == 1:
                        text '{color=#FF0000}{b}Computer [sl_displayable.curPlayer] Wins!{/b}{/color}'
                    elif sl_displayable.curPlayer == 2:
                        text '{color=#0070C0}{b}Computer [sl_displayable.curPlayer] Wins!{/b}{/color}'
                    elif sl_displayable.curPlayer == 3:
                        text '{color=#548235}{b}Computer [sl_displayable.curPlayer] Wins!{/b}{/color}'
                    elif sl_displayable.curPlayer == 4:
                        text '{color=#FFFF00}{b}Computer [sl_displayable.curPlayer] Wins!{/b}{/color}'
                else:
                    xpos 560
                    if sl_displayable.curPlayer == 1:
                        text '{color=#FF0000}{b}Player [sl_displayable.curPlayer] Wins!{/b}{/color}'
                    elif sl_displayable.curPlayer == 2:
                        text '{color=#0070C0}{b}Player [sl_displayable.curPlayer] Wins!{/b}{/color}'
                    elif sl_displayable.curPlayer == 3:
                        text '{color=#548235}{b}Player [sl_displayable.curPlayer] Wins!{/b}{/color}'
                    elif sl_displayable.curPlayer == 4:
                        text '{color=#FFFF00}{b}Player [sl_displayable.curPlayer] Wins!{/b}{/color}'
    fixed xpos 535 ypos 210:
        add sl_displayable.playerBig[sl_displayable.curPlayer]:
            zoom 1.5
    fixed xpos 370 ypos 450:
        textbutton 'Play Again' text_style "again_text" action [
            Function(sl_displayable.reset)
        ]
    fixed xpos 795 ypos 450:
        textbutton 'End Game' text_style "exit_text" action [
            Hide(screen = "winScreen"),
            Return(sl_displayable.curPlayer)
        ]

# END SCREEN

init python:

    import os
    import sys
    import pygame
    import math
    import random
    import time

    class SLDisplayable(renpy.Displayable):
        def __init__(self, maxPlayer = 4, p1 = 0, p2 = 0, p3 = 0, p4 = 0):
            super(SLDisplayable, self).__init__()
            self.posList = 4 * [0]
            self.curPlayer = 1
            self.maxPlayer = maxPlayer
            self.playerStat = [p1, p2, p3, p4]
            self.diceResList = 2 * [0]
            self.diceTotal = 0
            self.winStat = False
            self.moveBack = False
            self.ladderPos = {}
            self.snakePos = {}
            self.gridCoord = {}
            self.lStImage = {}
            self.lEnImage = {}
            self.sStImage = {}
            self.sEnImage = {}
            self.onDice = False
            self.afterDice = False
            self.keyFrame = 0
            self.onMove = False
            self.diceRandMax = 0
            self.diceRandCount = 0
            self.onLaunch = False
            self.oldCoord = 0
            self.launchCount = 0
            self.xLaunch = 0
            self.yLaunch = 0
            self.coordSetUp()
            random.seed()
            self.initiateSLPos()
            self.playerPiece = {
            0: Transform(Image(P1), zoom=MAX_ZOOM),
            1: Transform(Image(P2), zoom=MAX_ZOOM),
            2: Transform(Image(P3), zoom=MAX_ZOOM),
            3: Transform(Image(P4), zoom=MAX_ZOOM),
            }
            self.playerBig = {
            1: Transform(Image(P1BIG), zoom=BIG_ZOOM),
            2: Transform(Image(P2BIG), zoom=BIG_ZOOM),
            3: Transform(Image(P3BIG), zoom=BIG_ZOOM),
            4: Transform(Image(P4BIG), zoom=BIG_ZOOM),
            }
            self.diceImage = {
            1: Transform(Image(D1)),
            2: Transform(Image(D2)),
            3: Transform(Image(D3)),
            4: Transform(Image(D4)),
            5: Transform(Image(D5)),
            6: Transform(Image(D6)),
            }
            self.iconImage = {
            1: Transform(Image(ICON1), zoom=0.1),
            2: Transform(Image(ICON2), zoom=0.1),
            3: Transform(Image(ICON3), zoom=0.1),
            4: Transform(Image(ICON4), zoom=0.1),
            5: Transform(Image(ICON5), zoom=0.1),
            6: Transform(Image(ICON6), zoom=0.1),
            7: Transform(Image(ICON7), zoom=0.1),
            8: Transform(Image(ICON8), zoom=0.1),
            9: Transform(Image(ICON9), zoom=0.1),
            10: Transform(Image(ICON10), zoom=0.1),
            }
            self.curDiceImage = [self.diceImage.get(1), self.diceImage.get(1)]


        def render(self, width, height, st, at):
            render = renpy.Render(width, height)

            Icon = 1
            for lStart, lEnd in self.ladderPos.items():
                render.place(self.lStImage[lStart], x = self.gridCoord.get(lStart)[0], y = self.gridCoord.get(lStart)[1])
                render.place(self.lEnImage[lEnd], x = self.gridCoord.get(lEnd)[0], y = self.gridCoord.get(lEnd)[1])
                render.place(self.iconImage[Icon], x = self.gridCoord.get(lStart)[0], y = self.gridCoord.get(lStart)[1])
                render.place(self.iconImage[Icon], x = self.gridCoord.get(lEnd)[0], y = self.gridCoord.get(lEnd)[1])
                Icon += 1

            for sStart, sEnd in self.snakePos.items():
                render.place(self.sStImage[sStart], x = self.gridCoord.get(sStart)[0], y = self.gridCoord.get(sStart)[1])
                render.place(self.sEnImage[sEnd], x = self.gridCoord.get(sEnd)[0], y = self.gridCoord.get(sEnd)[1])
                render.place(self.iconImage[Icon], x = self.gridCoord.get(sStart)[0], y = self.gridCoord.get(sStart)[1])
                render.place(self.iconImage[Icon], x = self.gridCoord.get(sEnd)[0], y = self.gridCoord.get(sEnd)[1])
                Icon += 1

            if not self.winStat:
                if self.diceTotal != 0 and not self.onMove and not self.onLaunch:
                    self.move()
                if self.playerStat[self.curPlayer-1] == 2 and self.diceTotal == 0 and not self.onMove and not self.onLaunch:
                    time.sleep(0.5)
                    self.dice()
            if self.afterDice:
                time.sleep(1)
                renpy.hide_screen("rollerScreen")
                self.afterDice = False
            for i in range(0, self.maxPlayer):
                if self.posList[i] != 0:
                    if i != self.curPlayer-1 or self.posList[i]-1 == 0 or (not self.onMove and not self.onLaunch):
                        render.place(self.playerPiece[i], x=self.gridCoord.get(self.posList[i])[0], y=self.gridCoord.get(self.posList[i])[1])

                    if self.onMove and i == self.curPlayer-1:
                        if self.posList[i] <= 1:
                            self.onMove = False
                        else:
                            self.keyFrame += 1
                            if self.round_up(self.posList[i]-1, -1) == self.round_up(self.posList[i], -1):
                                x_offset = self.keyFrame * MOVEMENT
                                y_offset = 0
                            else:
                                x_offset = 0
                                y_offset = self.keyFrame * MOVEMENT
                            if self.moveBack and self.posList[i] != 100:
                                render.place(self.playerPiece[i], x = (self.gridCoord.get(self.posList[i]+1)[0] + x_offset), y = (self.gridCoord.get(self.posList[i])[1] - y_offset))
                            elif (self.round_up(self.posList[i]-1,-1)/10)%2 == 1:
                                render.place(self.playerPiece[i], x = (self.gridCoord.get(self.posList[i]-1)[0] + x_offset), y = (self.gridCoord.get(self.posList[i]-1)[1] - y_offset))
                            else:
                                render.place(self.playerPiece[i], x = (self.gridCoord.get(self.posList[i]-1)[0] - x_offset), y = (self.gridCoord.get(self.posList[i]-1)[1] - y_offset))
                            if self.keyFrame * MOVEMENT == LOC_LEN:
                                self.onMove = False
                                self.keyFrame = 0
                                if self.diceTotal == 0:
                                    self.moveBack = False
                                    self.check()
                                renpy.redraw(self, 0.2)
                            else:
                                renpy.redraw(self, 0)

                    elif self.onLaunch and i == self.curPlayer-1:
                        self.launchCount += 1
                        if self.launchCount <=5:
                            self.playerPiece[i] = Transform(self.playerPiece[i], zoom=0.9)
                        elif self.launchCount >=(LAUNCH_COUNT - 5):
                            self.playerPiece[i] = Transform(self.playerPiece[i], zoom=10/9)
                        x_offset = self.xLaunch * self.launchCount
                        y_offset = self.yLaunch * self.launchCount
                        render.place(self.playerPiece[i], x = (self.gridCoord.get(self.oldCoord)[0] + x_offset), y = (self.gridCoord.get(self.oldCoord)[1] + y_offset))
                        if self.launchCount == LAUNCH_COUNT:
                            self.onLaunch = False
                            self.launchCount = 0
                            self.xLaunch = 0
                            self.yLaunch = 0
                            if i == 0:
                                self.playerPiece[i] = Transform(Image(P1), zoom = MAX_ZOOM)
                            elif i == 1:
                                self.playerPiece[i] = Transform(Image(P2), zoom = MAX_ZOOM)
                            elif i == 2:
                                self.playerPiece[i] = Transform(Image(P3), zoom = MAX_ZOOM)
                            elif i == 3:
                                self.playerPiece[i] = Transform(Image(P4), zoom = MAX_ZOOM)
                            renpy.sound.play(PLACE_SFX)
                            renpy.redraw(self, 0.2)
                            self.check()
                        else:
                            renpy.redraw(self, 0.1)
            if self.onDice:
                self.diceRandCount += 1
                self.curDiceImage[0] = self.diceImage.get(random.randint(1, 6))
                self.curDiceImage[1] = self.diceImage.get(random.randint(1, 6))
                if self.diceRandCount == self.diceRandMax:
                    self.onDice = False
                    self.diceRandCount = 0
                    self.curDiceImage[0] = self.diceImage.get(self.diceResList[0])
                    self.curDiceImage[1] = self.diceImage.get(self.diceResList[1])
                    self.afterDice = True
                renpy.redraw(self, 0.1)
            renpy.restart_interaction()
            return render

        def event(self, ev, x, y, st):
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_SPACE:
                    if (self.playerStat[self.curPlayer-1] and self.diceTotal == 0 and not self.onMove) or not self.onLaunch:
                        self.dice()

        def coordSetUp(self):
            for i in range(0, 10):
                for j in range(1, 11):
                    gridNum = i * 10 + j
                    lStPath = os.path.join(THIS_PATH, IMAGE_PATH, LADDER_START, str(gridNum) + '.png')
                    lEnPath = os.path.join(THIS_PATH, IMAGE_PATH, LADDER_END, str(gridNum) + '.png')
                    sStPath = os.path.join(THIS_PATH, IMAGE_PATH, SNAKE_START, str(gridNum) + '.png')
                    sEnPath = os.path.join(THIS_PATH, IMAGE_PATH, SNAKE_END, str(gridNum) + '.png')
                    self.lStImage.update({gridNum: Transform(Image(lStPath))})
                    self.lEnImage.update({gridNum: Transform(Image(lEnPath))})
                    self.sStImage.update({gridNum: Transform(Image(sStPath))})
                    self.sEnImage.update({gridNum: Transform(Image(sEnPath))})
                    if (i % 2) == 0:
                        xCoord = LOC_LEN * (j - 1)
                        yCoord = LOC_LEN * (9 - i)
                        self.gridCoord.update({gridNum: [xCoord, yCoord]})
                    else:
                        xCoord = LOC_LEN * (10 - j)
                        yCoord = LOC_LEN * (9 - i)
                        self.gridCoord.update({gridNum: [xCoord, yCoord]})


        def initiateSLPos(self):
            usedNumber = []
            for i in range(5):
                while True:
                    lStart = random.randint(2, 90)
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
                            if sStart%10 == 0:
                                newStart = sStart-9
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
            if not self.winStat and self.diceTotal == 0:
                number1 = random.randint(1, 6)
                number2 = random.randint(1, 6)
                self.diceResList[0] = number1
                self.diceResList[1] = number2
                self.diceTotal = number1 + number2
                # self.diceTotal = 100
                self.onDice = True
                self.diceRandMax = random.randint(15, 20)
                renpy.show_screen("rollerScreen", sl_displayable = self)
                renpy.redraw(self, 0)

        def move(self):
            if not self.winStat and not self.onDice and self.diceTotal != 0:
                self.onMove = True
                self.diceTotal-=1
                if not self.moveBack:
                    self.posList[self.curPlayer - 1] = self.posList[self.curPlayer - 1] + 1
                else:
                    self.posList[self.curPlayer - 1] = self.posList[self.curPlayer - 1] - 1
                if (self.posList[self.curPlayer - 1] == 100) and (self.diceTotal > 0):
                    self.moveBack = True
                renpy.sound.play(SLIDE_SFX)
                renpy.redraw(self, 0)

        def check(self):
            if self.posList[self.curPlayer - 1] in self.ladderPos:
                self.launcher(self.posList[self.curPlayer - 1], self.ladderPos.get(self.posList[self.curPlayer - 1]))
                self.posList[self.curPlayer - 1] = self.ladderPos.get(self.posList[self.curPlayer - 1])
            elif self.posList[self.curPlayer - 1] in self.snakePos:
                self.launcher(self.posList[self.curPlayer - 1], self.snakePos.get(self.posList[self.curPlayer - 1]))
                self.posList[self.curPlayer - 1] = self.snakePos.get(self.posList[self.curPlayer - 1])
            if self.posList[self.curPlayer - 1] == 100:
                self.winStat = True
                renpy.show_screen("winScreen", sl_displayable = self)
            elif not self.onLaunch:
                self.curPlayer += 1
                if self.curPlayer > self.maxPlayer:
                    self.curPlayer = 1

        def launcher(self, oldCoord, newCoord):
            self.onLaunch = True
            self.oldCoord = oldCoord
            oldX = self.gridCoord.get(oldCoord)[0]
            oldY = self.gridCoord.get(oldCoord)[1]
            newX = self.gridCoord.get(newCoord)[0]
            newY = self.gridCoord.get(newCoord)[1]
            self.xLaunch = (newX - oldX)/LAUNCH_COUNT
            self.yLaunch = (newY - oldY)/LAUNCH_COUNT
            renpy.redraw(self, 0.2)

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
            renpy.redraw(self, 0)
            renpy.hide_screen("winScreen")
