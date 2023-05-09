from turtle import *
import time
import random

maxlives = 3
livesUsed = 0
bombTemplate = Turtle()
tommy = Turtle()
left = False
right = False

def ldown():
    global left
    left=True

def lup():
    global left
    left=False

def rdown():
    global right
    right=True

def rup():
    global right
    right=False

def initialise():
    global level
    level = 1

    global bombcount
    bombcount = 0

    text = Turtle()
    text.hideturtle()

    tommy.hideturtle()

    bombTemplate.hideturtle()

    bombTemplate.shape("circle")
    bombTemplate.color("red")

    bombTemplate.penup()

    tommy.shape("square")
    tommy.color("blue")

    tommy.penup()
    tommy.goto(0, -100)

    s = Screen()
    s.listen()

    s.onkeypress(ldown,'Left')
    s.onkey(lup, 'Left')
    s.onkeypress(rdown, 'Right')
    s.onkey(rup, 'Right')


def welcome():
    DisplayText("Dodge the bombs!")

def showLifeInfo(lives_left):
    tommy.hideturtle()
    DisplayText(f"You have {lives_left} lives left")
    tommy.showturtle()

def show_game_over():
    DisplayText("Game Over!")

def DisplayText(message):
    text = Turtle()
    text.hideturtle()
    text.write(message, None, "center", ("Courier", 15, "bold"))
    time.sleep(2)
    text.clear()

def MoveBombs(bombs):
    for bomb in bombs:
        bomb.goto(bomb.xcor(), bomb.ycor()-10)

def playGameLife():
    dead = False
    bombs = []
    while not dead:
        dead = CheckIfDied(bombs)
        CheckCreateBomb(bombs)
        MoveBombs(bombs)
        MoveTommy()

def CheckIfDied(bombs):
    for bomb in bombs:
      y_collide = check_collision(tommy.ycor(), bomb.ycor())
      if y_collide:
        x_collide = check_collision(tommy.xcor(), bomb.xcor())
        if x_collide:
            bomb.hideturtle()
            return True
    
    return False

def CheckCreateBomb(bombs):
    createNewBomb = len(bombs) == 0
    for bomb in bombs:
            if bomb.ycor() < tommy.ycor():
                createNewBomb = True
                bomb.hideturtle()
                bombs.remove(bomb)

    if createNewBomb:
        newBomb = bombTemplate.clone()
        x = random.randint(-150, 150)
        y = 150  
        newBomb.goto(x, y)
        newBomb.showturtle()
        bombs.append(newBomb)

def MoveTommy():
    if left:
        tommy.backward(10)
    if right:
        tommy.forward(10)

def check_collision(yourCoordVal, bombCoordVal):
    diff = yourCoordVal - bombCoordVal
                
    if diff < 0:
        diff = diff * -1
                
    if diff <= 21:
        return True
                
    return False

def game():
    initialise()
    welcome()

    for l in range(1, maxlives+1):
        showLifeInfo(maxlives-l+1)
        playGameLife()

    show_game_over()

game()