board = []

question = " "

for y in range(10):
  row = []
  for x in range(10):
    row.append(0)
  board.append(row)

def prettyprint(board):
  for i in range(10):
    print(" ")
    for x in range(10):
      if 0 == board[i][x]:
          print("0 ", end = " ")
      elif 1 == board[i][x]:
          print("1 ", end = " ")

def findneighbors(x,y):
  neighbors = [(x+1,y+1), (x+1,y), (x+1, y-1), (x,y-1), (x,y+1), (x-1,y+1), (x-1,y), (x-1,y-1)]

  if x+1 > 9:
    neighbors[0] = -5, -5
    neighbors[1] = -5, -5
    neighbors[2] = -5, -5
  if y+1 > 9:
    neighbors[0] = -5, -5
    neighbors[4] = -5, -5
    neighbors[5] = -5, -5
    
  if y-1 < 0:
    neighbors[2] = -5, -5
    neighbors[3] = -5, -5
    neighbors[7] = -5, -5
  if x-1 < 0:
    neighbors[5] = -5, -5
    neighbors[6] = -5, -5
    neighbors[7] = -5, -5

  while (-5,-5) in neighbors:
    neighbors.remove((-5,-5))
  return neighbors

def neighborstate(x,y):
  alivenum = 0
  neighbors = findneighbors(x,y)
  for neighbor in neighbors:
    if board[neighbor[0]][neighbor[1]] == 1:
      alivenum += 1
    else:
      alivenum = alivenum
  return alivenum


def cubestate(x,y):
  for y in range(10):
    for x in range(10):

      if board[x][y] == 1:
        if neighborstate(x,y) < 2:
          board[x][y] = 0
        elif neighborstate(x,y) > 3:
          board[x][y] = 1

      if board[x][y] == 0:
        if neighborstate(x,y) == 3:
          board[x][y] = 1
        else:
          board[x][y] = 0
  return board

def shapes():
  x = 0
  y = 0

  end = False
  while end == False:
    main = input("Do you want to insert any more shapes or make any other squares alive? (Y/N)")

    if main == "Y":
      cell = input("Do you want to insert a cell or shape? C for cell any other letter for Shape")
      if cell == "C":
        x = int(input("What is the x coordinate?"))
        y = int(input("What is the y coordinate?"))
        board[x][y] = 1
        prettyprint(board)
      else:
        shape = input("What shape do you want to insert a cube, glider, or boat? (C/B/G)")
        if shape == "C":
          x = int(input("What is the x coordinate?"))
          y = int(input("What is the y coordinate?"))
          board[x+1][y] = 1
          board[x+1][y+1] = 1
          board[x][y+1] = 1
          board[x][y] = 1
          prettyprint(board)
        elif shape == "B":
          x = int(input("What is the x coordinate?"))
          y = int(input("What is the y coordinate?"))
          board[x+1][y] = 1
          board[x-1][y+1] = 1
          board[x][y+1] = 1
          board[x][y+1] = 1
          board[x][y] = 1
          board[x][y-1] = 1
          prettyprint(board)
        elif shape == "G":
          x = int(input("What is the x coordinate: "))
          y = int(input("What is the y coordinate: "))
          board[x][y] = 1
          board[x-1][y] = 1
          board[x+1][y] = 1
          board[x+1][y+1] = 1
          board[x+1][y-1] = 1
          board[x][y+1] = 1
          prettyprint(board)
    else:
      end = True
  return board    

exit = False 
x = 0
y = 0
while exit == False:
  run = input("Do you want to continue? (Y/N)")
  if run == "Y":
    cubestate(x,y)
    shapes()
    prettyprint(board)
  else:
    print("Here is the final board:")
    prettyprint(board)
    exit = True