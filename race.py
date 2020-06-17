import turtle as t
import random

#window
wn = t.Screen()
wn.title("Race")
wn.bgcolor("green")

#turtle
t.color('white')
t.speed(0)
t.penup()
t.goto(-140,140)

for i in range(15):
	t.write(i)
	t.right(90)
	t.forward(10)
	t.pendown()
	t.forward(350)
	t.penup()
	t.backward(360)
	t.left(90)
	t.forward(20)

#player1
p1 = t.Turtle()
p1.color('red')
p1.shape('turtle')
p1.shapesize(2)
p1.penup()
p1.goto(-170,100)
p1.pendown()

#player2
p2 = t.Turtle()
p2.color('blue')
p2.shape('turtle')
p2.shapesize(2)
p2.penup()
p2.goto(-170,40)
p2.pendown()

#player3
p3 = t.Turtle()
p3.color('black')
p3.shape('turtle')
p3.shapesize(2)
p3.penup()
p3.goto(-170,-20)
p3.pendown()

#player4
p4 = t.Turtle()
p4.color('yellow')
p4.shape('turtle')
p4.shapesize(2)
p4.penup()
p4.goto(-170,-80)
p4.pendown()

#player5
p5 = t.Turtle()
p5.color('white')
p5.shape('turtle')
p5.shapesize(2)
p5.penup()
p5.goto(-170,-140)
p5.pendown()

for i in range(100):
	p1.forward(random.randint(1,5))
	p2.forward(random.randint(1,5))
	p3.forward(random.randint(1,5))
	p4.forward(random.randint(1,5))
	p5.forward(random.randint(1,5))

while True:
	wn.update()