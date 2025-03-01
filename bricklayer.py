import turtle

screen = turtle.Screen()
screen.screensize(400,400)
screen.setworldcoordinates(0,0,400,400)

pointer = turtle.Turtle()
pointer.up()
pointer.hideturtle()
pointer.speed(0)

def drawRect(x, y, length, height):
  pointer.up()
  pointer.goto(x,y)
  pointer.begin_fill()
  pointer.down()
  pointer.goto(x+length, y)
  pointer.goto(x+length, y+height)
  pointer.goto(x, y+height)
  pointer.goto(x, y)
  pointer.up()
  pointer.end_fill()

def drawBrickWall(rows, cols, brickWidth, brickHeight, mortarWidth):
    for i in range(rows):
      for x in range(cols):
        drawRect((brickWidth+mortarWidth)*x,(brickHeight+mortarWidth)*i,brickWidth,brickHeight)

def drawBrickWallOffset(rows, cols, brickWidth, brickHeight, mortarWidth):
  smallWidth = brickWidth/2-mortarWidth/2
  colsoriginal = cols
  for i in range(rows):
    movement = 0
    if i%2 == 1:
      cols = 1 + colsoriginal
    else:
      cols = colsoriginal
    for x in range(cols):
      if i%2 == 1 and (x == 0 or x == cols-1):
        width = smallWidth
      else:
        width = brickWidth
      drawRect(movement,(brickHeight+mortarWidth)*i,width,brickHeight)
      movement += width + mortarWidth

def drawBrickWallCustom(rows, cols, brickWidth, brickHeight, mortarWidth):
  smallWidth = brickWidth/2-mortarWidth/2
  colsoriginal = cols
  for i in range(rows):
    movement = 0
    if i%2 == 1:
      cols = 2*colsoriginal
    else:
      cols = colsoriginal
    for x in range(cols):
      if i%2 == 1 and cols == 2*colsoriginal:
        width = smallWidth
      else:
        width = brickWidth
      drawRect(movement,(brickHeight+mortarWidth)*i,width,brickHeight)
      movement += width + mortarWidth 
      
drawBrickWallCustom(6,7,75,20,10)
turtle.done() 