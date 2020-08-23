from math import pi, sin, cos
import random
import pygame
import time

# Initiate PyGame
pygame.init()

# Display
weightWin = 1250
hightWin = 834
text = ''
win = pygame.display.set_mode((weightWin, hightWin))   # center: 625, 417
pygame.display.set_caption("casiCaracol")
icon = pygame.image.load('images/beer.png')
pygame.display.set_icon(icon)
message = pygame.font.SysFont('Comic Sans MS', 15)
title = pygame.font.SysFont('Arial', 130)
textOnScreen = message.render(text, True, (0, 0, 0), (255, 255, 255))
win.blit(textOnScreen, (int(weightWin / 2), int(hightWin / 2)))

# Images
bg = pygame.image.load('images/background.jpg')
redButton = pygame.image.load('images/red-button.png')
redButton = pygame.transform.scale(redButton, (128, 128))
blackButton = pygame.image.load('images/black-button.png')
blackButton = pygame.transform.scale(blackButton, (128, 128))
higher = pygame.image.load('images/up-arrow.png')
higher = pygame.transform.scale(higher, (128, 128))
lower = pygame.image.load('images/down-arrow.png')
lower = pygame.transform.scale(lower, (128, 128))
back = pygame.image.load('images/cards/back.png')
rotate_back = pygame.transform.rotate(back, 90)
startButton = pygame.image.load('images/start-button.png')
startButton = pygame.transform.scale(startButton, (500, 206))
exitButton = pygame.image.load('images/exit-button.png')
exitButton = pygame.transform.scale(exitButton, (200, 108))
beer = pygame.image.load('images/big-beer.png')
beer = pygame.transform.scale(beer, (250, 250))



# Game Logic
#               1. Se ponen todas las cartas boca abajo sobre la mesa formando un espiral
#               2. Se comienza dando vuelta la primera carta (la mas lejana al centro)
#               3. El primer jugador debe dar vuelta la carta escoginaod una de las siguientes opciones: mayor, menor, negro, rojo
#               4. En caso de seleccionar un



# Variables
listCards = ['c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'c10', 'c11', 'c12',  'c13',
             'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9', 'd10', 'd11', 'd12',  'd13',
             'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8', 'h9', 'h10', 'h11', 'h12',  'h13',
             's1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's10', 's11', 's12',  's13',
             'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'c10', 'c11', 'c12',  'c13',
             'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9', 'd10', 'd11', 'd12',  'd13',
             'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8', 'h9', 'h10', 'h11', 'h12',  'h13',
             's1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's10', 's11', 's12',  's13']
random.shuffle(listCards)
copyListCards = listCards
numCards = 52
nC = 0
suitCard = listCards[nC][0]
rankCard = listCards[nC][1:]
withCard = 75
hightCard = 108

class Card(object):
    def __init__(self, suit, rank, x, y):
        self.suit = suit
        self.rank = rank
        self.x = x
        self.y = y
        self.image = pygame.image.load('images/cards/'+str(self.suit)+str(self.rank)+'.png')
        self.rotate_image = pygame.transform.rotate(self.image, 90)

# Mov Cards
xCard = int(weightWin/6)
yCard = int(hightWin/5)
wrongCard = False
colorOption = False

def chooseCard():
    global wrongCard, colorOption, xCard, yCard, suitCard, rankCard, nC

    suitCard = listCards[nC][0]
    rankCard = listCards[nC][1:]

    if (xCard + withCard/2) >= (5*weightWin/6):
        xCard = int(weightWin/6)
        yCard += int(hightCard + 20)
    else:
        xCard += int(withCard/2)

    if colorOption == True:
        chosenCard = Card(suitCard, rankCard, xCard, yCard + 16)
        win.blit(chosenCard.rotate_image, (chosenCard.x, chosenCard.y))
    else:
        chosenCard = Card(suitCard, rankCard, xCard, yCard)
        win.blit (chosenCard.image, (chosenCard.x,chosenCard.y))

    pygame.display.update()
    if wrongCard == True:
        backCard()

    nC += 1

def backCard():
    global colorOption, xCard, yCard, wrongCard

    pygame.time.delay(750)
    if colorOption == True:
        win.blit(rotate_back, (xCard, yCard + 16))
        xCard += 16
        colorOption = False
    else:
        win.blit(back, (xCard, yCard))
    wrongCard = False

def choosOption():
    global suitCard, rankCard, lastSuit, lastRank, wrongCard, nC, listCards, colorOption
    xMouse, yMouse = pygame.mouse.get_pos()

    # HIGHER BUTTON
    if xMouse >= weightWin/5 and xMouse <= 128 + weightWin/5 and yMouse >= 20 and yMouse <= 148:
        if int(listCards[nC - 1][1:]) <= int(listCards[nC][1:]):
            print ( listCards[nC][1:] + ' SI es MAYOR que ' + listCards[nC - 1][1:])
            chooseCard()
        else:
            text = 'No es mayor, debes tomar'
            textOnScreen = message.render(text, True, (0, 0, 0), (255, 255, 255))
            win.blit(textOnScreen, (0,50))
            print ( listCards[nC][1:] + ' NO es MAYOR que ' + listCards[nC - 1][1:])
            wrongCard = True
            chooseCard()

    # LOWER BUTTON
    if xMouse >= 2*weightWin/5 and xMouse <= 128 + 2*weightWin/5 and yMouse >= 20 and yMouse <= 148:
        if int(listCards[nC - 1][1:]) >= int(listCards[nC][1:]):
            print ( listCards[nC][1:] + ' SI es MENOR que ' + listCards[nC - 1][1:])
            chooseCard()
        else:
            text = 'No es menor, debes tomar'
            textOnScreen = message.render(text, True, (0, 0, 0), (255, 255, 255))
            win.blit(textOnScreen, (0,50))
            print ( listCards[nC][1:] + ' NO es MENOR que ' + listCards[nC - 1][1:])
            wrongCard = True
            chooseCard()

    # RED BUTTON
    if xMouse >= 3*weightWin/5 and xMouse <= 128 + 3*weightWin/5 and yMouse >= 20 and yMouse <= 148:
        if listCards[nC][0] == 'd' or listCards[nC][0] == 'h':
            print(listCards[nC][1:] + ' SI es ROJO')
            colorOption = True
            chooseCard()
        else:
            text = 'No es roja, debes tomar'
            textOnScreen = message.render(text, True, (0, 0, 0), (255, 255, 255))
            win.blit(textOnScreen, (0,50))
            print(listCards[nC][1:] + ' NO es ROJO')
            wrongCard = True
            colorOption = True
            chooseCard()

    # BLACK BUTTON
    if xMouse >= 4*weightWin/5 and xMouse <= 128 + 4*weightWin/5 and yMouse >= 20 and yMouse <= 148:
        if listCards[nC][0] == 's' or listCards[nC][0] == 'c':
            print(listCards[nC][1:] + ' SI es NEGRO')
            colorOption = True
            chooseCard()
        else:
            text = 'No es negra, debes tomar'
            textOnScreen = message.render(text, True, (0, 0, 0), (255, 255, 255))
            win.blit(textOnScreen, (0,50))
            print(listCards[nC][1:] + ' NO es NEGRO')
            wrongCard = True
            colorOption = True
            chooseCard()


run = True
play = False
win.blit(bg, (0, 0))

while run:
    pygame.time.delay(100)

    if not(play):
        win.blit (beer, (weightWin/2 - 125, 50))
        win.blit (startButton, (weightWin/2 - 250, hightWin/2))
        text = 'PLAY'
        textOnScreen = title.render(text, True, (0, 0, 0))
        win.blit(textOnScreen, (weightWin/2 - 150, hightWin/2 + 25))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                xMouse, yMouse = pygame.mouse.get_pos()
                if xMouse >= weightWin/2 - 250 and xMouse <= weightWin/2 + 250 and yMouse >= hightWin/2 and yMouse <= hightWin/2 + 206:
                    win.blit(bg, (0, 0))
                    win.blit(back, (20, hightCard * 6))
                    chosenCard = Card(suitCard, rankCard, xCard, yCard)
                    win.blit(chosenCard.image, (chosenCard.x, chosenCard.y))
                    nC += 1
                    win.blit(higher, (int(weightWin / 5), 20))
                    win.blit(lower, (int(2 * weightWin / 5), 20))
                    win.blit(redButton, (int(3 * weightWin / 5), 20))
                    win.blit(blackButton, (int(4 * weightWin / 5), 20))
                    play = True
        pygame.display.update()
    else:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                choosOption()

        pygame.display.update()

pygame.quit()

print ('Este fue el orden del juego: ')
print (copyListCards)
