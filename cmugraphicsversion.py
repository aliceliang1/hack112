from cmu_graphics import *
import random

####################################################
# onAppStart: called only once when app is launched
####################################################

def onAppStart(app):
    app.width = 1000
    app.height = 600
    app.stepsPerSecond = 10
    app.themes = ["Grocery"]
    app.themeIndex= 0
    app.currTheme = "Grocery"
    # photos
    app.scottyUrl = "cmu://786056/30136545/Scotty's+Market.jpg"
    newGame(app)

def newGame(app):
    app.livesCount = 2
    app.winGame = False
    app.loseGame = False
    
####################################################
# Code used by multiple screens
####################################################

def onKeyPressHelper(app, key):
    if key == 'm': setActiveScreen('mapScreen')
    elif key == 'g': setActiveScreen('groceryHomeScreen')
    elif key == '?': setActiveScreen('helpScreen')

def drawScreenTitle(app, screenTitle):
    # drawLabel('BreakLingo', app.width/2, 20, size=20, bold=True)
    drawLabel(screenTitle, app.width/2, 50, size=16, bold=True)

####################################################
# helpScreen
####################################################

def helpScreen_redrawAll(app):
    drawRect(0, 0, app.width, app.height, fill='honeydew')
    drawScreenTitle(app, 'Help Screen')

def helpScreen_onKeyPress(app, key):
    onKeyPressHelper(app, key)

####################################################
# mapScreen
####################################################

def mapScreen_redrawAll(app):
    drawScreenTitle(app, 'Maps Screen')
    drawRect(0, 0, 200, 200, fill='blue')

def mapScreen_onKeyPress(app, key):
    onKeyPressHelper(app, key)

####################################################
# groceryHomeScreen
####################################################

def groceryHomeScreen_redrawAll(app):
    drawScreenTitle(app, 'Grocery Screen')
    drawImage(app.scottyUrl, 0, 0, 1000, 600)

    

def groceryHomeScreen_onKeyPress(app, key):
    onKeyPressHelper(app, key)


####################################################
# main function
####################################################

def main():
    runAppWithScreens(initialScreen='Help Screen')

main()

def main():
    runApp()

main()

cmu_graphics.run()