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
    # setActiveScreen('helpScreen')
    newGame(app)

def newGame(app):
    app.livesCount = 2
    app.winGame = False
    app.loseGame = False
    
####################################################
# Code used by multiple screens
####################################################

def onKeyPressHelper(app, key):
    # Since every screen does the same thing on key presses, we can
    # write the main logic here and just have them call this helper fn
    # You should add/edit some code here...
    if   key == 'm': setActiveScreen('setMapScreen')
    elif key == 'g': setActiveScreen('setGroceryHomeScreen')
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

####################################################
# setMapScreen
####################################################

def setMapScreen_onScreenActivate(app):
#     # insert a picture
    print('''

********************************************
You just activated the setDims Screen!
You can put code here (in setDimsScreen_onScreenActivate)
to do something each time the user activates this screen.
********************************************
''')

def setMapScreen_redrawAll(app):
    # instructions
    drawScreenTitle(app, 'Set Maps Screen')
    pass

def mapScreen_redrawAll(app):
    drawRect(0, 0, 200, 200, fill='blue')


####################################################
# setGroceryHomeScreen
####################################################

def setGroceryHomeScreen_redrawAll(app):
    drawScreenTitle(app, 'Set Grocery Screen')
    

def setGroceryHomeScreen_onKeyPress(app, key):
    pass

####################################################
# playScreen
####################################################

def playScreen_redrawAll(app):
    drawScreenTitle(app, 'Set Play Screen')


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