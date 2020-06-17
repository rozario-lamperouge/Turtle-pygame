# importing the turtle module
import turtle

# initializing my window 
wn = turtle.Screen()

# creating a palyer object
player = turtle.Turtle()

# giving color to the player
player.color("black","red")
player.begin_fill()

# function to draw a sqaure:
def square():
	player.forward(100)
	player.right(90)
	player.forward(100)
	player.right(90)
	player.forward(100)
	player.right(90)
	player.forward(100)
	player.right(90)

	player.penup()
	player.forward(100)
	player.pendown()

# function to draw a triangle
def triangle():
	player.forward(100)
	player.right(120)
	player.forward(100)
	player.right(120)
	player.forward(100)

	player.penup()
	player.right(120)
	player.forward(150)
	player.pendown()

# function to draw a rectangle
def Rectangle():
	player.forward(100)
	player.right(90)
	player.forward(50)
	player.right(90)
	player.forward(100)
	player.right(90)
	player.forward(50)
	player.right(90)

	player.penup()
	player.forward(100)
	player.pendown()

# function to draw a design
def design():
	while True:
		player.left(135)
		player.forward(100)
		player.left(100)
		player.forward(100)

# listening to my keyboard inputs
wn.listen()

# calling seperate functions based on my keyboard inputs
wn.onkeypress(square,"s")
wn.onkeypress(Rectangle,"r")
wn.onkeypress(triangle,'t')
wn.onkeypress(design,'d')


# player.end_fill()

turtle.done()