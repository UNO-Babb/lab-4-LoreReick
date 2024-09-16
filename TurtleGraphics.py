#TurtleGraphics.py
#Name: Lore Reick
#Date: 9/16/24
#Assignment: Lab 4
import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS
#This draws squares
def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)
#This draws Polygons
def drawPolygon(myTurtle, sides):
    for s in range(sides):
        myTurtle.forward(50)
        myTurtle.right(360/sides)

def fillCorner(turt, corner):
    #draw big square
    drawSquare(turt, 100)
    #This fills the Top left
    if corner == 1:
        turt.begin_fill()
        drawSquare(turt,50)
        turt.end_fill()
    #Top Right
    if corner == 2:
        turt.forward(50)
        turt.begin_fill()
        drawSquare(turt,50)
        turt.end_fill()
    #Bottom Left
        if corner == 3:
        turt.right(90)
        turt.forward(50)
        turt.left(90)
        turt.begin_fill()
        drawSquare(turt,50)
        turt.end_fill()
    #Bottom Right
    elif corner == 4:
        turt.right(90)
        turt.forward(100)
        turt.left(90)
        turt.forward(50)
        turt.left(90)
        turt.begin_fill()
        drawSquare(turt,50)
        turt.end_fill()
 #This draws squares inside of squares      
def squaresInSquares(turt, squareamount):
    turt.penup()
    turt.left(45)
    turt.forward(60)
    turt.right(135)
    turt.pendown()
    squaresize = 100
    counter = 0
    while counter < int(squareamount):
       drawSquare(turt, squaresize)
       turt.penup()
       turt.left(135)
       turt.forward(15)
       turt.right(135)
       turt.pendown()
       squaresize = squaresize + 20
       counter = counter + 1
       
def TurtleDrawing(myTurtle, amount):
    #Colors and draws the body of the turtle. It is brown. The body is an octogon.
    myTurtle.fillcolor("brown")
    myTurtle.begin_fill()
    drawPolygon(myTurtle, 8)
    myTurtle.end_fill()
    #Colors and draws leg one. It is red.The legs are triangles.
    myTurtle.left(225)
    myTurtle.fillcolor("red")
    myTurtle.begin_fill()
    drawPolygon(myTurtle,3)
    myTurtle.end_fill()
    #This section moves the turtle to draw the second leg. It is blue! 
    myTurtle.right(225)
    myTurtle.forward(50)
    myTurtle.right(45)
    myTurtle.forward(50)
    myTurtle.left(180)
    myTurtle.fillcolor("blue")
    myTurtle.begin_fill()
    drawPolygon(myTurtle,3)
    myTurtle.end_fill()
    #This section moves the turtle to draw the third leg. It is green.
    myTurtle.right(225)
    myTurtle.forward(50)
    myTurtle.right(45)
    myTurtle.forward(50)
    myTurtle.left(180)
    myTurtle.fillcolor("green")
    myTurtle.begin_fill()
    drawPolygon(myTurtle,3)
    myTurtle.end_fill()
    #This is the last section that moves to the last leg, and it is pink.
    myTurtle.right(225)
    myTurtle.forward(50)
    myTurtle.right(45)
    myTurtle.forward(50)
    myTurtle.left(180)
    myTurtle.fillcolor("pink")
    myTurtle.begin_fill()
    drawPolygon(myTurtle,3)
    myTurtle.end_fill()
    # The turtle has no head. It is dead.
        
        
        
    
     


def main():
    myTurtle = turtle.Turtle()
    # Try These! Just Unhashtag them.
    #drawPolygon(myTurtle, 5) #draws a pentagon
    #drawPolygon(myTurtle, 8) #draws an octogon
    
    #TurtleDrawing(myTurtle, 1) # Draws a poorly represented Turtle.

    #fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    #fillCorner(myTurtle, 4) #draws a square bottom left corner filled in.

    #squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    #squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()