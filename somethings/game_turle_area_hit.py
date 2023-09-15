import turtle
GAME_HEIGHT=600
GAME_WIDTH=600
TARGET_RIGHT_X=-300
TARGET_TOP_Y=350
FORCE_FACTOR=25
TARGET_WIDTH=25
ANIMATION_SPEED=1
NORTH=90
SOUTH=270
EAST=0
WEST=180
turtle.setup(GAME_HEIGHT,GAME_WIDTH)
turtle.hideturtle()
turtle.speed(0)
turtle.penup()
turtle.goto(TARGET_RIGHT_X,TARGET_TOP_Y)
turtle.setheading(WEST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(SOUTH)
turtle.forward(TARGET_WIDTH)
turtle.setheading(EAST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(NORTH)
turtle.forward(TARGET_WIDTH)
turtle.goto(0,0)
turtle.showturtle()
turtle.pendown()
turtle.setheading(EAST)
turtle.speed(ANIMATION_SPEED)
angle=float(turtle.numinput("Угол броска","Введите угол для броска черепахи к цели (0-360):\n"))
force=int(input("Введите силу броска (1-10):\n"))
190