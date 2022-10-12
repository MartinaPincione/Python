# Python Pong Using Functional Programming

import turtle
import time

wn = turtle.Screen() #creating window
wn.title("Python Pong!")
wn.bgcolor("green") #changing background color of window
wn.setup(width = 800, height = 600) #in pixels, with (0,0) at the center
wn.tracer(0) #stops the window from updating and requires us to manually update it 

title_screen = turtle.Turtle()
title_screen.speed(0)
title_screen.color("red")
title_screen.penup()
title_screen.hideturtle()
title_screen.goto(0,0)
title_screen.write("Welcome to Python Pong!", align = "center", font = ("Times New Roman", 50, "normal"))

time.sleep(5)

title_screen.clear()


# Paddle L
paddle_l = turtle.Turtle()
paddle_l.speed(0) 
paddle_l.shape("square")
paddle_l.color("orange")
paddle_l.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_l.penup()
paddle_l.goto(-350, 0)


# Paddle R
paddle_r = turtle.Turtle()
paddle_r.speed(0) 
paddle_r.shape("square")
paddle_r.color("orange")
paddle_r.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_r.penup()
paddle_r.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0) 
ball.shape("circle")
ball.color("white")
ball.shapesize()
ball.penup()
ball.goto(0, 0)
ball.dx = 1.5 #every time x moves its displacement is 1.5
ball.dy = 1.5

# Score Var
score_l = 0
score_r = 0


# Score Board
pen = turtle.Turtle()
pen.speed(0)
pen.color("red")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Player L: 0   Player R: 0", align = "center", font = ("Times New Roman", 25, "normal")) #default score



# Moves Paddle Left
def paddle_l_up():
    y = paddle_l.ycor() #the current y coordinate of the left paddle
    y += 17
    paddle_l.sety(y) #yets the y coordinate of the left paddle to the new y

def paddle_l_down():
    y = paddle_l.ycor() #the current y coordinate of the left paddle
    y -= 17
    paddle_l.sety(y) #yets the y coordinate of the left paddle to the new y

# Moves Paddle Right
def paddle_r_up():
    y = paddle_r.ycor() #the current y coordinate of the right paddle
    y += 17
    paddle_r.sety(y) #yets the y coordinate of the right paddle to the new y

def paddle_r_down():
    y = paddle_r.ycor() #the current y coordinate of the right paddle
    y -= 17
    paddle_r.sety(y) #yets the y coordinate of the right paddle to the new y

# Keyboard Binding
wn.listen() #listen for keyboard input
wn.onkeypress(paddle_l_up, "w") #executes the following function with the lowercase w press
wn.onkeypress(paddle_l_down, "s") 
wn.onkeypress(paddle_r_up, "Up") #executes the following function with the up arrow
wn.onkeypress(paddle_r_down, "Down") 



#main game loop
while True:
    wn.update()

    # Move the Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border 
    if (ball.ycor() > 290):
        ball.sety(290)
        ball.dy *= -1 #reverses the direction of the ball's movement

    if (ball.xcor() > 390):
        score_l += 1
        ball.goto(0, 0)
        ball.dx *= -1
        pen.clear() #clears what is on the screen so it doesn't write over itself
        pen.write("Player L: {}   Player R: {}".format(score_l, score_r), align = "center", font = ("Times New Roman", 25, "normal")) #default score



    if (ball.ycor() < -290):
        ball.sety(-290)
        ball.dy *= -1

    if (ball.xcor() < -390):
        score_r += 1
        ball.goto(0, 0)
        ball.dx *= -1
        pen.clear() #clears what is on the screen so it doesn't write over itself
        pen.write("Player L: {}   Player R: {}".format(score_l, score_r), align = "center", font = ("Times New Roman", 25, "normal")) #default score


    # Ball hits Paddles
    if (ball.xcor() > 340 and (ball.ycor() < paddle_r.ycor() + 50) and (ball.ycor() > paddle_r.ycor() - 50)): #the width is 50 pixels from center
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and (ball.ycor() < paddle_l.ycor() + 50) and (ball.ycor() > paddle_l.ycor() - 50)):
        ball.setx(-340)
        ball.dx *= -1


    


    
        

