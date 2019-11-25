from turtle import *
w = Turtle()
colormode(255)

def reminder():
  # by Mr. Riley
  # don't forget to put a comment with your name at the top of each function you make
  # this will help to keep track of who created each function
  return True
  
def makeSkyscraper():
    #Made by Dominick
    w.fillcolor((.5,.5,.5))
    w.begin_fill()
    w.forward(150)
    w.left(90)
    w.forward(500)
    w.left(90)
    w.forward(150)
    w.left(90)
    w.forward(500)
    w.penup()
    w.left(90)
    w.forward(25)
    w.left(90)
    w.forward(50)
    w.pendown()
    w.end_fill()
    for i in range(6):
        makeWindow()
        w.penup()
        w.forward(75)
        w.pendown()
    w.right(90)
    w.penup()
    w.forward(100)
    w.right(90)
    w.forward(35)
    w.pendown()
    for i in range(6):
        makeWindow()
        w.penup()
        w.forward(75)
        w.pendown()

def makeWindow():
    #Made by Dominick
    w.fillcolor("light blue")
    w.begin_fill()
    for i in range (4):
        w.forward(40)
        w.right(90)
    w.end_fill()

def makeCloud():
    #by Dominick
    w.fillcolor("white")
    w.begin_fill()
    w.setheading(0)
    w.forward(100)
    w.left(90)
    for i in range(3):
        for i in range(110):
            w.forward(1)
            w.left(1)
        w.right(74.5)
    w.setheading(0)
    w.forward(150)
    w.end_fill()

def makeCar():
    #by Dominick
    def makeCarFrame():
        w.fillcolor(1,.1,.1)
        w.begin_fill()
        w.forward(100)
        w.right(45)
        w.forward(60)
        w.right(45)
        w.forward(50)
        w.right(90)
        w.forward(30)
        w.right(90)
        for i in range(180):
            w.left(1)
            w.forward(.5)
        w.right(90)
        w.forward(50)
        w.right(90)
        for i in range(180):
            w.left(1)
            w.forward(.5)
        w.right(90)
        w.forward(30)
        w.right(90)
        w.forward(93)
        w.right(90)
        w.forward(100)
        w.end_fill()
    makeCarFrame()
    w.penup()
    w.forward(84)
    w.right(45)
    w.forward(60)
    w.forward(10)
    w.right(45)
    w.forward(30)
    w.forward(15)
    w.right(90)
    w.forward(41)
    w.right(90)
    w.pendown()
    w.fillcolor(0,0,0)
    w.begin_fill()
    for i in range (360):
        w.left(1)
        w.forward(.45)
    w.end_fill()
    w.penup()
    w.left(90)
    w.forward(109)
    w.right(90)
    w.fillcolor(0,0,0)
    w.begin_fill()
    for i in range (360):
        w.left(1)
        w.forward(.45)
    w.end_fill()
    w.penup()
    w.forward(52)
    w.right(90)
    w.forward(100)
    w.pendown()
    w.fillcolor("light blue")
    w.begin_fill()
    w.forward(42)
    w.left(135)
    w.forward(60)
    w.left(135)
    w.forward(50)
    w.end_fill()

def makeSun():
    #by Dominick
    w.fillcolor("yellow")
    w.begin_fill()
    for i in range(360):
        w.right(1)
        w.forward(1)
    w.end_fill()
    for i in range(20):
        for i in range(18):
            w.right(1)
            w.forward(1)
        w.left(90)
        w.forward(40)
        w.left(180)
        w.forward(40)
        w.left(90)
def drawCircle(centerX, centerY, radius, color):
    w.penup()
    w.goto(int(centerX), int(centerY))
    w.setheading(0)
    w.forward(int(radius))
    w.right(90)
    w.fillcolor(color)
    w.begin_fill()
    w.pendown()
    for i in range(360):
        w.forward((2 * int(radius) * pi)/360)
        w.right(1)
    w.end_fill()

def randomRed():
    #by MatthewSharp
    return ((randint(100, 255)), 0, 0)
    

def randomBlue():
    #by MatthewSharp
    return (0, 0, (randint(100, 255)))



def randomGreen():
    #by MatthewSharp
    return (0, (randint(100, 255)), 0)


def randomOrange():
    #by MatthewSharp
    return ((randint(200, 255)), 130, 0)


def randomYellow():
    #by MatthewSharp
    return ((randint(210, 255)), 255, 0)


def randomPurple():
    #by MatthewSharp
    return ((randint(130, 220)), 0, 255)

def starfish():
  #by megan
  w.penup()
  w.goto(randint(-400,400), randint(-200,0) )
  w.pendown()
  w.fillcolor("orange")
  w.begin_fill()
  w.pendown()
  for i in range(5):
    w.forward(50)
    w.right(144)
  w.end_fill()
  w.penup()

def cresentMoon():
    #by megan
    w.left(180)
    w.begin_fill()
    w.pendown()
    for i in range(210):
        w.forward(1)
        w.right(.5)
    w.left(120)
    for i in range(400):
        w.forward(.95)
        w.left(.55)
    w.forward(12)
    w.end_fill()
    w.penup()

def stickPerson():
    #by megan
    w.begin_fill()
    w.pendown()
    for i in range(360):
     w.forward(.5)
     w.left(1)
    w.end_fill()
#body
    w.right(90)
    w.forward(125)
#right leg
    w.left(45)
    w.forward(87.5)
#left leg
    w.right(180)
    w.forward(87.5)
    w.left(90)
    w.forward(87.5)
    w.right(180)
    w.forward(87.5)
    w.left(45)
    w.forward(75)
    w.left(90)
    w.forward(75)
    w.left(180)
    w.forward(150)


def windTurbine():
  #by megan
  w.pendown()
  w.fillcolor("black")
  w.setheading(90)
  w.forward(450)
  w.right(90)
  w.forward(20)
  w.right(90)
  w.forward(450)
  w.right(180)
  w.forward(425)
  w.right(60)
  for i in range(2):
    w.forward(350)
    w.right(175)
    w.forward(400)
  w.forward(-30)
  w.left(90)
  for i in range(2):
    w.forward(350)
    w.right(175)
    w.forward(400)
  w.left(135)
  w.forward(15)
  w.right(135)
  w.begin_fill()
  for i in range(360):
    w.forward(.5)
    w.right(1)
  w.end_fill()
  w.penup()

def DrawRect(topLeftX, topLeftY, width, height, color):
  #by megan
  w.fillcolor(color)
  w.penup()
  w.goto(topLeftX, topLeftY)
  w.pendown()
  w.setheading(0)
  w.begin_fill()
  for i in range(2):
    w.forward(width)
    w.right(90)
    w.forward(height)
    w.right(90)
  w.end_fill()
  w.penup()

  def drawMountins():
    #by MatthewSharp
    w.penup()
    w.goto(-100,200)
    w.pendown()
    w.left(45)
    w.forward(150)
    w.right(90)
    w.forward(50)
    w.left(90)
    w.forward(40)
    w.right(90)
    w.forward(100)
    w.left(120)
    w.forward(100)
    w.right(140)
    w.forward(150)
    w.left(115)
    w.forward(150)
    w.right(90)
    w.forward(200)
    w.forward(-180)
    w.right(120)

    for i in range(3):
        w.forward(5)
        w.left(5)
    w.right(50)
    for i in range(3):
        w.forward(5)
        w.left(5)
    w.penup()
    w.goto(188, 280)

    w.pendown()
    for i in range(3):
        w.forward(6)
        w.left(5)
    w.right(50)

    for i in range(3):
        w.forward(6)
        w.left(5)
    w.penup()
    w.goto(20,290)
    w.pendown()

    for i in range(3):
        w.forward(6)
        w.left(5)
    w.right(50)

    for i in range(3):
        w.forward(2)
        w.left(5)
    
def fish():
  #by megan
  me.pencolor("black")
  me.fillcolor("orange")
  me.penup()
  me.goto(randint(-400,400), randint(-200,300))
  me.pendown()
  me.begin_fill()
  me.setheading(90)
  fishTailSize = random()*30+20 
  fishBodySize = random()*3+1   
  for i in range(5):
     me.forward(fishTailSize)
     me.right(120)
  me.end_fill()
  me.right(172)
  me.begin_fill()
  for i in range(60):
    me.forward(fishBodySize)
    me.right(1.4)
  me.right(90)
  for i in range(60):
    me.forward(fishBodySize)
    me.right(1.5)
  me.forward(5)
  me.end_fill()
  
  
def makeBarn():
    w.left(180)
    w.pendown()
    w.begin_fill()
    w.fillcolor(165,42,42)
    w.left(90)
    w.forward(80)
    w.right(90)
    w.forward(100)
    w.right(90)
    w.forward(80)
    w.right(50)
    w.forward(65)
    w.right(80)
    w.forward(70)
    w.right(140)
    w.end_fill()
    w.begin_fill()
    w.fillcolor("white")
    w.forward(103)
    w.left(90)
    w.forward(5)
    w.left(90)
    w.forward(101)
    w.left(90)
    w.forward(5)
    w.left(90)
    w.end_fill()
    w.penup()
    w.forward(57)
    w.right(90)
    w.forward(10)
    w.right(90)
    w.pendown()
    w.begin_fill()
    w.fillcolor("white")
    for i in range(4):
        w.forward(15)
        w.left(90)
    w.end_fill()
    
def makeTree():
    C.pendown()
    colormode(255)
    C.pencolor()
    C.begin_fill()
    C.fillcolor(0, 255, 0)
    C.forward(30)
    C.left(90)
    C.forward(150)
    C.right(90)
    C.forward(20)
    for i in range(180):
        C.forward(1)
        C.left(1)
    C.forward(0)
    C.right(90)
    for i in range(193):
        C.forward(1)
        C.left(1)
    C.right(90)
    for i in range(193):
        C.forward(1)
        C.left(1)
    C.forward(20)
    C.right(114)
    C.forward(153)
    C.end_fill()
    C.begin_fill()
    C.fillcolor(150,75,0)
    C.backward(153)
    C.left(83)
    C.forward(38)
    C.right(84)
    C.forward(150)
    C.right(90)
    C.forward(30)
    C.end_fill()
    
def makeBirf():
    w.penup()
    w.pendown()
    # By Kyle
    w.left(90)
    for i in range(180):
        w.forward(.3)
        w.right(1)
    w.left(180)
    for i in range(180):
        w.forward(.3)
        w.right(1)
    

  
update()
