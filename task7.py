from turtle import *
import random
import math
import matplotlib.pyplot as plt

def randomWalkOnCircle():
  # Screen
    window = Screen ()
    window.setup(350, 400)
    window.title("Project Task 07")

    # Circle boundary 
    T1 = Turtle()
    T1.hideturtle()
    T1.speed(1)
    T1.penup()
    T1.setpos(0,-100)
    T1.pendown()
    T1.pen(fillcolor="Black", pencolor="Black", pensize=2)
    T1.circle(100)
    T1.penup()
    
    # Moving pointer
    T2 = Turtle()
    T2.speed(0)
    T2.penup()
    cordx = []
    cordy = []
    n = 0

  # Random moves generator
    while n < 3000:
        T2.pendown()
        T2.color("blue")
    
    # current position
        x,y = T2.position() # xcor, ycor
        cordx.append(x)
        cordy.append(y)
        n+=1
    # saving old cordinates for later use
        old_x , old_y = x, y 
        discrete_steps = random.choice([0, 0.5, 1])
        continous_angle = random.uniform(0,360) #in degrees
    # new coordinates 
        new_x = x + (discrete_steps* math.cos(math.radians(continous_angle)))
        new_y =  y + (discrete_steps* math.sin(math.radians(continous_angle)))
    # if with in the boundary -> move in random direction
        if (new_x)**2 + (new_y)**2 < 100**2:
            T2.setheading(continous_angle)
        #T2.goto(new_x, new_y)
            x,y = new_x, new_y
            T2.goto(x,y)
        else:
        # bounce back / reverse and move in other direction
        # T2.setheading(continous_angle)
            T2.penup()
            x,y = -old_x, -old_y
            T2.goto(x,y)
            T2.pendown()
    return [cordx, cordy]

r1 = randomWalkOnCircle()
plt.plot(r1[0], r1[1])
plt.xlabel('x')
plt.ylabel('y')
plt.show()
randomWalkOnCircle()