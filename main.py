# 1. import the graphic module
import turtle
import os
# lets us interact with the os for the sound imports

# 2. creating a window
wn = turtle.Screen()
wn.title('Pong')
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0)  # stops the window from updating = speeding the game

# 4. paddle a - left
paddle_a = turtle.Turtle()  # module name . class name
paddle_a.speed(0)  # speed of animation - it's set to the max
paddle_a.shape('square')
paddle_a.color('white')
paddle_a.shapesize(stretch_wid=5, stretch_len=1)  # 20 pixels is the default size
paddle_a.penup()  # so it does not draw a line on it's pattern
paddle_a.goto(-350, 0)  # coordinates of the starting point - x / y

# paddle b - right
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(+350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball.dx = 2     # dx / dy = delta / change - up / down by 2 pixels
ball.dy = 2

# 9. creating the scoreboard via turtle
score_a = 0
score_b = 0
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f'Player A: {score_a}  Player B: {score_b}', align='center', font=('Courier', 24, 'normal'))


# 5. functions for movement
def paddle_a_up():
    y = paddle_a.ycor()  # for the movement we need to know the y coordinate (ycor is from turtle)
    y += 20  # 20 pixels to the y coordinate
    paddle_a.sety(y)  # setting the new y as the current


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# 6. keyboard binding
wn.listen()  # turtle listens for keyboard inputs
wn.onkeypress(paddle_a_up, 'w')
wn.onkeypress(paddle_a_down, 's')
wn.onkeypress(paddle_b_up, 'Up')    # up / down arrows
wn.onkeypress(paddle_b_down, 'Down')

# 3. Main game loop - the core of the game
while True:
    wn.update()  # every time the loop runs it updates the screen

    # 7. moving the ball
    ball.setx(ball.xcor() + ball.dx)    # starts at 0 0 and then goes 2 + 2 - this depends on the computer speed
    ball.sety(ball.ycor() + ball.dy)

    # 8. create borders:
    # top / bottom
    if ball.ycor() > 290:   # since the height from the middle is the window height / 2 and the ball is 20 pixels
        ball.sety(290)
        ball.dy *= -1   # reverses the direction of the ball => dy = -2
        # 10. creating the sound effects with the help of the os module
        os.system('afplay wall_hit.mp3&')   # the & sign makes it so the game doesn't freeze while the sound is played
        # for linux - aplay
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system('afplay wall_hit.mp3&')

    # left / right
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f'Player A: {score_a}  Player B: {score_b}', align='center', font=('Courier', 24, 'normal'))
        os.system('afplay point.mp3&')

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f'Player A: {score_a}  Player B: {score_b}', align='center', font=('Courier', 24, 'normal'))
        os.system('afplay point.mp3&')

    # paddle - ball collision
    if (340 < ball.xcor() < 350) and (paddle_b.ycor() + 40 > ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1.03
        os.system('afplay paddle.mp3&')

    if (-340 > ball.xcor() > -350) and (paddle_a.ycor() + 40 > ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1.03
        os.system('afplay paddle.mp3&')
