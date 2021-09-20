#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 15:02:31 2021

@author: campbellmahan

 """
# creating a simple line image using turtle
# wanted a blue sky with a big cloud to add perspective
# balloons floating away into the sky
# envokes a emotion that reminds me of my childhood
# ballons change color each run to utilize the random library
# fun light hearted image that displays my programming skills

import turtle
import random

turtle.colormode(255)
# rgb values and light blue to protray as the sky
panel = turtle.Screen().bgcolor('light blue')

cloud = turtle.Turtle()
# turtle named cloud to keep everything diffrent shape/turtle organized
cloud.color("white")
cloud.forward(150)
# simple 4 point circle for loop to create the shape of a cloud
for x in range (0,4):
    cloud.begin_fill()
    cloud.forward(100)
    cloud.circle(150)
    cloud.left(90)
    cloud.end_fill()
 

balloon = turtle.Turtle()
# turtle named after the balloons being drawn in image
colors = [(255,0,0), (255,140,0), (255,255,0), (127,255,0), (186,85,211)]
randomcolor = random.choice(colors)
# random library used to change the color of the balloons everytime the code is run
# creates a different color but similar image each and everytime

balloon.up()
balloon.right(180)
balloon.forward(200)
balloon.right(180)
balloon.down()
# for loop used to create 2 balloon shapes in image
for x in range (0, 2):
    balloon.begin_fill()
    balloon.pencolor(randomcolor)
    balloon.fillcolor(randomcolor)
    balloon.circle(80)
    balloon.down()
    balloon.end_fill()
    balloon.up()
    balloon.forward(300)
    balloon.left(90)

string = turtle.Turtle()
# another turtle named to create orangization throughout code
string.up()
string.forward(20)
string.right(90)
string.forward(80)
string.down()
string.forward(200)
string.right(90)
string.up()
string.forward(230)
string.right(90)
string.down()
string.forward(290)
string.up()

turtle.done()
# all done!
