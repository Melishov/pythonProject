import random
import turtle
condition = True
while condition:
    screen = turtle.Screen()
    GAME_HEIGHT=1000
    GAME_WIDTH=1000
    TARGET_RIGHT_X=random.randint(-450, 450)
    TARGET_TOP_Y=random.randint(-450, 450)
    FORCE_FACTOR=50
    TARGET_WIDTH=50
    ANIMATION_SPEED=1
    NORTH=90
    SOUTH=270
    EAST=0
    WEST=180
    turtle.setup(GAME_HEIGHT,GAME_WIDTH)
    turtle.hideturtle()
    turtle.pencolor("black")
    turtle.speed(0)
    turtle.penup()
    turtle.goto(TARGET_RIGHT_X,TARGET_TOP_Y)
    turtle.pendown()
    turtle.setheading(WEST)
    turtle.forward(TARGET_WIDTH)
    turtle.setheading(SOUTH)
    turtle.forward(TARGET_WIDTH)
    turtle.setheading(EAST)
    turtle.forward(TARGET_WIDTH)
    turtle.setheading(NORTH)
    turtle.forward(TARGET_WIDTH)
    turtle.penup()
    turtle.goto(0,0)
    turtle.showturtle()
    turtle.pendown()
    turtle.setheading(EAST)
    turtle.speed(ANIMATION_SPEED)
    angle=float(turtle.numinput("Угол броска","Введите угол для броска черепахи к цели (0-360):\n"))
    force=int(turtle.numinput("Сила броска","Введите силу броска (1-10):\n"))
    turtle.left(angle)
    force=force*FORCE_FACTOR
    turtle.forward(force)
    targetX=turtle.xcor()
    targetY=turtle.ycor()
    if targetX<TARGET_RIGHT_X and targetX>(TARGET_RIGHT_X-TARGET_WIDTH):
     if targetY<TARGET_TOP_Y and targetY>(TARGET_TOP_Y-TARGET_WIDTH):
         turtle.textinput("Ты попал в цель!","Всё!")
     else:
          looser_answer=turtle.textinput("Ха-ха лузер!","Попробуешь ещё раз?")
          if looser_answer == "Да" or "Да!" or "Ага" or "Ага!":
              condition = False
    else:
     looser_answer=turtle.textinput("Ха-ха лузер!","Попробуешь ещё раз?")
     if looser_answer == "Да" or "Да!" or "Ага" or "Ага!":
           condition = False
    #turtle.done()

