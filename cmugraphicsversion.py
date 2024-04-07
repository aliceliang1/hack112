from cmu_graphics import *
import random

####################################################
# onAppStart: called only once when app is launched
####################################################

def onAppStart(app):
    app.width = 900
    app.height = 600
    app.stepsPerSecond = 10
    app.themes = ["Grocery"]
    app.themeIndex= 0
    app.currTheme = "Grocery"
    # photos
    app.scottyUrl = "https://www.cmu.edu/dining/news/2023/scottys-market-rendering_900x600-min.jpg"
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
    drawImage(app.scottyUrl, 0, 0)
    # drawRect(app.width/2 - 70, app.height/2 - 10, 140, 50, fill='white')
    for i in range(3):
        drawRect(app.width/2 - 100, 100*(i+2), 200, 80, fill='white', border='black')
    drawLabel('Checkout', app.width/2, 100*2 + 40, size=24)
    drawLabel('Order To-Go', app.width/2, 100*3+40, size=24)
    drawLabel('Small Talk', app.width/2, 100*4+40, size=24)
    # drawRect(app.width/2 - 70, app.height/2 )
    

def groceryHomeScreen_onKeyPress(app, key):
    onKeyPressHelper(app, key)


####################################################
# main function
####################################################

def main():
    runAppWithScreens(initialScreen='helpScreen')

main()

def main():
    runApp()

main()

cmu_graphics.run()