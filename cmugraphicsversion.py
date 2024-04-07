
from cmu_graphics import *
import random
import pyaudio
import wave
import speech_recognition as sr

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
    app.cashierUrl = "https://i.pinimg.com/736x/63/fe/45/63fe45b8bd25e633c93b40c765dcae26.jpg"
    app.language = 'chinese'
    # help screen
    app.play = False
    # app.url = 'https://drive.google.com/file/d/1PTMYdlDgp2zHuR9niUs-DdMMH4sp5onp/view?usp=sharing'
    app.url = "https://files.oaiusercontent.com/file-LTdIVW5JJgHdeNxPDMGaSx8V?se=2024-04-07T06%3A25%3A39Z&sp=r&sv=2021-08-06&sr=b&rscc=max-age%3D31536000%2C%20immutable&rscd=attachment%3B%20filename%3Dc62f5cf8-0763-49a6-a229-98493239a332.webp&sig=vu%2BkfBUP2TEIVQdkMqhB19WJq0HuuoTCMjbIqjgp7E4%3D"
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
    # recording
    app.recordButton = False
    app.correctPhraseSaid = False
    
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

# def helpScreen_redrawAll(app):
#     drawRect(0, 0, app.width, app.height, fill='honeydew')
#     drawScreenTitle(app, 'Help Screen')

def helpScreen_onKeyPress(app, key):
    onKeyPressHelper(app, key)
 
def helpScreen_redrawAll(app):
    drawScreenTitle(app, 'Help Screen')
    #drawImage(app.url, -75, -265)
    color = 'lightCyan' if app.play else 'paleTurquoise'
    drawRect(app.width/2 - 125, 525, 250, 50, fill = color, 
        border = 'midnightBlue', borderWidth = 8)
    drawLabel("Press Play!", app.width/2, 550, size = 16, font = 'montserrat', bold = True)
 
def helpScreen_onMouseMove(app, mouseX, mouseY):
    isPlay(app, mouseX, mouseY)
 
def helpScreen_onMousePress(app, mouseX, mouseY):
    if app.play == True:
        setActiveScreen('mapScreen')
 
def isPlay(app, mouseX, mouseY):
    if 325 <= mouseX <= 575 and 525 <= mouseY <= 575:
        app.play = True
    else:
        app.play = False

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
    drawImage(app.cashierUrl, 100, -50)
    drawRect(app.width/2-255, app.height/2+150, 510, 100, fill='white')
    drawRect(75, 150, 200, 100, fill='orangeRed')
    drawLabel('nǐ xiǎng zěn yàng tāo qián?', 175, 200, fill='black')
    drawButton(app)
    if app.recordButton == True:
        drawLabel("Recording...", 850, 100, size = 16)
        drawLabel(f'Are you using card or cash, or Flex today?', app.width/2, app.height/2, fill='black', size = 30)
    if app.correctPhraseSaid:
        drawLabel('CORRECT PHRASE', app.width/2, app.height/2, fill='green')
    elif app.correctPhraseSaid == False and app.recordButton == True:
        drawLabel('WRONG PHRASE', app.width/2, app.height/2, fill='green')


def drawButton(app):
    drawCircle(850, 50, 20, fill='red')
    drawCircle(850, 50, 25, fill=None, border='red')
    drawLabel('REC', 850, 50, fill='white')

def groceryOneScreen_onKeyPress(app, key):
    onKeyPressHelper(app, key)

def distance(x0, y0, x1, y1):
    return ((x1 - x0)**2 + (y1 - y0)**2)**0.5

def groceryOneScreen_onMousePress(app, mouseX, mouseY):
    cx = 850
    cy = 50
    r = 25
    # test for intersection
    if distance(cx, cy, mouseX, mouseY) <= r:
        # yes, it is inside the circle!
        # so increase the counter
        app.recordedText = record(app)
        print(app.recordedText)
        app.recordButton = True
        app.compText = '我要用卡掏'
        app.correctPhraseSaid = findHowAccurateRecording(app.recordedText, app.compText)
        
            

def record(app):
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    CHUNK = 1024
    RECORD_SECONDS = 10
    WAVE_OUTPUT_FILENAME = "speech.wav"
    
    # Initialize PyAudio
    audio = pyaudio.PyAudio()
    
    # Open recording stream
    stream = audio.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)
    
    # drawLabel("Recording...", 850, 60, size = 20)
    
    frames = []

    # Record audio in chunks
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    
    print("Finished recording.")
    
    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save the recorded audio to a file
    with wave.open(WAVE_OUTPUT_FILENAME, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
    
    print("Audio saved to", WAVE_OUTPUT_FILENAME)
    return translate(app)

def translate(app):
    if app.language == 'chinese':
        return chineseText()

def chineseText():
    # Initialize the recognizer
    recognizer = sr.Recognizer()
    
    # Specify the path to the WAV file containing Chinese speech
    wav_file_path = "speech.wav"

    # Load the audio file
    with sr.AudioFile(wav_file_path) as source:
        # Adjust for ambient noise if necessary
        recognizer.adjust_for_ambient_noise(source)
        # Record the audio from the WAV file
        audio = recognizer.record(source)

    try:
        print("Recognizing...")
        # Use Google's speech recognition with Chinese language parameter
        text = recognizer.recognize_google(audio, language='zh-CN')  # 'zh-CN' for Simplified Chinese
        return text
    except sr.UnknownValueError:
        return "Sorry, I couldn't understand what was said in the audio."
    except sr.RequestError as e:
        return "Sorry, I couldn't request results from the speech recognition service; {0}".format(e)

def findHowAccurateRecording(recText, compText):
    accurateWordCount = 0
    accuracy = None
    print(recText)
    for i in range(min(len(recText), len(compText))):
        if recText[i] == compText[i]:
            accurateWordCount += 1
    accuracy = accurateWordCount/len(compText)
    return accuracy > .4

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
