# from turtle import *
import random
import math
import matplotlib.pyplot as plt

def randomWalkOnCircle():
    #choosing a random uniform startposition for two nodes
    r1 = random.uniform(0,100)
    r2 = random.uniform(0,100)
    continous_angle1 = random.uniform(0,360) #in degrees
    continous_angle2 = random.uniform(0,360)
    x1, y1 = r1*math.cos(math.radians(continous_angle1)), r1*math.sin(math.radians(continous_angle1)) #start pos for node1
    x2, y2 = r2*math.cos(math.radians(continous_angle2)), r2*math.sin(math.radians(continous_angle2)) #start pos for node2

    cordx1= []
    cordx2 = []
    cordy1 = []
    cordy2 = []
    steps = 0
    while abs(math.sqrt((x2 - x1)**2 + (y2 - y1)**2)) > 1: #the nodes are within 1 unit distance
        steps +=1
    # saving old cordinates for later use
        old_x1 , old_y1 = x1, y1
        old_x2, old_y2 = x2, y2 
        cordx1.append(x1)
        cordx2.append(x2)
        cordy1.append(y1)
        cordy2.append(y2)

        continous_step1 = random.uniform(0,1)
        continous_angle1 = random.uniform(0,360) #in degrees
        continous_step2 = random.uniform(0,1)
        continous_angle2 = random.uniform(0,360) #in degrees
    # new coordinates for node 1
        new_x1 = x1 + (continous_step1* math.cos(math.radians(continous_angle1)))
        new_y1 =  y1 + (continous_step1* math.sin(math.radians(continous_angle1)))
    #new coordinates for node 2    
        new_x2 = x2 + (continous_step2* math.cos(math.radians(continous_angle2)))
        new_y2 =  y2 + (continous_step2* math.sin(math.radians(continous_angle2)))
    
    # if node1 with in the boundary -> move in random direction
        if (new_x1)**2 + (new_y1)**2 < 100**2:
            x1,y1 = new_x1, new_y1
        else:
        # bounce back / reverse and move in other direction
            x1,y1 = -old_x1, -old_y1       
        # if node2 with in the boundary -> move in random direction
        if (new_x2)**2 + (new_y2)**2 < 100**2:
            x2,y2 = new_x2, new_y2
        else:
        # bounce back / reverse and move in other direction
            x2,y2 = -old_x2, -old_y2
    return [steps, cordx1, cordx2, cordy1, cordy2]

step_arr = []
exp = 0
for i in range(50):
    steps = randomWalkOnCircle()[0]
    step_arr.append(steps)
    exp+=steps
print('The expected number of steps:', exp/50)
print(step_arr)
plt.hist(step_arr)
plt.xlabel('number of steps')
plt.ylabel('frequency')
plt.show()

# r1 = randomWalkOnCircle()
# plt.xlabel('x')
# plt.ylabel('y')
# plt.plot(r1[1], r1[3], '-b')
# plt.plot(r1[2], r1[4], '-g')
# plt.show()

