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

update()
