from turtle import *

#we want to paint a house

#step 1 draw a square
shape("triangle")
speed(30)
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#step 2 drawing a door

forward(70)
color("yellow")
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
#end of the door

penup()
goto(200, 200)
pendown()

#step 3 drawing a roof

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#end of the roof

color("blue")
penup()
goto(30, 200)
pendown()
begin_fill()
left(30)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
penup()
goto(120, 200)
pendown()
right(180)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()



exitonclick()