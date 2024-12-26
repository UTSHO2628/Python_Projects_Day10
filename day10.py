# Happy Birthday
from turtle import *
import random

# Set up the screen
bgcolor("light blue")
title("Happy Birthday!")
pensize(3)

# Function to draw a rectangle (Cake layer)
def draw_rectangle(width, height, color):
    fillcolor(color)
    begin_fill()
    for _ in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)
    end_fill()

# Function to draw the cake
def draw_cake():
    # Bottom layer
    penup()
    goto(-100, -100)
    pendown()
    draw_rectangle(200, 50, "chocolate")

    # Middle layer
    penup()
    goto(-80, -50)
    pendown()
    draw_rectangle(160, 40, "pink")

    # Top layer
    penup()
    goto(-60, -10)
    pendown()
    draw_rectangle(120, 30, "light yellow")

# Function to draw candles
def draw_candles():
    for i in range(-50, 60, 25):
        penup()
        goto(i, 20)
        pendown()
        pencolor("blue")
        fillcolor("blue")
        begin_fill()
        forward(10)
        left(90)
        forward(40)
        left(90)
        forward(10)
        left(90)
        forward(40)
        left(90)
        end_fill()

        # Flame
        penup()
        goto(i + 5, 60)
        pendown()
        pencolor("orange")
        fillcolor("orange")
        begin_fill()
        circle(5)
        end_fill()

# Function to draw balloons
def draw_balloons():
    colors = ["red", "green", "blue", "yellow", "purple"]
    for _ in range(5):
        x = random.randint(-200, 200)
        y = random.randint(50, 200)
        penup()
        goto(x, y)
        pendown()
        pencolor(random.choice(colors))
        fillcolor(random.choice(colors))
        begin_fill()
        circle(20)
        end_fill()
        # String
        penup()
        goto(x, y - 20)
        pendown()
        pencolor("black")
        right(90)
        forward(50)
        left(90)

# Function to write "Happy Birthday"
def write_message():
    penup()
    goto(-150, -200)
    pendown()
    pencolor("dark blue")
    style = ("Arial", 24, "bold")
    write("Happy Birthday!", font=style, align="center")

# Draw the cake
draw_cake()

# Add candles
draw_candles()

# Add balloons
draw_balloons()

# Write the message
write_message()

hideturtle()
done()
