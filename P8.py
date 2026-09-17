import turtle
import random
#Screen Setup

screen = turtle.Screen()

screen.setup(width=800,height=700)
screen.setworldcoordinates(-500,-500,500,500)
screen.title('Plot 4')
screen.tracer(0,0)
t = turtle.Turtle()

def DrawRectangle():
    t.goto(-350,500)
    t.fillcolor('Black')
    t.pendown()
    t.begin_fill()
    t.goto(350,500)
    t.goto(350,-100)
    t.goto(-350,-100)
    t.goto(-350,500)
    t.end_fill()
    t.penup()

Nrows=6
Ncols=7

def Draw_Circle(x,y,r,fill_Col):
    t.goto(x,y)
    t.setheading(-90)
    t.fillcolor(fill_Col)
    t.begin_fill()
    t.circle(r)
    t.end_fill()

boards=[]

NRows=6
NCols=7

board = [[0 for i in range(NCols)] for j in range(NRows)]

def DrawBoard():
    DrawRectangle()
    for kk in range(Nrows):
      for jj in range(Ncols):
        if board[kk][jj] == 0:
          Draw_Circle(-340 + jj*100, 450 - kk*100, 40, 'white')
        if board[kk][jj] == 1:
          Draw_Circle(-340 + jj*100, 450 - kk*100, 40, 'blue')
        if board[kk][jj] == 2:
          Draw_Circle(-340 + jj*100, 450 - kk*100, 40, 'red')

def All_same(cells, value):
#Checks whether all are same
  allequal = True
  
  for cell in cells: 
    if cell != value:
      allequal = False
      break

  return allequal

def checkHorizontalWinner(value):
# Horizontal Wins
  winner = False
  for jj in range(NRows):
    for kk in range(4):
      cells = []
      for cnt in range(4):
        cells.append(board[jj][kk+cnt])
        
      if All_same(cells, value):
        winner = True
        break

  return winner

def checkVerticalWinner(value):
#Vertical Winner 
  winner = False
  for jj in range(3):
    for kk in range(NCols):
      cells = []
      for cnt in range(4):
        cells.append(board[jj+cnt][kk])
      if All_same(cells, value):
        winner = True
        break

  return winner

def checkDiagonalOneWinner(value):
#Diagonal Winner
  winner = False
  for jj in range(3,NRows,1):
    for kk in range(4):
      cells = []
      for cnt in range(4):
        cells.append(board[jj-cnt][kk+cnt])
      if All_same(cells, value):
        winner = True
        break

  return winner


def checkDiagonalTwoWinner(value):
#Diagonal winner
  winner = False
  # Check for cells sloping downwards
  for jj in range(0,3,1):
    for kk in range(4):
      cells = []
      for cnt in range(4):
        cells.append(board[jj+cnt][kk+cnt])
      if All_same(cells, value):
        winner = True
        break

  return winner







def checkwinner(value):
#Combined it all
  winner = checkHorizontalWinner(value)
  if not winner:
    # No winner yet
    winner = checkVerticalWinner(value)
    if not winner:
      winner = checkDiagonalOneWinner(value)
      if not winner:
        winner = checkDiagonalTwoWinner(value)
        
  return winner

      
    


def lowest_row(col):
  # Find the lowest available row in a given column
  r = -1
  for kk in range(Nrows-1, -1, -1):
    if board[kk][col] == 0:
      r = kk
      break
      
  return r


def play(x, y):

  global turn, gameOver
  if gameOver:
    return
  
  col = int((x + 350)//100)
   # determine the column (Depending on the click location)
  
  if col < 0: 
    col = 0
  if col > Ncols-1:
    col = Ncols - 1

  avail_cols = find_open_cols()

  if col in avail_cols:
#Lowest available ROW!!
    available_row = lowest_row(col)
    board[available_row][col] = 1
  
    DrawBoard()

    if checkwinner(1):
      gameOver = True
      print('Player Wins')
    else:
      turn = 2
  
  if turn == 2:
    playc()
  
  
  
def find_open_cols():
  open_cols = [m for m in range(Ncols)]
  full_cols = []

  # Remove those columns that are full
  for col in open_cols:
    if lowest_row(col) == -1:
      full_cols.append(col)

  for col in full_cols:
    open_cols.remove(col)

  return open_cols

def display_board():
  for kk in range(NRows):
    print(board[kk])



def playc():
  global turn, gameOver
  # Find which columns are available
  # Consider all the columns
  cols_avail = find_open_cols()
  #print(cols_avail)
  # Pick up a random column from those that are open
  if len(cols_avail) > 0:
    col = random.choice(cols_avail)
    available_row = lowest_row(col)
    board[available_row][col] = 2  
  
  DrawBoard()
  # Check for winner and accordingly decide whether next player or game over
  if checkwinner(2):
    gameOver = True
    print('Computer Wins')
  else:
    turn = 1


gameOver = False   
turn = 1


DrawBoard()
screen.onclick(play)

gameOver = False

if random.random()>0.5:
  turn =1
  print("Player's Chance")
else:
  turn=2
  print("Computer's chance")
  playc()

DrawBoard()  