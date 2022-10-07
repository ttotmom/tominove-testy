import turtle
from turtle import Screen
import math
import time
import random

#def healthbars():






def canvas():
    screen=turtle.Screen()
    screen.setup(width=300,height=100)
    screen.screensize(bg=("black"))




def PlayerHP():
    plyer = turtle.Turtle(shape="square", visible=False)
    plyer.color('green')
    plyer.pensize("25")
    plyer.shape("square")
    plyer.penup()
    plyer.goto(-150,25)
    plyer.pendown()
    plyer.goto(10,25)




def EasyHP():
    easy = turtle.Turtle(shape="square", visible=False)
    easy.color('red')
    easy.pensize("25")
    easy.shape("square")
    easy.penup()
    easy.goto(-150,-16)
    easy.pendown()
    easy.goto(-30,-16)




def MediumHP():
    medium = turtle.Turtle(shape="square", visible=False)
    medium.color('red')
    medium.pensize("25")
    medium.shape("square")
    medium.penup()
    medium.goto(-150,-16)
    medium.pendown()
    medium.goto(10,-16)




def HardHP():
    hard = turtle.Turtle(shape="square", visible=False)
    hard.color('red')
    hard.pensize("25")
    hard.shape("square")
    hard.penup()
    hard.goto(-150,-16)
    hard.pendown()
    hard.goto(60,-16)




def EasyDMG(widthdmg):
    plyer_loss = turtle.Turtle(shape="square", visible=False)
    plyer_loss.color('black')
    plyer_loss.pensize("25")
    plyer_loss.shape("square")
    plyer_loss.penup()
    plyer_loss.goto(widthdmg,25)
    plyer_loss.pendown()




def PlayerDMG(ewidthdmg):
    easy_loss = turtle.Turtle(shape="square", visible=False)
    easy_loss.color('black')
    easy_loss.pensize("25")
    easy_loss.shape("square")
    easy_loss.penup()
    easy_loss.goto(ewidthdmg,-16)
    easy_loss.pendown()











