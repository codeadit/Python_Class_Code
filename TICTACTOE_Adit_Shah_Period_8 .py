board = [[0,0,0],
        [0,0,0],
        [0,0,0]]

player = 0
x = 0
y = 0

def win(board):
   for i in range(3):
      if board[i][0] == board[i][1] == board[i][2] != 0:
         return board[i][0]
      if board[0][i] == board[1][i] == board[2][i] != 0:
         return board[0][i]
   if (board[0][0] == board[1][1] == board[2][2] != 0 
       or board[0][2] == board[1][1] == board[2][0] != 0):
      return board[1][1]

   for x in range(3):
      if 0 in board[x]:
         return 0
   return 3

def prettyprint(board):
   for i in range(3):
    print(" ")
    print("-"*17)
    for x in range(3):
      if 1 == board[i][x]:
          print("| X |", end = " ")
      elif 2 == board[i][x]:
          print("| O |", end = " ")
      elif 0 == board[i][x]:
          print("|   |", end = " ")
   print()
   print("-" * 17)

def turn(board, player):
   print("Player ",player,"'s turn")
   x = int(input("Enter the row: "))
   y = int(input("Enter the column: "))
   while board[x][y] != 0:
     x = int(input("Player" + str(player) + ": Please enter another row:"))
     y = int(input("Player" + str(player) + ": Please enter another column:"))
   board[x][y] = player
   prettyprint(board)
   if win(board) == player:
      print("Player " + str(player) + " wins!")
      return 
   if win(board) == 3:
      print("Tie!")
      return
   return x, y

def two_player(board):
   while win(board) == 0:
    player = 1
    turn(board, 1)
    if win(board) == 0:
      player = 2
      turn(board, 2)
  
two_player(board)