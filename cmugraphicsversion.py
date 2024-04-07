
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
    app.cashierUrl = "https://files.oaiusercontent.com/file-DZsSTpx4c7ABOdXIthZQ4m9M?se=2024-04-07T05%3A15%3A22Z&sp=r&sv=2021-08-06&sr=b&rscc=max-age%3D31536000%2C%20immutable&rscd=attachment%3B%20filename%3D68a7ddd3-0956-43f7-bbdb-5c38b0635b4d.webp&sig=iF4je0T4Z57i%2B4%2BI2K%2BFM0JBXImlzwuy94yqNOWoZWk%3D"
    newGame(app)

def newGame(app):
    app.livesCount = 2
    app.groceryHomeOneSelected = False
    app.groceryHomeTwoSelected = False
    app.groceryHomeThreeSelected = False
    app.winGame = False
    app.loseGame = False
    # map variables
    app.tepper = False
    app.scotty = False
    app.cuc = False
    
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

# def mapScreen_redrawAll(app):
#     drawScreenTitle(app, 'Maps Screen')
#     drawRect(0, 0, 200, 200, fill='blue')

def mapScreen_onKeyPress(app, key):
    onKeyPressHelper(app, key)
 
def mapScreen_redrawAll(app):
    drawRect(0, 0, app.width, app.height, fill = 'limeGreen')
    drawLabel('Map of CMU', app.width/2, 40, size = 25, bold = True, font = 'montserrat')
    drawRect(0, app.height/2 - 30, app.width, 80, fill = 'gray')
    drawLine(0, app.height/2 + 10, app.width, app.height/2 + 10, fill = 'black', dashes = True, lineWidth = 2)
    drawLine(0, app.height/2 - 30, app.width, app.height/2 - 30, fill = 'black', lineWidth = 3)
    drawLine(0, app.height/2 + 50, app.width, app.height/2 + 50, fill = 'black',  lineWidth = 3)
 
    drawRect(25, 75, 100, 175, fill = 'lightCyan')   
    drawRect(150, 75, 100, 50, fill = 'lightCyan')
    drawRect(150, 150, 100, 100, fill = 'lightCyan')
 
    tepColor = 'darkOrange' if app.tepper == True else 'tomato'
    drawRect(275, 75, 200, 175, fill = tepColor)
    drawLabel("Visit Tepper!", 375, 75 + 175/2, size = 20, font = 'montserrat')
    drawRect(500, 150, 100, 100, fill = 'lightCyan')
    drawRect(500, 75, 100, 50, fill = 'lightCyan')
 
    scottyColor = 'darkOrange' if app.scotty == True else 'tomato'
    drawRect(625, 75, 250, 125, fill = scottyColor)
    drawLabel("Visit Scotty's!", 625 + 250/2, 75 + 125/2, size = 20, font = 'montserrat')
    drawRect(625, 225, 75, 25, fill = 'lightCyan')
    drawRect(725, 225, 150, 25, fill = 'lightCyan')
 
    drawRect(25, 375, 100, 175, fill = 'lightCyan')
    drawRect(150, 500, 100, 50, fill = 'lightCyan')
    drawRect(150, 375, 100, 100, fill = 'lightCyan')
 
    cucColor = 'darkOrange' if app.cuc == True else 'tomato'
    drawRect(275, 375, 325, 175, fill = cucColor)
    drawLabel("Visit the CUC!", 275 + 325/2, 375 + 175/2, size = 20, font = 'montserrat')
    drawRect(625, 375, 100, 50, fill = 'lightCyan')
    drawRect(625, 450, 100, 100, fill = 'lightCyan')
    drawRect(750, 375, 125, 125, fill = 'lightCyan')
    drawRect(750, 525, 50, 25, fill = 'lightCyan')
    drawRect(825, 525, 50, 25, fill = 'lightCyan')
 
def mapScreen_onMouseMove(app, mouseX, mouseY):
    isTepperSelected(app, mouseX, mouseY)
    isScottySelected(app, mouseX, mouseY)
    isCUCSelected(app, mouseX, mouseY)
 
def mapScreen_onMousePress(app, mouseX, mouseY):
    if app.tepper == True:
        pass
    elif app.scotty == True:
        setActiveScreen('groceryHomeScreen')
    elif app.cuc == True:
        pass
 
def isTepperSelected(app, mouseX, mouseY):
    if 275 <= mouseX <= 475 and 75 <= mouseY <= 250:
        app.tepper = True
    else:
        app.tepper = False
 
def isScottySelected(app, mouseX, mouseY):
    if 625 <= mouseX <= 875 and 75 <= mouseY <= 200:
        app.scotty = True
    else:
        app.scotty = False
 
def isCUCSelected(app, mouseX, mouseY):
    if 275 <= mouseX <= 600 and 375 <= mouseY <= 550:
        app.cuc = True
    else:
        app.cuc = False

####################################################
# groceryHomeScreen
####################################################

def groceryHomeScreen_redrawAll(app):
    drawScreenTitle(app, 'Grocery Screen')
    drawImage(app.scottyUrl, 0, 0)
    # drawRect(app.width/2 - 70, app.height/2 - 10, 140, 50, fill='white')
    drawLabel('Grocery Store', app.width/2, 70, size=50, fill='black')
    for i in range(3):
        drawRect(app.width/2 - 100, 100*(i+2), 200, 80, fill='white', border='black')
    drawLabel('Checkout', app.width/2, 100*2 + 40, size=24)
    drawLabel('Order To-Go', app.width/2, 100*3+40, size=24)
    drawLabel('Small Talk', app.width/2, 100*4+40, size=24)

    # drawRect(app.width/2 - 70, app.height/2 )

def groceryHomeScreen_onMousePress(app, mouseX, mouseY):
    if (app.width/2-100 <= mouseX <= ((app.width/2)-100) + 200 and
        (100*2) <= mouseY <= (100*2)+80):
        app.groceryHomeOneSelected = True
        setActiveScreen('groceryOneScreen')
    elif (app.groceryHomeOneSelected == True and app.width/2-100 <= mouseX <= ((app.width/2)-100) + 200 and
        (100*3) <= mouseY <= (100*3)+80):
        app.groceryHomeTwoSelected = True
        setActiveScreen('groceryTwoScreen')
    elif (app.groceryHomeOneSelected == True and app.groceryHomeTwoSelected == True and 
          app.width/2-100 <= mouseX <= ((app.width/2)-100) + 200 and 
          (100*4) <= mouseY <= (100*4)+80):
        app.groceryHomeThreeSelected = True
        setActiveScreen('groceryThreeScreen')

def groceryHomeScreen_onKeyPress(app, key):
    onKeyPressHelper(app, key)

####################################################
# groceryOneScreen
####################################################

def groceryOneScreen_redrawAll(app):
    drawLabel('Cashier', app.width/2, app.height/2)
    drawImage(app.cashierUrl, -100, -100)

def groceryOneScreen_onKeyPress(app, key):
    onKeyPressHelper(app, key)

# def groceryOneScreen_onMousePress(app, mouseX, mouseY):

####################################################
# groceryTwoScreen
####################################################

def groceryTwoScreen_redrawAll(app):
    drawLabel('Order To-Go', app.width/2, app.height/2)

def groceryTwoScreen_onKeyPress(app, key):
    onKeyPressHelper(app, key)

####################################################
# groceryThreeScreen
####################################################

def groceryThreeScreen_redrawAll(app):
    drawLabel('Small Talk', app.width/2, app.height/2)

def groceryThreeScreen_onKeyPress(app, key):
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