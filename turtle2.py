import turtle

t = turtle.Turtle()

def up():
    t.forward(100)

def left():
    t.left(30)

def right():
    t.right(30)

def down():
    turtle.bye()

turtle.onkey(up,'Up')
turtle.onkey(left,'Left')
turtle.onkey(right,'Right')
turtle.onkey(down,'Down')

turtle.listen()
turtle.mainloop()
