#Game of Matches
#
#By Uku Pattak and Janar Ojalaid

import pygame, sys
from pygame.locals import *
from random import *
from tkinter import *
from tkinter import ttk

#Pygame init must be after import
pygame.init()

#Player names from last game
playerNamesHistory = []

#GameBoard design
blackMatch = pygame.image.load('images/black.png')
blueMatch = pygame.image.load('images/blue.png')
redMatch = pygame.image.load('images/red.png')
background = pygame.image.load('images/background.png')
buttonImage = pygame.image.load('images/ok.png')
gameOverImage = pygame.image.load('images/gameover.png')
icon = pygame.image.load('images/icon.png')
buttonFontObject = pygame.font.SysFont('trebuchetms', 30)
playerFontObject = pygame.font.SysFont('trebuchetms', 14)
scoreFontObject = pygame.font.SysFont('trebuchetms', 24)

#Main function, what runs all the other functions
def main():
    getData()
    
    if confirmation == True:
        prepareBoards()
    
        mainGame()

'''### ALL THE MAIN FUNCTIONS ###'''

#Function, what gets all the needed data from players
#
#Variables changed: numberOfTaking, playerNames, computerLevel, scoreList, raam, matchesCanTake, confirmation
def getData():
    global numberOfTaking, playerNames, computerLevel, scoreList, raam, matchesCanTake, confirmation
    
    confirmation = False
    playerNames = []
    
    raam = Tk()
    raam.title("Game of Matches")
        
    silt=ttk.Label(raam, text="PC")
    silt.grid(column=3, row=0, padx=10, pady=5, sticky=(N,E))

    silt = ttk.Label(raam, text="1. player")
    silt.grid(column=0, row=1, padx=5, pady=5, sticky=(N, W))
    esimene=StringVar()
    playerName=ttk.Entry(raam, textvariable=esimene)
    playerName.grid(column=1, row=1, padx=5, pady=5, sticky=(N, W, E))
    if len(playerNamesHistory) > 0:
        playerName.insert(0, playerNamesHistory[0])
    
    silt = ttk.Label(raam, text="2. player")
    silt.grid(column=0, row=2, padx=5, pady=5, sticky=(N, W))
    teine=StringVar()
    playerName=ttk.Entry(raam, textvariable=teine)
    playerName.grid(column=1, row=2, padx=5, pady=5, sticky=(N, W, E))
    p2=StringVar()
    if len(playerNamesHistory) > 1:
        playerName.insert(0, playerNamesHistory[1])
        
    check=ttk.Checkbutton(raam, variable=p2)
    check.grid(column=3, row=2, padx=5, pady=5, sticky= (N,E))
    
    silt = ttk.Label(raam, text="3. player")
    silt.grid(column=0, row=3, padx=5, pady=5, sticky=(N, W))
    kolmas=StringVar()
    playerName=ttk.Entry(raam, textvariable=kolmas)
    playerName.grid(column=1, row=3, padx=5, pady=5, sticky=(N, W, E))
    p3=StringVar()
    if len(playerNamesHistory) > 2:
        playerName.insert(0, playerNamesHistory[2])
        
    check=ttk.Checkbutton(raam, variable=p3)
    check.grid(column=3, row=3, padx=5, pady=5, sticky= (N,E))

    silt = ttk.Label(raam, text="4. player")
    silt.grid(column=0, row=4, padx=5, pady=5, sticky=(N, W))
    neljas=StringVar()
    playerName=ttk.Entry(raam, textvariable=neljas)
    playerName.grid(column=1, row=4, padx=5, pady=5, sticky=(N, W, E))
    p4=StringVar()
    if len(playerNamesHistory) > 3:
        playerName.insert(0, playerNamesHistory[3])
          
    check=ttk.Checkbutton(raam, variable=p4)
    check.grid(column=3, row=4, padx=5, pady=5, sticky= (N,E))

    silt=ttk.Label(raam, text="Number of taking matches")
    silt.grid(column=0, row=5, padx=5, pady=5, sticky=(N,W))
    valuetikk=IntVar()
    numberOfTaking=ttk.Combobox(raam, textvariable=valuetikk, state="readonly")
    numberOfTaking.grid(column=1, row=5, padx=5, pady=5, sticky=(N,W,E))
    numberOfTaking["values"]=(2, 3, 4, 5)
    numberOfTaking.current(3)

    silt = ttk.Label(raam, text = 'Player can take 1 to n match')
    silt.grid(column = 0, row = 6, padx = 5, pady = 5, sticky = (N,W))
    p5 = StringVar()
    check = ttk.Checkbutton(raam, variable = p5)
    check.grid(column = 1, row = 6, padx = 5, pady = 5, sticky = (N, W))

    silt = ttk.Label(raam, text="PC level")
    silt.grid(column=0, row=7, padx=5, pady=5, sticky=(N,W))
    valuelevel = IntVar()
    level = ttk.Combobox(raam, textvariable=valuelevel, state="readonly")
    level.grid(column=1, row=7, padx=5, pady=5, sticky=(N,W))
    level["values"] = (3, 2, 1)
    level.current(1)

    nupp=ttk.Button(raam, text="Next", command = confirmForward)
    nupp.grid(column=1, row=8, padx=5, pady=5, sticky=(N,S,W,E))

    #enter klahv viib edasi
    raam.bind("<Return>", confirmReturn)
    #escape klahv sulgeb
    raam.bind("<Escape>", confirmEscape)
    
    raam.columnconfigure(1, weight=1)
    raam.rowconfigure(1, weight=1)
    
    raam.mainloop()
    
    pc = [0, p2.get(), p3.get(), p4.get()]

    players = [esimene.get(), teine.get(), kolmas.get(), neljas.get()]
    
    organisePlayerNames(pc, players)
    
    #Game data
    numberOfTaking = valuetikk.get()
    computerLevel = valuelevel.get() * 2
    scoreList = [0, 0, 0, 0]
    shuffle(playerNames)
    
    if p5.get()=="1":
        matchesCanTake = True
    else:
        matchesCanTake = False

#Function, what will put random number of matches to each board
#
#Variables changed: matchesOnBoards
def prepareBoards():
    global matchesOnBoards
    
    matchesOnBoards = []
    maxMatches = 6 * numberOfTaking
    
    for i in range(4):
        randomMatches = randint(numberOfTaking + 1, maxMatches)
        
        matchesOnBoards.append(randomMatches)
    
#Function, where the main game is written
#
#Variables changed: fpsClock, windowId, matchesTakenCount, mouseX, mouseY, activeMatchesIds, computerPlayer, currentPlayerIndex, computerPlayerPassive
def mainGame():
    global fpsClock, windowId, matchesTakenCount, mouseX, mouseY, activeMatchesIds, computerPlayer, currentPlayerIndex, computerPlayerPassive
    
    fpsClock = pygame.time.Clock()
    windowId = pygame.display.set_mode((800, 575))
    pygame.display.set_caption('Tikumäng 1.0')
    pygame.display.set_icon(icon)

    activeMatchesIds = []
    matchesTakenCount = numberOfTaking
    currentPlayerIndex = 0
    
    computerPlayer = controlComputerPlayer()
    computerPlayerPassive = False

    drawGameBoard(None)  

    #Main game loop
    while True:
        for event in pygame.event.get():
            #If user wants to quit game
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE) or confirmation == False:
                pygame.quit()
                sys.exit()
            #The game will start again if game is over
            elif getTotalMatchesOnBoards(True) == 0:
                pygame.time.delay(100)
                main()
            #If player is computer
            elif computerPlayer == True:
                mouseX, mouseY = (90, 40)
                
                computer(matchesOnBoards)
                matchesTakenCount = 0
                analyseAndCarryOutEvent()

                computerPlayer = False
                computerPlayerPassive = True
            #Starts carrying out the event if user clicked on the screen
            elif event.type == MOUSEBUTTONUP:
                mouseX, mouseY = event.pos
                analyseAndCarryOutEvent()

            pygame.display.update()

#Function analyses given events with various information
#
#Variables changed: matchesTakenCount, activeMatchesIds, computerPlayerPassive, computerPlayer, matchId, numberOfTaking
def analyseAndCarryOutEvent():
    global matchId, matchesTakenCount, numberOfTaking, computerPlayer, computerPlayerPassive

    matchId = getMatchIdByPos()
    unActiveMatchId = None

    #If user clicked on match
    if matchId != None and controlMatchUnlocked() == True:
        if matchId not in activeMatchesIds and matchesTakenCount > 0:
            activeMatchesIds.append(matchId)

            matchesTakenCount -= 1
        elif matchId in activeMatchesIds:
            activeMatchesIds.pop(activeMatchesIds.index(matchId))
            unActiveMatchId = matchId

            matchesTakenCount += 1           
    #If user clicked on OK button
    elif controlSubmitButtonClick() == True:
        computerPlayerPassive = False
        
        modifyScoreList()
        deleteSelectedMatches()
        modifyCurrentPlayer()

        computerPlayer = controlComputerPlayer()
        totalMatches = getTotalMatchesOnBoards(True)
        
        if totalMatches < numberOfTaking:
            numberOfTaking = totalMatches
            
        matchesTakenCount = numberOfTaking

    #Draws updated gameboard
    drawGameBoard(unActiveMatchId)

'''### DRAWING FUNCTIONS ###'''

#Function draws game board to PyGame window
#
#Variables changed: allMatchesPositions, allMatchesIds
def drawGameBoard(unActiveMatchId):
    global allMatchesPositions, allMatchesIds
    
    #Draws background
    windowId.blit(background, (0, 0))
    
    #Draws players scores/names and OK button
    drawPlayersCorner()
    
    #Draws matches to board
    allMatchesPositions = []
    allMatchesIds = []

    screenMarginX = 90
    screenMarginY = 40

    currentMarginX = screenMarginX
    currentMarginY = screenMarginY
    
    currentBoardMarginX = screenMarginX
    currentBoardMarginY = screenMarginY

    activeMatchesIdsLen = len(activeMatchesIds)

    for index, matches in enumerate(matchesOnBoards):
        matchesPositions = []
        matchesIds = []

        for match in range(1, matches + 1):
            matchId = [index, match - 1]
            activeMatchBingo = False

            #Append match info to lists
            matchesPositions.append([currentMarginX, currentMarginY])
            matchesIds.append(matchId)

            #Draw unactive match
            if unActiveMatchId == matchId:
                windowId.blit(blueMatch, (currentMarginX, currentMarginY))
            else:
                if activeMatchesIdsLen != 0:
                    for activeMatchId in activeMatchesIds:
                        if activeMatchId == matchId:
                            #Draw active match
                            windowId.blit(redMatch, (currentMarginX, currentMarginY))
                                                    
                            activeMatchBingo = True
                            activeMatchesIdsLen -= 1
                            break
                #If current match is activated or not
                if activeMatchBingo == False: 
                    if (matches - numberOfTaking) < match:
                        windowId.blit(blueMatch, (currentMarginX, currentMarginY))
                    else:
                        windowId.blit(blackMatch, (currentMarginX, currentMarginY))
            #Move next match position
            if match % 10 == 0 and match != 0:
                currentMarginX = currentBoardMarginX
                currentMarginY += 70
            elif match % 5 == 0 and match != 0:
                currentMarginX += 50
            else:
                currentMarginX += 27
                
        #Move next matches positions to new board
        if (index + 1) % 2 == 0 and index != 0:
            currentBoardMarginX = screenMarginX
            currentBoardMarginY += screenMarginY + 200

        else:
            currentBoardMarginX += 326

        currentMarginX = currentBoardMarginX
        currentMarginY = currentBoardMarginY

        allMatchesPositions.append(matchesPositions)
        allMatchesIds.append(matchesIds)

#Draws score list, players names and OK button
#
#Varibales changed: submitButtonPosition
def drawPlayersCorner():
    global submitButtonPosition

    submitButtonPosition = (370, 530)
    firstPlayerNamePosition = [40, 550]
    firstScorePosition = [60, 520]

    #Draw numberOfTaking value or OK button to bottom of the screen
    if getTotalMatchesOnBoards(True) == 0:
        windowId.blit(gameOverImage, (310, 530))
    elif matchesCanTake == True:
        if matchesTakenCount == numberOfTaking:
            textSurfaceObject = buttonFontObject.render('...', True, (254, 15, 28))

            windowId.blit(textSurfaceObject, (375, 527))
        else:
            windowId.blit(buttonImage, submitButtonPosition)
    elif controlSubmitButtonUnlocked() == True:   
        windowId.blit(buttonImage, submitButtonPosition)
    else:
        textSurfaceObject = buttonFontObject.render(str(matchesTakenCount), True, (254, 15, 28))
        
        windowId.blit(textSurfaceObject, (383, 527))
        
    #Draw player names and scores
    for index, player in enumerate(playerNames):
        if currentPlayerIndex == index:
            nameObject = playerFontObject.render(player, True, (0, 174, 239))
            scoreObject = scoreFontObject.render(str(scoreList[index]), True, (0, 174, 239))
        else:
            nameObject = playerFontObject.render(player, True, (255, 255, 255))
            scoreObject = scoreFontObject.render(str(scoreList[index]), True, (255, 255, 255))

        windowId.blit(nameObject, (firstPlayerNamePosition[0], firstPlayerNamePosition[1]))
        windowId.blit(scoreObject, (firstScorePosition[0], firstScorePosition[1]))       

        if index == 1:
            firstPlayerNamePosition[0] += 300
            firstScorePosition[0] += 300
        else:
            firstPlayerNamePosition[0] += 170
            firstScorePosition[0] += 170

'''### COMPUTER ALGORITM ###'''

#Computer algoritm
#
#Variables changed: computerMove
def computer(matchesOnBoards):
    global computerMove
    
    matchesOnBoards, boardsIndexs = getSortedData(matchesOnBoards, [0, 1, 2, 3])
    matchesAllowedToTake = numberOfTaking
    
    boardsNotAllowedToChoose = []
    boardsCanNotChoose = []
    boardsCanChoose = [board for index, board in enumerate(boardsIndexs) if matchesOnBoards[index] != 0]
    
    computerMove = []

    for level in range(1, computerLevel + 1):
        nextStep = (numberOfTaking + 1) * level
        lastStep = (numberOfTaking + 1) * (level - 1)

        #Selects only those boards what are in the level rate and not 0
        boardsToChoose = [index for index, x in enumerate(matchesOnBoards) if x < nextStep and x > lastStep and x != 0]
        #Selects boards, where matches numbers are equal to 'dead' numbers etc
        boardsShouldNotChoose = [index for index, x in enumerate(matchesOnBoards) if x == nextStep or x == lastStep and x != 0]
        
        #Inserts those dead spot boards to forbidden-take list
        boardsCanNotChoose = list(set(boardsCanNotChoose + boardsShouldNotChoose))
        
        for boardIndex in boardsToChoose:
            #Calculates how many matches to take and what is the board real index
            matchesToTake = matchesOnBoards[boardIndex] - (numberOfTaking + 1) * (level - 1)
            realBoardIndex = boardsIndexs[boardIndex]

            #If computer is allowed to take those matches or it will exceed numberOfTaking
            if matchesToTake <= matchesAllowedToTake:
                computerMove.append([realBoardIndex, matchesToTake])
                matchesAllowedToTake -= matchesToTake

                #If comp. takes matches from that board consciously, then he cant to that again randomly
                if boardIndex not in boardsNotAllowedToChoose:
                    boardsNotAllowedToChoose.append(boardIndex)

        boardsNotAllowedToChoose += boardsCanNotChoose

        #Pops all not allowed boards from allowed list
        for boardIndex in boardsNotAllowedToChoose:
            realBoardIndex = boardsIndexs[boardIndex]
            
            if realBoardIndex in boardsCanChoose:
                boardsCanChoose.pop(boardsCanChoose.index(realBoardIndex))

        #If all the matches are taken, then comp. ends his loop
        if matchesAllowedToTake == 0:
            break

    #Comp. will make random select if there are some matches left to take
    if matchesCanTake == False and matchesAllowedToTake != 0 or matchesAllowedToTake == numberOfTaking:
        if not boardsCanChoose:
            if matchesCanTake == False:
                if not boardsCanNotChoose:
                    randomBoard = boardsIndexs[boardsNotAllowedToChoose[-1]]
                else:
                    randomBoard = boardsIndexs[boardsCanNotChoose[-1]]

                computerMove.append([randomBoard, matchesAllowedToTake])
            elif len(boardsCanNotChoose) == 1:
                randomBoard = boardsIndexs[boardsCanNotChoose[-1]]
                
                computerMove.append([randomBoard, matchesAllowedToTake])
            else:
                firstRandomBoard = boardsIndexs[boardsCanNotChoose[-1]]
                secondRandomBoard = boardsIndexs[boardsCanNotChoose[-2]]
                
                computerMove.append([firstRandomBoard, 1])
                computerMove.append([secondRandomBoard, 1])
        else:
            randomBoard = choice(boardsCanChoose)

            computerMove.append([randomBoard, matchesAllowedToTake])

    modifyComputerMove()

'''### PLAYER NAMES ORGANIZING ###'''
    
#Organise inserted player names, e.g title and str length etc
#
#Variables changed: playerNames, playerNamesHistory
def organisePlayerNames(pc, players):
    global playerNamesHistory
    names = open('names.txt').readlines()

    computerNames = []
    playerNamesHistory = []
    for name in names:
        computerNames.append(name.strip())

    for index, player in enumerate(players):
        if pc[index]=="1":
            if player:
                playerNamesHistory.append(player.title())
                playerNames.append(player.title() + ' (PC)')
                
            else:
                while True:
                    randName = choice(computerNames)
                    computerNames.pop(computerNames.index(randName))
                
                    if randName not in playerNames:
                        playerNamesHistory.append(randName)
                        playerNames.append(randName + ' (PC)')
                        break
        else: 
            if index == 0 and not player:
                playerNamesHistory.append('Player 1')
                playerNames.append('Player 1')
            elif player:
                playerNamesHistory.append(player.title())
                playerNames.append(player.title())

    if len(playerNames) == 1:
        randName = choice(computerNames)
        
        playerNamesHistory.append(randName)
        playerNames.append(randName + ' (PC)')
    else:
        modifyPlayerNames()

'''### MODIFY FUNCTIONS ###'''

#Makes computerMove list to activeMatchesIds list
#
#Variables changed: activeMatchesIds
def modifyComputerMove():
    for move in computerMove:
        for match in range(1, move[1] + 1):
            activeMatchesIds.append(allMatchesIds[move[0]][-match])

#Changes current player index and counts game rounds
#
#Variables changed: currentPlayerIndex
def modifyCurrentPlayer():
    global currentPlayerIndex
    
    if currentPlayerIndex < len(playerNames) - 1:
        currentPlayerIndex += 1
    else:
        currentPlayerIndex = 0
    
#Add 1 point to a player if he/she takes last match from board
#
#Variables changed: scoreList
def modifyScoreList():
    global scoreList

    for match in activeMatchesIds:
        if match[1] == 0:
            scoreList[currentPlayerIndex] += 1

#Modify player names so that they will fit to players corner
#
#Variables changed: playerNames
def modifyPlayerNames():
    for index, player in enumerate(playerNames):
        playerLength = len(player)
            
        if playerLength > 10:
            if player.find(' (PC)') != -1:
                sub = playerLength - 4
                player = player[:-sub] + '..' + '(PC)'
            else:
                sub = playerLength - 8
                player = player[:-sub] + '..'
        elif playerLength < 7:
            if player.find(' (PC)') != -1:
                add = 3 - playerLength
                player = add * ' ' + player
            else:
                add = 7 - playerLength
                player = add * ' ' + player

        playerNames[index] = player

'''### GET FUNCTIONS ###'''

#Function what returns match and board index if mouse is on the match
#
#Returns: matchId or None
def getMatchIdByPos():
    matchWidth = 12
    matchHeight = 59

    if computerPlayer == True:
        return [-1, -1]

    for index, matchesPositions in enumerate(allMatchesPositions):
        for key, matchPosition in enumerate(matchesPositions):
            if mouseX >= (matchPosition[0] - 3) and mouseX <= (matchPosition[0] + matchWidth + 3):
                if mouseY >= matchPosition[1] and mouseY <= (matchPosition[1] + matchHeight):
                    return allMatchesIds[index][key]

    return None

#Function counts how many matches are on the boards at the moment
#
#Returns: totalMatches
def getTotalMatchesOnBoards(afterSubmit):
    totalMatches = 0
    
    for matches in matchesOnBoards:
        totalMatches += matches

    if afterSubmit == False:
        totalMatches -= (numberOfTaking - matchesTakenCount)

    return totalMatches

#Sort two lists by one list values, [3, 4, 1] -> [1, 3, 4]
#
#Returns: matchesOnBoards, boardsIndexs
def getSortedData(matchesOnBoards, boardsIndexs):
    data = zip(matchesOnBoards, boardsIndexs)

    sortedData = sorted(data)

    matchesOnBoards = [element[0] for element in sortedData]
    boardsIndexs = [element[1] for element in sortedData]

    return matchesOnBoards, boardsIndexs

'''### DELETE FUNCTIONS ###'''

#Deletes all active matches that user have selected
#
#Variables changed: activeMatchesIds, matchesOnBoards, allMatchesPositions, allMatchesIds
def deleteSelectedMatches():
    global activeMatchesIds
    
    for activeMatchId in activeMatchesIds:
        boardIndex = activeMatchId[0]

        allMatchesPositions[boardIndex].pop()
        allMatchesIds[boardIndex].pop()
        
        matchesOnBoards[boardIndex] -= 1

    activeMatchesIds = []

'''### CONFIRM FUNCTIONS ###'''

#Tkinter continue function, gives permission to run other functions
#
#Variables changed: confirmation
def confirmForward():
    global confirmation
    
    raam.destroy()
    confirmation = True

#Tkinter continue function, gives permission to run other functions
#
#Variables changed: confirmation
def confirmReturn(x):
    global confirmation
    
    raam.destroy()
    confirmation = True

#Tkinter quit function
#
#Variables changed: confirmation
def confirmEscape(x):
    global confirmation
    
    raam.destroy()
    confirmation = False

'''### CONTROL FUNCTIONS ###'''

#Function controls if selected match is allowed to take from the board
#
#Returns: False or True
def controlMatchUnlocked():
    if matchesOnBoards[matchId[0]] - numberOfTaking <= matchId[1] and computerPlayerPassive == False:
        return True
    
    return False

#Controls if submit button can be active or not
#
#Returns: False or True
def controlSubmitButtonUnlocked():
    if matchesTakenCount == 0 or getTotalMatchesOnBoards(False) == 0 or matchesCanTake == True and matchesTakenCount < numberOfTaking:
        return True

    return False

#Controls if user clicked on active submit button
#
#Returns: False or True
def controlSubmitButtonClick():
    buttonWidth = 46
    buttonHeight = 32

    if controlSubmitButtonUnlocked() == True:
        if mouseX >= submitButtonPosition[0] and mouseX <= submitButtonPosition[0] + buttonWidth:
                if mouseY >= submitButtonPosition[1] and mouseY <= submitButtonPosition[1] + buttonHeight:
                    return True
                
    return False

#Controls if player is computer
#
#Returns: False or True
def controlComputerPlayer():
    if playerNames[currentPlayerIndex].find('(PC)') != -1:
        return True

    return False
    
main()
