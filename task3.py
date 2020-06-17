from numpy import *
from pylab import *

radius = 100
stepsize = [0, 0.5, 1]
theta = np.pi
steps = list(np.random.choice(stepsize, 10, p=[1/3,1/3,1/3]))
x= radius*np.cos(theta)
y= radius*np.sin(theta)