import random
import numpy as np
import matplotlib.pyplot as plt


def randomWalk(start_pos1, start_pos2, prob_arr1, prob_arr2):
    x = 0
    y1 = start_pos1
    y2 = start_pos2
    time = [x]
    positionY1 = [y1]
    positionY2 = [y2]
    while y1 != y2:
        move1 = np.random.choice([1, 0, -1], p=prob_arr1)
        move2 = np.random.choice([1, 0, -1], p=prob_arr2)
        x += 1
        y1 += move1
        y2 += move2        
        time.append(x)
        positionY1.append(y1)
        positionY2.append(y2)
    return [time, positionY1, positionY2]




#simulation1
Randwalk1 = randomWalk(0, 1, [1/3, 1/3, 1/3], [1/3, 1/3, 1/3]) 
#simulation2
#Randwalk2 = randomWalk(5, 10, [1/6, 1/6, 2/3], [2/3, 1/6, 1/6]) 
#fig, (ax1, ax2) = plt.subplots(2)
#subplot1
plt.plot(Randwalk1[0], Randwalk1[1], '-b', label="Person1")
plt.plot(Randwalk1[0], Randwalk1[2], '-g', label="Person2")
#subplot2
# ax2.plot(Randwalk2[0], Randwalk2[1], '-b', label="Person1")
# ax2.plot(Randwalk2[0], Randwalk2[2], '-g', label="Person2")

#ax1.set(ylabel='position of the person')
plt.xlabel=('time (t)')
plt.ylabel=('position of the person')

plt.legend(bbox_to_anchor=(1.005, 1), loc='upper left', borderaxespad=0, fancybox=True)
#ax2.legend(bbox_to_anchor=(1.005, 1), loc='upper left', borderaxespad=0, fancybox=True)
plt.show()

