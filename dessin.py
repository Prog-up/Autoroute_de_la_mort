# -*- coding: utf-8 -*-
#======================================================================
# dessin.py		  	Prog_up 2021-03-30
#
#dessin turtles
#======================================================================

from turtle import *
up()
def voiture(couleur = "grey"):
    down()
    begin_fill()
    fillcolor(couleur)
    forward(50)
    left(34)
    forward(18)
    left(56)
    forward(65)
    left(32)
    forward(47)
    left(58)
    forward(30)
    left(58)
    forward(47)
    left(32)
    forward(65)
    left(56)
    forward(18)
    left(124)
    end_fill()
    up()
    forward(70)
    down()
    begin_fill()
    fillcolor("#87CEEB")
    right(27)
    forward(22)
    right(63)
    forward(30)
    right(63)
    forward(22)
    right(117)
    forward(50)
    end_fill()
    left(113)
    fillcolor("black")
    begin_fill()
    forward(59)
    left(67)
    forward(7)
    left(70)
    forward(59)
    left(110)
    forward(50)
    end_fill()
    up()
    right(60)
    forward(18)
    right(30)
    down()
    begin_fill()
    forward(15)
    right(90)
    forward(11)
    right(123)
    forward(20)
    left(57)
    end_fill()
    up()
    left(67)
    forward(68)
    left(90)
    down()
    begin_fill()
    forward(17)
    left(90)
    forward(12)
    left(123)
    forward(20)
    end_fill()
    up()
    hideturtle()

def rectangle():
    down()
    pencolor("white")
    width(20)
    begin_fill()
    fillcolor("grey")
    for _ in range (2) :
        forward(400)
        left(90)
        forward(350)
        left(90)
    pencolor("black")
    end_fill()
    up()

def game_over(t):
    goto(172,-200)
    setheading(90)
    rectangle()
    goto(-60,0)
    down()
    style1 = ('Arial', 30, 'italic')
    write('Score :' , font = style1)
    up()
    goto(-30,-50)
    down()
    write(t, font = style1)
    up()
    goto(-135, 50)
    style2 = ("Arial", 40)
    write("Game Over", font = style2)
