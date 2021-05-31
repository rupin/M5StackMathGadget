from m5stack import *
from m5ui import *
from uiflow import *

setScreenColor(0x222222)


from m5stack import *
from m5ui import *
from uiflow import *




generationMode = None
number1 = None
number2 = None
optionsList = None
j = None
i = None
sumOfNumbers=None
state=0;
awaitingNextQuestion=False

label4 = M5TextBox(120, 84, "1", lcd.FONT_DejaVu72, 0xFFFFFF, rotate=0)
label0 = M5TextBox(40, 16, "", lcd.FONT_DejaVu40, 0xFFFFFF, rotate=0)
label1 = M5TextBox(40, 73, "", lcd.FONT_DejaVu40, 0xFFFFFF, rotate=0)
label2 = M5TextBox(0, 73, "+", lcd.FONT_DejaVu40, 0xFFFFFF, rotate=0)
label5 = M5TextBox(40, 130, "", lcd.FONT_DejaVu40, 0xFFFFFF, rotate=0)
A1 = M5TextBox(50, 192, "", lcd.FONT_DejaVu24, 0xFFFFFF, rotate=0)
A2 = M5TextBox(144, 192, "S", lcd.FONT_DejaVu24, 0xFFFFFF, rotate=0)
A3 = M5TextBox(235, 192, "", lcd.FONT_DejaVu24, 0xFFFFFF, rotate=0)
line0 = M5Line(M5Line.PLINE, 6, 125, 150, 125, 0xFFFFFF)

label3 = M5TextBox(13, 151, "", lcd.FONT_Default, 0xFFFFFF, rotate=0)

import random
bufferBlank = open("res/blank.png").read()
bufferCrying = open("res/crying.png").read()
bufferThinking = open("res/thinking.png").read()
bufferParty = open("res/party.png").read()
#def eraseImage():
  
  #for i in range(0,80):
   # lcd.rect(80+i, 100, 80,80, color=0xffffff)

questionCount=0  
def setLabels():
  global questionCount
  questionCount=1
  if(state==0):
    #lcd.fill()
    line0.hide()
    label2.hide()
    label0.setText("")
    label1.setText("")
    A1.setText("<")
    A3.setText(">")
    label4.setText("1")
    label5.hide()

    


def enableQuestionUI():
    #lcd.fill(0x222222)
    line0.show()
    label2.show()
    label0.setText("***")
    label1.setText("***")
    A1.setText("***")
    A2.setText("***")
    A3.setText("***")
    A1.setPosition(50, 192)
    A2.setPosition(136, 192)
    A3.setPosition(224,192)
    label4.hide()
    
def showCorrectAnswer():
    global sumOfNumbers  
    line0.show()
    label2.show()
    A1.setText("")
    A2.setText("")
    A3.setText(">")
    A1.setPosition(50, 192)
    A2.setPosition(136, 192)
    A3.setPosition(224,192)
    label4.hide()
    label5.setText(formatNumber(sumOfNumbers))
  


def setImage(emotion):
  global bufferBlank, bufferCrying
  lcd.image_buff(200, 30, bufferBlank)
  
  if(emotion=="crying"):
    speaker.sing(220, 1/4)
    lcd.image_buff(200, 30, bufferCrying)
  
  if(emotion=="thinking"):
    lcd.image_buff(200, 30, bufferThinking)
    
  if(emotion=="party"):
    lcd.image_buff(200, 30, bufferParty)

def formatNumber(number):
  if(number<10):
    return "    "+str(number)
  
  elif(number<100 and number>9):
    return "  "+str(number)
  
  else:
    return str(number)
  
    
  
  

def showNewQuestion():
  global generationMode, number1, number2 
  global optionsList, j, shuffledList 
  global randomPosition, sumOfNumbers
  if generationMode:
    
    generationMode = False
    
    number2 = random.randint(1, 500)
    number1 = random.randint(1, 699)
    sumOfNumbers=number1+number2
    label0.setText(formatNumber(number1))
    label1.setText(formatNumber(number2))
    optionsList = []
    shuffledList = [0,0,0]
    
    
    for j in range(0, 3):
      optionsList.append(number1 + number2)
      optionsList.append(number1 + number2+random.randint(1, 10))
      optionsList.append(number1 + number2+random.randint(1, 10))    


    randomPosition = random.randint(1, 6)
    #label3.setText(str(len(optionsList)))


    for j in range(0, 3):
      shuffledList[j]=optionsList[randomPosition+j]
    A1.setText(str(shuffledList[0]))
    A2.setText(str(shuffledList[1]))
    A3.setText(str(shuffledList[2]))
    #reDraw()
    label5.setText("")
    setImage("thinking")
 
      
  

  


def updateQuestionCount(delta):
  global questionCount
  questionCount=questionCount+delta
  if(questionCount==0):
    questionCount=1
  label4.setText(str(questionCount))
  
  
  

def buttonA_wasPressed():
  global state
  
  
  if(state==0):
    updateQuestionCount(-1)
  elif(state==1):
    showNewQuestion()
    state=2
  elif(state==2):
    handleButton(0)
  elif(state==3):
    generationMode=True
    showNewQuestion();
    state=2
    

def buttonB_wasPressed():
  global state
  if(state==0):
    enableQuestionUI();
    state=1
  elif(state==2):
    handleButton(1)
    
  elif(state==3):
    generationMode=True
    showNewQuestion();
    state=2

  

def buttonC_wasPressed():
  global state
  
  if(state==0):
    updateQuestionCount(1)
  elif(state==2):
    handleButton(2)
  elif(state==3):
    generationMode=True
    showNewQuestion();
    state=2

    
def handleButton(buttonNumber):
  global state, generationMode, shuffledList, sumOfNumbers, questionCount
  if(shuffledList[buttonNumber]==sumOfNumbers):
      #label3.setText("Correct")
      setImage("party")
  else:
      #reDraw()
      setImage("crying")
  questionCount=questionCount-1    
  generationMode = True    
  showCorrectAnswer()
  if(questionCount>0):
    state=3  
  else:
    state=4
  
  

btnA.wasPressed(buttonA_wasPressed)
btnB.wasPressed(buttonB_wasPressed)
btnC.wasPressed(buttonC_wasPressed)

generationMode = True
#wait(1)
#buttonA_wasPressed()
setLabels()












