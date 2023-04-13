import turtle
import random

# screen
turtle.setup(500, 600)
# background color
turtle.bgcolor("black")

# padle1
padle1 = turtle.Turtle()
padle1.goto(0, -250)
padle1.shape("square")
padle1.color("white")
padle1.shapesize( stretch_wid=1, stretch_len=5 )
padle1.penup()
padle1.dx = 0

# padle2
padle2 = turtle.Turtle()
padle2.goto(0, 230)
padle2.shape("square")
padle2.color("white")
padle2.shapesize( stretch_wid=1, stretch_len=5 )
padle2.penup()
padle2.dx = 0

# ball
ball = turtle.Turtle()
ball.goto(0, -5)
ball.shape("circle")
ball.color("red")
ball.penup()

# ball speed range from -10 to -6 and 6 to 10
ball.dx = random.randint(3, 7) * random.choice([-1, 1])
ball.dy = random.randint(3, 7) * random.choice([-1, 1])

# Rules
game_over = False
winner = None
points = {
    'player1': 0,
    'player2': 0
}

game_rules = {
    'max_points': 5,
    'ball_speed': 3,
}

# Score Display
score_display = turtle.Turtle()
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 250)
score_display.write("Player 1: 0  Player 2: 0", align="center", font=("Courier", 24, "normal"))

# function to move padle1
def padle1_left():
    padle1.dx = -10
    padle1.setx(padle1.xcor() + padle1.dx)
    padle1.dx = 0
    
def padle1_right():
    padle1.dx = 10
    padle1.setx(padle1.xcor() + padle1.dx)
    padle1.dx = 0
    
def padle2_left():
    padle2.dx = -10
    padle2.setx(padle2.xcor() + padle2.dx)
    padle2.dx = 0
    
def padle2_right():
    padle2.dx = 10
    padle2.setx(padle2.xcor() + padle2.dx)
    padle2.dx = 0

# keyboard binding

turtle.listen()
turtle.onkeypress(padle1_left, "a")
turtle.onkeypress(padle1_right, "d")
turtle.onkeypress(padle2_left, "Left")
turtle.onkeypress(padle2_right, "Right")

def update_logic():
    padle1.setx(padle1.xcor() + padle1.dx)
    padle2.setx(padle2.xcor() + padle2.dx)

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

def check_collision_ball_paddles():
    if (ball.xcor() > padle1.xcor() - 50 and ball.xcor() < padle1.xcor() + 50) and (ball.ycor() < padle1.ycor() + 20 and ball.ycor() > padle1.ycor() - 20):
        ball.sety(padle1.ycor() + 20)
        ball.dy *= -1.5
    elif (ball.xcor() > padle2.xcor() - 50 and ball.xcor() < padle2.xcor() + 50) and (ball.ycor() < padle2.ycor() + 20 and ball.ycor() > padle2.ycor() - 20):
        ball.sety(padle2.ycor() - 20)
        ball.dy *= -1.5

def update_score():
    score_display.clear()
    score_display.write(f"Player 1: {points['player1']}  Player 2: {points['player2']}", align="center", font=("Courier", 24, "normal"))

def check_collision_ball_offscreen():
    if ball.ycor() > 270:
        ball.goto(0, 0)
        ball.dx = random.randint(3, 7) * random.choice([-1, 1])
        ball.dy = random.randint(3, 7)
        points["player1"] += 1
        update_score()
    elif ball.ycor() < -290:
        ball.goto(0, 0)
        ball.dx = random.randint(3, 7) + random.choice([-1, 1]) 
        ball.dy = random.randint(-7, -3)
        points["player2"] += 1
        update_score()

def check_collision_ball_walls():
    if ball.xcor() > 220:
        ball.setx(220)
        ball.dx *= -1
    elif ball.xcor() < -230:
        ball.setx(-230)
        ball.dx *= -1

def check_game_over():
    if points["player1"] == game_rules["max_points"]:
        game_over = True
        winner = "Player 1"
    elif points["player2"] == game_rules["max_points"]:
        game_over = True
        winner = "Player 2"
    

while not game_over:
    # logic
    update_logic()

    # check for ball collision with the padles
    check_collision_ball_paddles()
    
    # check for ball collision going off screen
    check_collision_ball_offscreen()

    # check for ball collision with the walls
    check_collision_ball_walls()

    # check game over
    if points["player1"] == game_rules["max_points"]:
        game_over = True
        winner = "Player 1"
    elif points["player2"] == game_rules["max_points"]:
        game_over = True
        winner = "Player 2"
        
    
# game over screen
game_over_display = turtle.Turtle()
game_over_display.goto(0, 40)
game_over_display.color("white")
game_over_display.penup()
game_over_display.hideturtle()
game_over_display.write(f"  Game Over! \n{winner} Wins!", align="center", font=("Courier", 24, "normal"))
turtle.done()
