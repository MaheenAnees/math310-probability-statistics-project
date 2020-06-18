# import random
# import turtle
# import math
# import numpy as np
# import matplotlib.pyplot as plt


# random.seed(None) # Seed generator, None => system clock
# jmax = 1000
# x = 0.; y = 0. # Start at origin

# x_axis = []
# y_axis = []
# for i in range(0, jmax + 1):
#   #turtle.setpos(x,y)
#   x_axis.append(x)
#   y_axis.append(y) # Plot points
#   theta = 2.*math.pi*random.random()# 0 =< angle =< 2 pi
#   x += math.cos(theta) # -1 =< x =< 1
#   x_axis.append(x)
#   y += math.sin(theta) # -1 =< y =< 1
#   y_axis.append(y) 
#   #turtle.setpos(x,y)

# plt.plot(x_axis, y_axis)
# plt.show()
#   #rate(100)
# print("This walk's distance R = ", math.sqrt(x*x + y*y))
