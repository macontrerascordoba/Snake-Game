import turtle
import time
import random


# Initializers
delay = 0.1
score = 0
high_score = 0
segments = []




# Creating the screen
wn = turtle.Screen()
wn.title("Snake")
wn.bgcolor("black")

wn.setup(width=700, height=700)
wn.tracer(0)




# Grid
grid = turtle.Turtle()
grid.speed(0)
grid.shape("square")
grid.color("gray10")
grid.hideturtle()
grid.penup()

gridY = 280

i = 0

while gridY >= -280:
    if i % 2 == 0:
        gridX = -280

    else:
        gridX = -260

    
    while gridX <= 280:
        grid.goto(gridX, gridY)
        grid.stamp()
        gridX += 40

    gridY -= 20
    i += 1




# Walls
aux = turtle.Turtle()
aux.speed(0)
aux.shape("square")
aux.color("white")
aux.pensize(1)
aux.hideturtle()

aux.penup()
aux.goto(-290, 290)
aux.pendown()
aux.goto(-290, -290)

aux.penup()
aux.goto(290, 290)
aux.pendown()
aux.goto(290, -290)

aux.penup()
aux.goto(-290, -290)
aux.pendown()
aux.goto(290, -290)

aux.penup()
aux.goto(-290, 290)
aux.pendown()
aux.goto(290, 290)




# Snake's head
head = turtle.Turtle()
head.shape("square")
head.color("chartreuse")
head.penup()
head.goto(0,0)
head.direction = "Stop"




# Snake's food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()

def checkFoodPlacement():

    safe = False

    while safe == False:

        foodX = random.randrange(-260, 260, 20)
        foodY = random.randrange(-260, 260, 20)

        safe = True

        if head.xcor() == foodX and head.ycor() == foodY:
            safe = False

        if len(segments) > 0:
            for segment in segments:
                if segment.xcor() == foodX and segment.ycor() == foodY:
                    safe = False

        print(foodX, " ", foodY)

    return foodX, foodY

foodX, foodY = checkFoodPlacement()

food.goto(foodX,foodY)




# Scoreboard
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,305)
pen.write("Score: 0     High Score: 0", 
            align="center", font=("candara", 20, "bold"))




#GameOver / Winner
pen_gameover = turtle.Turtle()
pen_gameover.speed(0)
pen_gameover.shape("square")
pen_gameover.color("white")
pen_gameover.penup()
pen_gameover.hideturtle()
pen_gameover.goto(0,0)




# Movement
def goup():
    if head.direction != "down":
        head.direction = "up"

def godown():
    if head.direction != "up":
        head.direction = "down"

def goleft():
    if head.direction != "right":
        head.direction = "left"

def goright():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    elif head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    elif head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    elif head.direction == "right":
        x = head.xcor()
        head.setx(x+20)




# Movement listener
wn.listen()
wn.onkeypress(goup, "w")
wn.onkeypress(godown, "s")
wn.onkeypress(goleft, "a")
wn.onkeypress(goright, "d")



#   Game Over text
def lose():
    pen.clear()
    head.hideturtle()
    food.hideturtle()

    for segment in segments:
        segment.goto(1000,1000)

    segments.clear()

    wn.update()

    pen_gameover.write("GAME OVER", align="center", font=("candara", 50, "bold"))
    time.sleep(1)
    pen_gameover.clear()

    head.goto(0,0)
    head.direction = "Stop"

    head.showturtle()

    foodX, foodY = checkFoodPlacement()
    food.goto(foodX,foodY)
    food.showturtle()

    wn.update()

    score = 0
    delay = 0.1

    pen.write("Score: {}     High Score: {}".format(score, high_score), 
                align="center", font=("candara", 20, "bold"))

    return score, delay




#You Win text
def win():
    pen.clear()
    head.hideturtle()
    food.hideturtle()

    for segment in segments:
        segment.goto(1000,1000)

    segments.clear()

    wn.update()

    pen_gameover.write("YOU WIN", align="center", font=("candara", 50, "bold"))
    time.sleep(1)
    pen_gameover.clear()

    head.goto(0,0)
    head.direction = "Stop"

    head.showturtle()

    foodX, foodY = checkFoodPlacement()
    food.goto(foodX,foodY)
    food.showturtle()

    wn.update()

    score = 0
    delay = 0.1

    pen.write("Score: {}     High Score: {}".format(score, high_score), 
                align="center", font=("candara", 20, "bold"))

    return score, delay





# Main gameplay loop
while True:
    wn.update()

    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        # If collision with borders, reset everything
        score, delay = lose()


    if head.distance(food) < 20:
        #if head collision with food, +10 points +1 segment
        foodX, foodY = checkFoodPlacement()
        food.goto(foodX,foodY)
        
        score += 10
        if score > high_score:
            high_score = score

        #adding new segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("DarkGreen")
        new_segment.penup()
        segments.append(new_segment)

        delay -= 0.001

        pen.clear()
        pen.write("Score: {}     High Score: {}".format(score, high_score), 
                    align="center", font=("candara", 20, "bold"))

    #segments movement
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()

        segments[index].goto(x,y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()

        segments[0].goto(x,y)
    
    move()

    for segment in segments:
        #if collision with segments, reset everything
        if head.distance(segment) < 20:
            score, dealy = lose()

    if score == 1000:
        score, delay = win()

    time.sleep(delay)