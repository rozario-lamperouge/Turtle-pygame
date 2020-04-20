import turtle
import time

# create the window
wn = turtle.Screen()
wn.title("Ping Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

score_a = 0
score_b = 0

# paddle 1
paddle1 = turtle.Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.shapesize(stretch_wid=5,stretch_len=1)
paddle1.color("red")
paddle1.penup()
paddle1.goto(-350,0)

# paddle 2
paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.shapesize(stretch_wid=5,stretch_len=1)
paddle2.color("blue")
paddle2.penup()
paddle2.goto(350,0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("yellow")
ball.penup()
ball.goto(0,0)
ball.dx = 2
ball.dy = 2

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  ||  Player B:0", align ="center", font=("Courier",24,"normal"))

def paddle1_up():
	y = paddle1.ycor()
	y = y + 20
	paddle1.sety(y)

def paddle1_down():
	y = paddle1.ycor()
	y = y - 20
	paddle1.sety(y)

def paddle2_up():
	y = paddle2.ycor()
	y = y + 20
	paddle2.sety(y)

def paddle2_down():
	y = paddle2.ycor()
	y = y - 20
	paddle2.sety(y)

wn.listen()
wn.onkeypress(paddle1_up,'w')
wn.onkeypress(paddle1_down,'s')
wn.onkeypress(paddle2_up,'Up')
wn.onkeypress(paddle2_down,'Down')

while True:
	wn.update()
	# moving the balls
	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)
	time.sleep(0.01)

	# Border checking
	if ball.ycor() > 290:
		ball.sety(290)
		ball.dy = ball.dy * -1

	if ball.ycor() < -290:
		ball.sety(-290)
		ball.dy = ball.dy * -1

	if ball.xcor() > 390:
		ball.goto(0,0)
		pen.clear()
		score_a = score_a + 1
		pen.write("Player A: {}  ||  Player B:{}".format(score_a,score_b), align ="center", font=("Courier",24,"normal"))
		ball.dx = ball.dx * -1

	if ball.xcor() < -390:
		ball.goto(0,0)
		pen.clear()
		score_b = score_b + 1
		pen.write("Player A: {}  ||  Player B:{}".format(score_a,score_b), align ="center", font=("Courier",24,"normal"))
		ball.dx = ball.dx * -1

	if(ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle2.ycor() + 50 and ball.ycor() > paddle2.ycor() - 50):
		ball.setx(340)
		ball.dx = ball.dx * -1

	if(ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle1.ycor() + 50 and ball.ycor() > paddle1.ycor() - 50):
		ball.setx(-340)
		ball.dx = ball.dx * -1
