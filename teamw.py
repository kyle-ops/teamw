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

update()
