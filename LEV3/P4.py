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

import turtle

def koch_curve(t, length, depth):
    """Draws a single side of the Koch snowflake recursively."""
    if depth == 0:
        t.forward(length)
    else:
        # Divide the length by 3 for the smaller segments
        length /= 3.0
        
        # Draw the 4 sub-segments with specific turning angles
        koch_curve(t, length, depth - 1)
        t.left(60)
        koch_curve(t, length, depth - 1)
        t.right(120)
        koch_curve(t, length, depth - 1)
        t.left(60)
        koch_curve(t, length, depth - 1)

def draw_snowflake(length, depth):
    """Combines three Koch curves into an equilateral triangle snowflake."""
    # Setup window and turtle
    screen = turtle.Screen()
    screen.bgcolor("white")
    
    t = turtle.Turtle()
    t.speed(0)  # Fastest drawing speed
    t.penup()
    t.goto(-length / 2, length / 3)  # Center the snowflake roughly
    t.pendown()
    t.pensize(2)
    
    # Loop 3 times to form the base equilateral triangle
    for _ in range(3):
        koch_curve(t, length, depth)
        t.right(120)
        
    # Keep screen open until it is clicked
    screen.exitonclick()

# Run the program: length = 300 pixels, recursion depth = 4


draw_snowflake(length=300, depth=4)




turtle.mainloop()
    
