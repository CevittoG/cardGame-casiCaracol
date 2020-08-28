import random
import pygame
from pygame.locals import *
import os

# Initiate PyGame
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
info = pygame.display.Info()

# Display
weightWin = info.current_w
hightWin = info.current_h - 20
text = ''
win = pygame.display.set_mode((weightWin, hightWin), RESIZABLE)  # center: 625, 417
pygame.display.set_caption("casiCaracol")
icon = pygame.image.load('images/beer.png')
pygame.display.set_icon(icon)
message = pygame.font.Font(None, 20)
title = pygame.font.SysFont('Arial', 130)
typing = pygame.font.Font(None, 100)

# Images
bg = pygame.image.load('images/background.jpg')
bg = pygame.transform.scale(bg, (weightWin, hightWin))
bgDark = pygame.image.load('images/background-dark.jpg')
bgDark = pygame.transform.scale(bgDark, (weightWin, hightWin))
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
nameButton = pygame.image.load('images/name-button.png')
nameButton = pygame.transform.scale(nameButton, (225, 157))
instructionsButton = pygame.image.load('images/instructions-button.png')
instructionsButton = pygame.transform.scale(instructionsButton, (225, 157))
beer = pygame.image.load('images/big-beer.png')
beer = pygame.transform.scale(beer, (250, 250))
cork = pygame.image.load('images/cork.png')
cork = pygame.transform.rotate(cork, 180)
corkMessage = pygame.transform.rotate(cork, -90)
exName = pygame.image.load('images/delete-name.png')
exName = pygame.transform.scale(exName, (25, 25))
nextButton = pygame.image.load('images/next-button.png')
nextButton = pygame.transform.scale(nextButton, (115, 115))

# -------------------- VARIABLES --------------------
# Cards
listCards = ['c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'c10', 'c11', 'c12', 'c13',
             'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9', 'd10', 'd11', 'd12', 'd13',
             'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8', 'h9', 'h10', 'h11', 'h12', 'h13',
             's1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's10', 's11', 's12', 's13',

             'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'c10', 'c11', 'c12', 'c13',
             'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9', 'd10', 'd11', 'd12', 'd13',
             'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8', 'h9', 'h10', 'h11', 'h12', 'h13',
             's1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's10', 's11', 's12', 's13']
random.shuffle(listCards)
numCards = len(listCards)
nC = 0
suitCard = listCards[nC][0]
rankCard = listCards[nC][1:]
xCard = int(weightWin / 6)
yCard = int(hightWin / 5)
weightCard = 75
hightCard = 108
# Player
playersList = []
numPlayer = 0
drinks = 0
currentDrinks = 0
# Game
run = True
play = False
typingNames = False
typingData = ['', 0, 30]
wrongCard = False
colorOption = False


class Card(object):
    def __init__(self, suit, rank, x, y):
        self.suit = suit
        self.rank = rank
        self.x = x
        self.y = y
        self.image = pygame.image.load('images/cards/' + str(self.suit) + str(self.rank) + '.png')
        self.rotate_image = pygame.transform.rotate(self.image, 90)


class Player(object):
    def __init__(self, name, score, y):
        self.name = name
        self.score = score
        self.x = 20
        self.y = y
        self.currentDrinks = 0


def chooseCard():
    global wrongCard, colorOption, xCard, yCard, suitCard, rankCard, nC, numCards

    suitCard = listCards[nC][0]
    rankCard = listCards[nC][1:]

    if (xCard + weightCard / 2) >= (5 * weightWin / 6):
        xCard = int(weightWin / 6)
        yCard += int(hightCard + 10)
    else:
        xCard += int(weightCard / 2)

    if colorOption:
        chosenCard = Card(suitCard, rankCard, xCard, yCard + 16)
        win.blit(chosenCard.rotate_image, (chosenCard.x, chosenCard.y))
    else:
        chosenCard = Card(suitCard, rankCard, xCard, yCard)
        win.blit(chosenCard.image, (chosenCard.x, chosenCard.y))

    pygame.display.update()
    if wrongCard:
        backCard()

    nC += 1
    numCards -= 1


def backCard():
    global colorOption, xCard, yCard, wrongCard

    pygame.time.delay(750)
    if colorOption:
        win.blit(rotate_back, (xCard, yCard + 16))
        xCard += 16
        colorOption = False
    else:
        win.blit(back, (xCard, yCard))
    wrongCard = False


def choosOption():
    global suitCard, rankCard, wrongCard, nC, listCards, colorOption, numPlayer, text, drinks
    xMouse, yMouse = pygame.mouse.get_pos()

    # HIGHER BUTTON
    if weightWin / 5 <= xMouse <= 128 + weightWin / 5 and 20 <= yMouse <= 148:
        if int(listCards[nC - 1][1:]) <= int(listCards[nC][1:]):
            wrongCard = False
            colorOption = False
            chooseCard()
            drinks += 1
            text = 'Drinks: ' + str(drinks)
            playersList[numPlayer].currentDrinks += 1
        else:
            wrongCard = True
            colorOption = False
            chooseCard()
            drinks += 1
            text = playersList[numPlayer].name + ' drinks ' + str(drinks)
            playersList[numPlayer].score += drinks
            drinks = 0
            playersList[numPlayer].currentDrinks = 0

    # LOWER BUTTON
    if 2 * weightWin / 5 <= xMouse <= 128 + 2 * weightWin / 5 and 20 <= yMouse <= 148:
        if int(listCards[nC - 1][1:]) >= int(listCards[nC][1:]):
            wrongCard = False
            colorOption = False
            chooseCard()
            drinks += 1
            text = 'Drinks: ' + str(drinks)
            playersList[numPlayer].currentDrinks += 1
        else:
            wrongCard = True
            colorOption = False
            chooseCard()
            drinks += 1
            text = playersList[numPlayer].name + ' drinks ' + str(drinks)
            playersList[numPlayer].score += drinks
            drinks = 0
            playersList[numPlayer].currentDrinks = 0

    # RED BUTTON
    if 3 * weightWin / 5 <= xMouse <= 128 + 3 * weightWin / 5 and 20 <= yMouse <= 148:
        if listCards[nC][0] == 'd' or listCards[nC][0] == 'h':
            colorOption = True
            chooseCard()
            drinks += 2
            text = 'Drinks: ' + str(drinks)
            playersList[numPlayer].currentDrinks += 1
        else:
            wrongCard = True
            colorOption = True
            chooseCard()
            drinks += 2
            text = playersList[numPlayer].name + ' drinks ' + str(drinks)
            playersList[numPlayer].score += drinks
            drinks = 0
            playersList[numPlayer].currentDrinks = 0

    # BLACK BUTTON
    if 4 * weightWin / 5 <= xMouse <= 128 + 4 * weightWin / 5 and 20 <= yMouse <= 148:
        if listCards[nC][0] == 's' or listCards[nC][0] == 'c':
            colorOption = True
            chooseCard()
            drinks += 2
            text = 'Drinks: ' + str(drinks)
            playersList[numPlayer].currentDrinks += 1
        else:
            wrongCard = True
            colorOption = True
            chooseCard()
            drinks += 2
            text = playersList[numPlayer].name + ' drinks ' + str(drinks)
            playersList[numPlayer].score += drinks
            drinks = 0
            playersList[numPlayer].currentDrinks = 0

    # NEXT BUTTON
    if 20 <= xMouse <= 135 and 450 <= yMouse <= 565:
        if playersList[numPlayer].currentDrinks >= 2:
            playersList[numPlayer].currentDrinks = 0
            if numPlayer + 1 > len(playersList) - 1:
                numPlayer = 0
            else:
                numPlayer += 1
        else:
            text = "You can't pass yet"

    # todo MAIN MENU
    #if penepene:
    #    restart()

def typeName():
    global typingNames, typingData, playersList
    while typingNames:
        if len(playersList) < 13:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.unicode.isalpha() and len(typingData[0]) < 9:
                        typingData[0] += event.unicode
                    elif event.key == K_BACKSPACE:
                        typingData[0] = typingData[0][:-1]
                    elif event.key == K_RETURN:
                        p = Player(typingData[0], typingData[1], typingData[2])
                        playersList.append(p)
                        typingData[0] = ''
                        typingData[1] = 0
                        typingData[2] += 30
                        typingNames = False
                elif event.type == pygame.QUIT:
                    return
        else:
            typingData[0] = 'You can´t add more players'
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        typingNames = False
        win.blit(bgDark, (0, 0))
        typing = pygame.font.Font(None, 100)
        block = typing.render(typingData[0], True, (255, 255, 255))
        rect = block.get_rect()
        rect.center = win.get_rect().center
        win.blit(block, rect)
        pygame.display.flip()


def showInstructions():
    # todo escribir las instrucciones con imagenes para que sea autoexplicativo
    return


def restart():
    global listCards, numCards, nC, suitCard, rankCard, xCard, yCard, weightCard, hightCard
    global playersList, numPlayer, drinks, currentDrinks
    global run, play, typingNames, typingData, wrongCard, colorOption
    # Cards
    listCards = ['c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'c10', 'c11', 'c12', 'c13',
                 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9', 'd10', 'd11', 'd12', 'd13',
                 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8', 'h9', 'h10', 'h11', 'h12', 'h13',
                 's1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's10', 's11', 's12', 's13',

                 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'c10', 'c11', 'c12', 'c13',
                 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9', 'd10', 'd11', 'd12', 'd13',
                 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8', 'h9', 'h10', 'h11', 'h12', 'h13',
                 's1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's10', 's11', 's12', 's13']
    random.shuffle(listCards)
    numCards = len(listCards)
    nC = 0
    suitCard = listCards[nC][0]
    rankCard = listCards[nC][1:]
    xCard = int(weightWin / 6)
    yCard = int(hightWin / 5)
    weightCard = 75
    hightCard = 108
    # Player
    playersList = []
    numPlayer = 0
    drinks = 0
    currentDrinks = 0
    # Game
    run = True
    play = False
    typingNames = False
    typingData = ['', 0, 30]
    wrongCard = False
    colorOption = False
    win.blit(bg, (0, 0))


while run:
    weightWin = info.current_w
    hightWin = info.current_h - 150
    pygame.time.delay(100)

    if not play:
        win.blit(bg, (0, 0))
        win.blit(beer, (int(weightWin / 2) - 125, 50))
        win.blit(startButton, (int(weightWin / 2) - 250, int(hightWin / 2)))
        win.blit(nameButton, (int(weightWin / 2) - 250, int(hightWin / 2) + 231))
        win.blit(instructionsButton, (int(weightWin / 2) + 25, int(hightWin / 2) + 231))
        title = pygame.font.SysFont('Arial', 130)
        playOnScreen = title.render('PLAY', True, (0, 0, 0))
        win.blit(playOnScreen, (int(weightWin / 2) - 150, int(hightWin / 2) + 25))
        title = pygame.font.SysFont('Arial', 30)
        namesOnScreen = title.render('Add Players', True, (255, 255, 255))
        win.blit(namesOnScreen, (int(weightWin / 2) - 225, int(hightWin / 2) + 285))
        instructionsOnScreen = title.render('Instruccions', True, (255, 255, 255))
        win.blit(instructionsOnScreen, (int(weightWin / 2) + 55, int(hightWin / 2) + 285))

        win.blit(cork, (0, 0))
        title = pygame.font.SysFont('Arial', 10)
        playersOnScreen = title.render('Max 13 players', True, (0, 0, 0))
        win.blit(playersOnScreen, (50, 5))
        message = pygame.font.Font(None, 30)
        for i in range(len(playersList)):
            playerInfo = playersList[i].name + ': ' + str(playersList[i].score)
            playersOnScreen = message.render(playerInfo, True, (0, 0, 0))
            win.blit(playersOnScreen, (20, playersList[i].y))
            win.blit(exName, (180, playersList[i].y))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                xMouse, yMouse = pygame.mouse.get_pos()
                if weightWin / 2 - 250 <= xMouse <= weightWin / 2 + 250 and hightWin / 2 <= yMouse <= hightWin / 2 + 206 and len(
                        playersList) >= 2:
                    win.blit(bg, (0, 0))
                    win.blit(back, (20, hightWin - 50))
                    chosenCard = Card(suitCard, rankCard, xCard, yCard)
                    win.blit(chosenCard.image, (chosenCard.x, chosenCard.y))
                    nC += 1
                    numCards -= 1
                    win.blit(higher, (int(weightWin / 5), 20))
                    win.blit(lower, (int(2 * weightWin / 5), 20))
                    win.blit(redButton, (int(3 * weightWin / 5), 20))
                    win.blit(blackButton, (int(4 * weightWin / 5), 20))
                    win.blit(nextButton, (20, 450))
                    play = True
                elif weightWin / 2 - 250 <= xMouse <= weightWin / 2 - 25 and hightWin / 2 + 231 <= yMouse <= hightWin / 2 + 388:
                    typingNames = True
                    typeName()
                elif weightWin / 2 + 25 <= xMouse <= weightWin / 2 + 250 and hightWin / 2 + 231 <= yMouse <= hightWin / 2 + 388:
                    showInstructions()
                elif 180 <= xMouse <= 205:
                    register = 0
                    for p in range(len(playersList)):
                        if playersList[p].y + 25 >= yMouse >= playersList[p].y:
                            register = p
                    playersList.pop(register)
                    for r in range(register, len(playersList)):
                        playersList[r].y -= 30
                    typingData[2] -= 30

        pygame.display.update()
    else:

        if numCards == 1:
            pygame.time.delay(750)
            showTimer = False
            win.blit(corkMessage, (105 + int(3 * weightWin / 5), int(hightWin) + 10))
            text = 'Press ENTER to start timer'
            message = pygame.font.Font(None, 40)
            textOnScreen = message.render(text, True, (0, 0, 0))
            rectText = textOnScreen.get_rect()
            rectText.center = (325 + int(3 * weightWin / 5), int(hightWin) + 55)
            win.blit(textOnScreen, (rectText.x, rectText.y))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        showTimer = True

            seconds = 59
            minutes = 4
            timer = '0' + str(minutes) + ':' + str(seconds)
            while showTimer:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        showTimer = False
                        run = False
                    elif event.type == MOUSEBUTTONDOWN and minutes >= 0:
                        minutes = -1
                    elif event.type == KEYDOWN:
                        if event.key == K_RETURN and minutes >= 0:
                            minutes = -1
                    elif event.type == MOUSEBUTTONDOWN and minutes < 0:
                        showTimer = False
                        restart()
                if seconds < 1:
                    seconds = 59
                    minutes -= 1
                    timer = '0' + str(minutes) + ':' + str(seconds)
                elif seconds < 10:
                    timer = '0' + str(minutes) + ':0' + str(seconds)
                else:
                    timer = '0' + str(minutes) + ':' + str(seconds)


                if minutes < 0:
                    timer = "Time's out!"
                    win.blit(bgDark, (0, 0))
                    typing = pygame.font.Font(None, 200)
                    block = typing.render(timer, True, (255, 255, 255))
                    rect = block.get_rect()
                    rect.center = win.get_rect().center
                    rect.y = int(win.get_rect().h / 2) - 100
                    lastCard = pygame.image.load('images/cards/' + listCards[len(listCards) - 1] + '.png')
                    lastCard = pygame.transform.scale(lastCard, (int(weightCard * 1.5), int(hightCard * 1.5)))
                    win.blit(lastCard, (int(win.get_rect().w / 2) - weightCard, int(win.get_rect().h / 2) + 50))
                    win.blit(block, rect)
                    pygame.display.flip()
                else:
                    win.blit(corkMessage, (105 + int(3 * weightWin / 5), int(hightWin) + 10))
                    message = pygame.font.Font(None, 70)
                    textOnScreen = message.render(timer, True, (0, 0, 0))
                    rectText = textOnScreen.get_rect()
                    rectText.center = (325 + int(3 * weightWin / 5), int(hightWin) + 55)
                    win.blit(textOnScreen, (rectText.x, rectText.y))
                    pygame.display.flip()
                    pygame.time.delay(999)
                    seconds -= 1
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    choosOption()

            win.blit(back, (20, hightWin - 50))
            typing = pygame.font.Font(None, 55)
            numCardsOnScreen = typing.render(str(numCards), True, (0, 0, 0))
            rectNumCard = numCardsOnScreen.get_rect()
            rectNumCard.center = (int(57 - rectNumCard.w / 2), int(hightWin + 4 - rectNumCard.h / 2))
            win.blit(numCardsOnScreen, rectNumCard.center)

            win.blit(cork, (0, 0))
            for i in range(len(playersList)):
                playerInfo = playersList[i].name + ': ' + str(playersList[i].score)
                if i == numPlayer:
                    message = pygame.font.Font(None, 35)
                    playersOnScreen = message.render(playerInfo, True, (0, 0, 0))
                else:
                    message = pygame.font.Font(None, 30)
                    playersOnScreen = message.render(playerInfo, True, (255, 255, 255))
                win.blit(playersOnScreen, (20, playersList[i].y))

            win.blit(corkMessage, (105 + int(3 * weightWin / 5), int(hightWin) + 10))
            message = pygame.font.Font(None, 60)
            textOnScreen = message.render(text, True, (0, 0, 0))
            rectText = textOnScreen.get_rect()
            rectText.center = (325 + int(3 * weightWin / 5), int(hightWin) + 55)
            win.blit(textOnScreen, (rectText.x, rectText.y))

        pygame.display.update()

pygame.quit()

print('Este fue el orden del juego: ')
print(listCards)
