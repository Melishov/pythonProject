import turtle
upLeftX=-70
upLeftY=200
upRightX=80
upRightY=180
middleRightX=40
middleRightY=20
middleCenterX=0
middleCenterY=0
middleLeftX=-40
middleLeftY=-20
downRightX=120
downRightY=-140
downLeftX=-90
downLeftY=-180
turtle.setup(500,600)
turtle.speed(1)
turtle.bgcolor('black')
turtle.pencolor('white')
turtle.penup()
turtle.setpos(upLeftX,upLeftY)
turtle.dot(10,"yellow")
turtle.write("Бетельгейзе")
turtle.setpos(upRightX,upRightY)
turtle.dot(10,"yellow")
turtle.write("Хатиса")
turtle.setpos(middleRightX,middleRightY)
turtle.dot(10,"yellow")
turtle.write("Минтака")
turtle.setpos(middleCenterX,middleCenterY)
turtle.dot(10,"yellow")
turtle.write("Альнилам")
turtle.setpos(middleLeftX,middleLeftY)
turtle.dot(10,"yellow")
turtle.write("Альнитак")
turtle.setpos(downLeftX,downLeftY)
turtle.dot(10,"yellow")
turtle.write("Саиф")
turtle.setpos(downRightX,downRightY)
turtle.dot(10,"yellow")
turtle.write("Ригель")
turtle.pendown()
turtle.pencolor('yellow')
turtle.pensize(3)
turtle.goto(middleRightX,middleRightY)
turtle.setpos(upRightX,upRightY)
turtle.setpos(middleRightX,middleRightY)
turtle.setpos(middleCenterX,middleCenterY)
turtle.setpos(middleLeftX,middleLeftY)
turtle.setpos(upLeftX,upLeftY)
turtle.setpos(middleLeftX,middleLeftY)
turtle.setpos(downLeftX,downLeftY)
turtle.done()


