import turtle
import math
import random

#screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Shooters")

#draw border
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.setposition(-300,-300)
pen.pensize(3)
pen.pendown()
for i in range(4):
	pen.fd(600)
	pen.lt(90)
pen.hideturtle()

#player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.goto(0,-250)
player.setheading(90)

playerspeed = 15

#create the enemy
enimies = []

def CreateEnimies():
	global enimies, enemyspeed
	enemy = turtle.Turtle()
	enemy.color("red")
	enemy.shape("circle")
	enemy.penup()
	enemy.speed(0)
	enemy.goto(random.randint(-200,200),200)
	enimies.append(enemy)

	enemyspeed = 2

# create the player bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 20

#define bullet state
#ready - ready to fire
#fire - bullet is firing
bulletstate = "ready"

#move player:
def move_left():
	x = player.xcor()
	x = x - 15
	if x < -280:
		x = -280
	player.setx(x)

def move_right():
	x = player.xcor()
	x = x + 15
	if x > 280:
		x = 280
	player.setx(x)

def fire_bullet():
	global bulletstate
	if bulletstate == "ready":
		bulletstate = "fire"

		#move the bullet abouve the player
		x = player.xcor()
		y = player.ycor()  + 10
		bullet.goto(x,y)
		bullet.showturtle()

def isCollision(t1, t2):
	distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
	if distance < 20:
		return True
	else:
		return False

wn.listen()
wn.onkeypress(move_left,'Left')
wn.onkeypress(move_right,'Right')
wn.onkeypress(fire_bullet,'Return')

CreateEnimies()
CreateEnimies()
CreateEnimies()

while True:
	wn.update()

	for enemy in enimies:
		# move the enemy
		x = enemy.xcor()
		x = x + enemyspeed
		enemy.setx(x)
		#move the enemy back and down
		if enemy.xcor() > 280:
			y = enemy.ycor()
			y = y - 40
			enemyspeed = enemyspeed * -1
			enemy.sety(y)

		if enemy.xcor() < -280:
			y = enemy.ycor()
			y = y - 40
			enemyspeed = enemyspeed * -1
			enemy.sety(y)

		#move the bullet
		if bulletstate == "fire":
			y = bullet.ycor()
			y = y + bulletspeed
			bullet.sety(y)

		#check to see if bullet has gone to top
		if bullet.ycor() > 275:
			bullet.hideturtle()
			bulletstate = "ready"

		#check for collision between the bullet and enemy
		if isCollision(bullet, enemy):
			#reset the bullet
			bullet.hideturtle()
			bulletstate = "ready"
			bullet.setposition(0, -400)
			#reset the enemy
			enemy.setposition(-200, 250)

		if isCollision(player, enemy):
			player.hideturtle()
			enemy.hideturtle()
			print("Game Over")
			break

