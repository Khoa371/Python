import math
from turtle import *

# Define the equations for the x and y coordinates of the heart shape
def heart_x(k):
    return 19 * math.sin(k) ** 3

def heart_y(k):
    return 16 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)

# Set up the drawing environment
speed(1)
bgcolor("black")
color("red")

# Move the turtle to the starting position
penup()
goto(heart_x(0) * 15, heart_y(0) * 15)
pendown()

# Draw the heart shape
for i in range(360):
    x = heart_x(math.radians(i))
    y = heart_y(math.radians(i))
    goto(x * 15, y * 15)

# Return to the starting position
goto(heart_x(0) * 15, heart_y(0) * 15)

# Start filling the shape
begin_fill()

# Draw the heart shape for filling
for i in range(360):
    x = heart_x(math.radians(i))
    y = heart_y(math.radians(i))
    goto(x * 15, y * 15)

# End filling the shape
end_fill()

# Move the turtle to the center of the heart
penup()
goto(0, 30)  # Center of the heart shape
pendown()

done()  # This keeps the window open after drawing is done
