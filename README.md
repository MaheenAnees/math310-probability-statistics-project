# MATH 310 Probability and Statistics: Final Project

## Overview
The purpose of this project is to generate and model random variables' probability mass and density functions through simulations using data analysis tools of python (matplotlib, numpy, pandas).

## Task Descriptions
### Task 1: discrete random variables
A one-dimensional random walk mathematical and simulation-based model to predict the expected distance from the starting point. Model was tested for range of scenarios e.g. starting position, (un)equal probabilities of moving left, right, and not moving at all. 

### Task 2: discrete random variables
A one-dimensional random walk mathematical and simulation-based model where two people start $x$ units away from each other and are traversing the grid with some probabilities. The expected time it takes to meet them is predicted and model was tested for a range of scenarios.

### Task 3: discrete random variables
A two-dimensional random walk model using simulation-based approach. The two-dimensional region in $\mathbb R^2$ is a circular region of radius 100 units (1 unit can be 1 cm or 1 meter, or 1 km). The two dimensional circular space is referred as a disc, _d(0, R)_. A node or nodes within a circular region _d(0, R)_ at time _t_, undertakes a random walk whose next position at the fixed discrete time _t+1_ unit time is modeled as follows:
- Step size is a discrete random variable. You can assume that step size is between {0, 0.5, 1}.
- Orientation is a discrete random variable between \[0 - 2 &pi\].

For example: a node at the center of a 100-unit radius circle will take a random step of size _r_ between {0, 0.5, 1} and a direction with angle &theta. To begin with, its assumed that all step sizes and angles are equally likely. 

Over the next course of time slots the node will traverse a random path based on the random walk model described above. Of course, at some point in time, it is quite likely that after many units of time, the node might try to leave the 100-unit circular region. Hence, for its re-entry model, to ensure that the node does not escape the test region, we have used the concept of 3D traversal to implement it, by imagining a 2D circle in 3D space(as a sphere). A node colliding with the boundary of the 2D circle can be imagined as a point moving from one hemisphere to another of a sphere, coming from the opposite coordinates into the first hemisphere on completion of one rotation. The trajectory of the node starting from the origin with the re-entry model was then demonstrated and assessed.  

### Task 4: Continuous random variables
Repeated task 1 by assuming that the step size is a continuous uniform random variable between _0 - 1_. The PDF is modelled as a uniform random variable.

### Task 5: Continuous random variables
Repeated task 3 by assuming that the step size and the orientation are continuous random variables between _0-1_ and _0 - 2 &pi_. The PDF is modelled as a uniform random variable.

### Task 6: Continuous random variables
Repeated task 3 by assuming that the step size and the orientation are continuous random variables between _0 - 1_ and _0 - 2 &pi_.

### Task 7: Continuous random variables
Repeated task 3 by assuming that the step size is a discrete random variable and the orientation is a continuous random variables between _0 - 2&pi_. 

### Task 8
Building on task 5, this task captures the trajectory of two nodes whose initial locations are chosen randomly and uniformly over a circular region. It also determines the average number of steps taken by the two nodes so that they are within 1 unit (distance between the two nodes _< 1_ unit distance) by running multiple simulations.

## Team Members
- Arhum Ishtiaq
- Maheen Anees
