import turtle

zolw = turtle.Turtle()
#zolw.speed(0)
turtle.bgcolor('lightgray')
#zolw.shape('turtle')
kolory = ['white','red','blue','green','yellow','black']
def kwadrat(bok, kolor):
    zolw.color(kolor)
    for i in range(4):
        zolw.left(90)
        zolw.forward(bok)
    zolw.home()

def pentagram(bok):
    zolw.fillcolor('red')
    zolw.color('red')
    zolw.begin_fill()
    for i in range(5):
        zolw.forward(bok)
        zolw.right(180-36)
    zolw.end_fill()
    zolw.hideturtle()

def szesciokat(bok):
    for i in range(6):
        zolw.forward(bok)
        zolw.right(60)
        zolw.hideturtle()

def siatka_heksagonalna(bok):
    zolw.get
    for j in range(5):
        for i in range(10):
            szesciokat(bok)
            zolw.penup()
            zolw.forward(bok*3)
            zolw.pendown()
        zolw.penup()
        zolw
kat = 0
kolor = 0
'''
while kat<360:
    zolw.left(kat)
    kwadrat(200,kolory[kolor])
    kolor += 1
    if kolor > 5:
        kolor = 0
    kat += 0.5
'''
#pentagram(300)
zolw.penup()
zolw.backward(300)
zolw.pendown()
siatka_heksagonalna(20)
turtle.exitonclick()