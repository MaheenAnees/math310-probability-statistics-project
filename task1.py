import random
import numpy as np
import matplotlib.pyplot as plt


def randomWalk(steps, start_pos, prob_arr):
    x = 0
    y = start_pos
    time = [x]
    position = [y]

    for i in range(0, steps):
        move = np.random.choice(['L', 'R', 'S'], p=prob_arr)
        if move == 'R':
            x += 1
            y += 1
        elif move == 'L':
            x += 1
            y += -1
        else:
            x += 1
            y = y
        time.append(x)
        position.append(y)    
    return [time, position]




Randwalk1 = randomWalk(25, 0, [1/3, 1/3, 1/3])  # equally likely
Randwalk2 = randomWalk(25, 0, [2/3, 1/6, 1/6]) # probability of moving left is 2x
Randwalk3 = randomWalk(25, 0, [1/6, 2/3, 1/6]) # probability of moving right is 2x
Randwalk4 = randomWalk(25, 0, [1/2, 1/2, 0]) # the node always moves either left or right
Randwalk5 = randomWalk(25, 0, [0.2, 0.5, 0.3]) 
Randwalk6 = randomWalk(25, 2, [1/3, 1/3, 1/3]) # same as randwalk1 but diff start pos
Randwalk7 = randomWalk(25, 3, [2/3, 1/6, 1/6]) # same as randwalk2 but diff start pos
Randwalk8 = randomWalk(25, -1, [1/6, 2/3, 1/6]) # same as randwalk3 but diff start pos
Randwalk9 = randomWalk(25, 10, [1/2, 1/2, 0]) # same as randwalk4 but diff start pos
Randwalk10 = randomWalk(25, -5, [0.2, 0.5, 0.3]) # same as randwalk5 but diff start pos


plt.plot(Randwalk1[0], Randwalk1[1], '-g', label="Randwalk1")
plt.plot(Randwalk2[0], Randwalk2[1], '-b', label="Randwalk2")
plt.plot(Randwalk3[0], Randwalk3[1], '-y', label="Randwalk3")
plt.plot(Randwalk4[0], Randwalk4[1], '-k', label="Randwalk4")
plt.plot(Randwalk5[0], Randwalk5[1], '-c', label="Randwalk5")
plt.plot(Randwalk6[0], Randwalk6[1], '-m', label="Randwalk6")
plt.plot(Randwalk7[0], Randwalk7[1], '-r', label="Randwalk7")
plt.plot(Randwalk8[0], Randwalk8[1], '--g', label="Randwalk8")
plt.plot(Randwalk9[0], Randwalk9[1], '--r', label="Randwalk9")
plt.plot(Randwalk10[0], Randwalk10[1], '--y', label="Randwalk10")


plt.title("1D Random Walks")
plt.grid(True, color='k')
plt.xlabel('time (t)')
plt.ylabel('position of the object')
plt.legend(bbox_to_anchor=(1.005, 1), loc='upper left', borderaxespad=0, fancybox=True)
plt.show()
