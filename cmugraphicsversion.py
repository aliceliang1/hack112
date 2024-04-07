from cmu_graphics import *
import random

####################################################
# onAppStart: called only once when app is launched
####################################################

def onAppStart(app):
    newGame(app)
    pass

def newGame(app):
    pass
    
####################################################
# Code used by multiple screens
####################################################

def onKeyPressHelper(app, key):
    # Since every screen does the same thing on key presses, we can
    # write the main logic here and just have them call this helper fn
    # You should add/edit some code here...
    if   key == 'd': setActiveScreen('setDimsScreen')
    elif key == 't': setActiveScreen('setThemeScreen')
    elif key == '?': setActiveScreen('helpScreen')
    elif key == 'p': setActiveScreen('playScreen')

def drawScreenTitle(app, screenTitle):
    drawLabel('SuperSet!', app.width/2, 20, size=20, bold=True)
    drawLabel(screenTitle, app.width/2, 50, size=16, bold=True)

####################################################
# helpScreen
####################################################

def helpScreen_redrawAll(app):
    drawRect(0, 0, app.width, app.height, fill='honeydew')
    # drawScreenTitle(app, 'Help Screen')

####################################################
# setDimsScreen
####################################################

def setDimsScreen_onScreenActivate(app):
    app.currDims = copy.copy(app.dims)
    print('''

********************************************
You just activated the setDims Screen!
You can put code here (in setDimsScreen_onScreenActivate)
to do something each time the user activates this screen.
********************************************
''')

def setDimsScreen_redrawAll(app):
    pass
    # drawScreenTitle(app, 'Set Dimensions Screen')


####################################################
# setThemeScreen
####################################################

def setThemeScreen_redrawAll(app):
    drawScreenTitle(app, 'Set Theme Screen')
    

def setThemeScreen_onKeyPress(app, key):
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