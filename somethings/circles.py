import turtle
#Переменные:
COUNT_CIRCLES=22
STARTING_RADIUS=20
OFFSET=15
SPEED=0
STARTING_RADIUS
#Настройка черепахи:
turtle.hideturtle
turtle.speed(SPEED)
#Начало
radius=STARTING_RADIUS
y=OFFSET*-1
for circles in range(COUNT_CIRCLES):
    turtle.pendown()
    turtle.circle(radius)
    turtle.penup()
    turtle.goto(0,y)
    y-=OFFSET
    radius+=OFFSET
turtle.done()