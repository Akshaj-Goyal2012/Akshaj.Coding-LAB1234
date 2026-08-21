import turtle
t = turtle.Turtle()

x = 123

def left_circular_shift(x,d,nbits):
  x_s=x<<d
  mask_lower=int('0b'+nbits*'1')
  mask_upper=('0b'+d*'1',2)<<nbits
  overflow=(x_s&mask_upper)>>nbits
  x_cs=(x_s&mask_lower)|overflow

  return x_cs

def left_shift_click(x,s,nbits):
  y=x <<s
  if y > 2**nbits - 1:
    y=2**nbits - 1
  return y  

def swap_bits(x,p1,p2):
  b1= x&(1<<p1)
  b1_shift=b1<<(p2>>p1)

  b2=x&(1<<p2)
  b2_shift=b2>>(p2-p1)

  tmp=(1<<p1)|(1<<p2)
  tmp=255^tmp

  x_new=x&tmp
  y=x_new|b1_shift|b2_shift
  return y


clr = 'red'

def draw_sq(x, y, clr):
  t.penup()
  t.goto(x, y)
  t.setheading(0)
  t.pendown()
  t.fillcolor(clr)
  t.begin_fill()
  for _ in range(4):
    t.forward(20)
    t.left(90)
  t.end_fill()
  t.penup()


#draw_sq(0, 0, 'red')
t.speed(0)
x = 234
import time

ts = turtle.Screen()
ts.tracer(0)

#pattern = int(input('A number between 0 and 255'))
t.penup()


style = 3

if style == 0:
  pattern = 0b000000011
if style == 1:
  pattern = 0b11000000
if style == 2:
  pattern = 0b11000011
if style == 3:
  pattern = 0b00000001

for cnt in range(1000):
  if style == 0:
    pattern = pattern << 2
    if pattern > 0b11111111: 
      pattern = 0b00000011
  if style == 1:
    pattern = pattern >> 2
    if pattern == 0b00000000:
      pattern = 0b11000000
  if style == 2:
    pattern = pattern ^ 0b11111111
  if style == 3:
    if pattern == 0b11111111:
      pattern = 0b00000000
    pattern = pattern | (1 << cnt%8)
  if style == 5:
    pattern = 0b01111111
    


  ts.tracer(0)
  for kk in range(8):
    b = (pattern & (2**kk)) >> kk
    t.goto(100 - 40*kk, 40)
    t.write('b' + str(kk))
    if b == 1:
      draw_sq(100- 40*kk, 0, 'red')
    else:
      draw_sq(100 - 40*kk, 0, 'white')
  ts.update()
  time.sleep(0.5)

