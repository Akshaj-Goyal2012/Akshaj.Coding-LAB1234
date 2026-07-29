import turtle

t = turtle.Turtle()




t.penup()




def triangle(x,y,l):
    t.speed(0)
    t.penup()
    t.setheading(90)
    t.goto(x,y)
    t.pendown()
    t.setheading(60)
    t.goto(x-l,y-l)
    t.setheading(180)
    t.goto(x,y-l)
    t.goto(x-l,y-l)
    t.setheading(-60)
    t.goto(x,y)
    t.goto(x+l,y-l)
    t.goto(x,y-l)
    if l > 10:
        triangle(x +l*1/2 , y+l*1/2, l/2)
        triangle(x - l*1/2, y+l*1/2, l/2)
        triangle(x+1/2*l , y-1/2*l , l/2)
        triangle(x-1/2*l , y-1/2*l , l/2)



triangle(0,100,150)

def koch_curve(t, length, depth):
    if depth == 0:
        t.forward(length)
        return
    
    length /= 3.0
    koch_curve(t, length, depth - 1) 
    t.left(60)
    koch_curve(t, length, depth - 1) 
    t.right(120)
    koch_curve(t, length, depth - 1) 
    t.left(60)
    koch_curve(t, length, depth - 1) 

def draw_snowflake(t, length, depth):
    for _ in range(3):
        koch_curve(t, length, depth)
        t.right(120)
t.clear()

screen = turtle.Screen()


artist = turtle.Turtle()
artist.speed(0)


artist.penup()
artist.goto(-150, 90)
artist.pendown()

draw_snowflake(artist, 300, 3)
screen.mainloop()