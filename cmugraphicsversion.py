from cmu_graphics import *
import random

def onAppStart(app):
    app.cx = 300
    app.cy = 200
    app.r = 50
    app.dx = 10 # amount to change app.cx 
    app.insideCount = 0
    app.outsideCount = 0
    app.color = 'blue'
    

def pointIsInEitherPartialDot(app, mouseX, mouseY):
    d = distance(app.cx, app.cy, mouseX, mouseY)
    if d <= app.r:
        return True
    elif app.cx + app.r > app.width:
        partialAmount = (app.cx + app.r) - app.width
        middleOfPartialDot = partialAmount - app.r
        d = distance(middleOfPartialDot, app.cy, mouseX, mouseY)
        if d <= app.r:
            return True
    else:
        return False
        
def redrawAll(app):
    drawLabel('Click in Partial Dots', 200, 30, size=16)
    drawLabel('Press the left or right arrow', 200, 50, size=12)
    drawLabel('Click inside and outside the partial dots', 200, 70, size=12)
    # Draw the dot:
    drawCircle(app.cx, app.cy, app.r, fill=app.color)
    # And if part of the dot extends beyond the right
    # edge, draw that same amount of dot on the left edge:
    if app.cx > app.width - app.r:
        pixelsBeyondRightEdge = (app.cx + app.r) - app.width
        cx = -app.r + pixelsBeyondRightEdge
        drawCircle(cx, app.cy, app.r, fill=app.color)
    
    drawLabel(f'Clicks inside: {app.insideCount}', 200, 100)
    drawLabel(f'Clicks outside: {app.outsideCount}', 200, 120)

def onKeyPress(app, key):
    if key == 'right':
        app.cx += app.dx
        if app.cx >= app.width + app.r:
            app.cx = app.r
    elif key == 'left':
        app.cx -= app.dx
        if app.cx - app.r < 0:
            # The dot is partly off the left edge, so add
            # app.width to it, so that it instead sits partly
            # off the right edge:
            app.cx += app.width

def distance(x1, y1, x2, y2):
    xValues = (x2 - x1)**2
    yValues = (y2 - y1)**2
    distanceFormula = (xValues + yValues)**(1/2)
    return distanceFormula
    
def onMouseMove(app, mouseX, mouseY):
    if pointIsInEitherPartialDot(app, mouseX, mouseY) == True:
        app.color = 'pink'
    else:
        app.color = 'blue'


def onMousePress(app, mouseX, mouseY):
    if pointIsInEitherPartialDot(app, mouseX, mouseY) == True:
        app.insideCount += 1
    else:
        app.outsideCount += 1

def main():
    runApp()

main()

cmu_graphics.run()