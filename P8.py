import turtle
#Screen Setup

screen = turtle.Screen()

screen.setup(width=800,height=700)
screen.setworldcoordinates(-500,-500,500,500)
screen.title('Plot 4')
screen.tracer(0,0)
t = turtle.Turtle()

def DrawRectangle():
    t.goto(-350,100)
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
screen.update()      


DrawBoard()  
turtle.done()        










