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
        triangle(x +l*1/3, y+ l*1/3, l/2)
        triangle(x - 1/3*l, y+1/3*l, l/2)
        triangle(x+1/3*l , y-1/3*l , l/2)
        triangle(x-1/3*l , y-1/3*l , l/2)



triangle(0,100,150)    

turtle.mainloop()
    
