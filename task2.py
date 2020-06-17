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




#simulation1
Person1a = randomWalk(360, 0, [1/3, 1/3, 1/3]) 
Person2a = randomWalk(360, 10, [1/3, 1/3, 1/3])
#simulation2
Person1b = randomWalk(360, 5, [1/6, 2/3, 1/6]) 
Person2b = randomWalk(360, 10, [1/3, 1/3, 1/3])

fig, (ax1, ax2) = plt.subplots(2)

#subplot1
ax1.plot(Person1a[0], Person1a[1], '-b', label="Person1")
ax1.plot(Person2a[0], Person2a[1], '-g', label="Person2")
#subplot2
ax2.plot(Person1b[0], Person1b[1], '-b', label="Person1")
ax2.plot(Person2b[0], Person2b[1], '-g', label="Person2")

ax1.set(ylabel='position of the person')
ax2.set(xlabel='time (t)', ylabel='position of the person')

ax1.legend(bbox_to_anchor=(1.005, 1), loc='upper left', borderaxespad=0, fancybox=True)
ax2.legend(bbox_to_anchor=(1.005, 1), loc='upper left', borderaxespad=0, fancybox=True)
plt.show()

