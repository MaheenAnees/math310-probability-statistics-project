import random
import numpy as np
import matplotlib.pyplot as plt


def randomWalk(steps, start_pos, prob_arr):
    x = 0
    y = start_pos
    time = [x]
    position = [y]
    Z = [-1, 1, 0]
    move = np.random.choice(Z, steps, p=prob_arr)

    for i in move:
        x += 1
        y += i
        time.append(x)
        position.append(y) 
    exp = Z[0]*prob_arr[0] + Z[1]*prob_arr[1] + Z[2]*prob_arr[2]  
    expDist = exp*steps 
    Dist = np.sum(move)
    return [time, position, ((expDist**2)**0.5), ((Dist**2)**0.5)]



#equal prob same start position
Randwalk1a = randomWalk(25, 0, [1/3, 1/3, 1/3])
Randwalk1b = randomWalk(25, 0, [1/3, 1/3, 1/3])
Randwalk1c = randomWalk(25, 0, [1/3, 1/3, 1/3])
Randwalk1d = randomWalk(25, 0, [1/3, 1/3, 1/3])
Randwalk1e = randomWalk(25, 0, [1/3, 1/3, 1/3])
Randwalk1f = randomWalk(25, 0, [1/3, 1/3, 1/3])
#equal prob diff start position
Randwalk2a = randomWalk(25, 2, [1/3, 1/3, 1/3])
Randwalk2b = randomWalk(25, 2, [1/3, 1/3, 1/3])
Randwalk2c = randomWalk(25, 2, [1/3, 1/3, 1/3])
Randwalk2d = randomWalk(25, 2, [1/3, 1/3, 1/3])
Randwalk2e = randomWalk(25, 2, [1/3, 1/3, 1/3])
Randwalk2f = randomWalk(25, 2, [1/3, 1/3, 1/3])
#unequal prob same start position
Randwalk3a = randomWalk(25, 0, [0.3, 0.5, 0.2])
Randwalk3b = randomWalk(25, 0, [0.3, 0.5, 0.2])
Randwalk3c = randomWalk(25, 0, [0.3, 0.5, 0.2])
Randwalk3d = randomWalk(25, 0, [0.3, 0.5, 0.2])
Randwalk3e = randomWalk(25, 0, [0.3, 0.5, 0.2])
Randwalk3f = randomWalk(25, 0, [0.3, 0.5, 0.2])
#unequal prob diff start position
Randwalk4a = randomWalk(25, 2, [0.3, 0.5, 0.2])
Randwalk4b = randomWalk(25, 2, [0.3, 0.5, 0.2])
Randwalk4c = randomWalk(25, 2, [0.3, 0.5, 0.2])
Randwalk4d = randomWalk(25, 2, [0.3, 0.5, 0.2])
Randwalk4e = randomWalk(25, 2, [0.3, 0.5, 0.2])
Randwalk4f = randomWalk(25, 2, [0.3, 0.5, 0.2])

plt.figure()

plt.subplot(221)
plt.plot(Randwalk1a[0], Randwalk1a[1], '-g')
plt.plot(Randwalk1b[0], Randwalk1b[1], '-m')
plt.plot(Randwalk1c[0], Randwalk1c[1], '-b')
plt.plot(Randwalk1d[0], Randwalk1d[1], '-r')
plt.plot(Randwalk1e[0], Randwalk1e[1], '-y')
plt.plot(Randwalk1f[0], Randwalk1f[1], '-k')
plt.xlabel('time (t)')
plt.ylabel('position of the object')

plt.subplot(222)
plt.plot(Randwalk2a[0], Randwalk2a[1], '-g')
plt.plot(Randwalk2b[0], Randwalk2b[1], '-m')
plt.plot(Randwalk2c[0], Randwalk2c[1], '-b')
plt.plot(Randwalk2d[0], Randwalk2d[1], '-r')
plt.plot(Randwalk2e[0], Randwalk2e[1], '-y')
plt.plot(Randwalk2f[0], Randwalk2f[1], '-k')
plt.xlabel('time (t)')
plt.ylabel('position of the object')

plt.subplot(223)
plt.plot(Randwalk3a[0], Randwalk3a[1], '-g')
plt.plot(Randwalk3b[0], Randwalk3b[1], '-m')
plt.plot(Randwalk3c[0], Randwalk3c[1], '-b')
plt.plot(Randwalk3d[0], Randwalk3d[1], '-r')
plt.plot(Randwalk3e[0], Randwalk3e[1], '-y')
plt.plot(Randwalk3f[0], Randwalk3f[1], '-k')
plt.xlabel('time (t)')
plt.ylabel('position of the object')

plt.subplot(224)
plt.plot(Randwalk4a[0], Randwalk4a[1], '-g')
plt.plot(Randwalk4b[0], Randwalk4b[1], '-m')
plt.plot(Randwalk4c[0], Randwalk4c[1], '-b')
plt.plot(Randwalk4d[0], Randwalk4d[1], '-r')
plt.plot(Randwalk4e[0], Randwalk4e[1], '-y')
plt.plot(Randwalk4f[0], Randwalk4f[1], '-k')
plt.xlabel('time (t)')
plt.ylabel('position of the object')


# plt.title("1D Random Walks-Discrete Model")
print('For plot top-left')
print('Expected distance according to model: ' + str(Randwalk1a[2]))
print('Average of the distance covered: '+ str((Randwalk1a[3] + Randwalk1b[3] + Randwalk1c[3] + Randwalk1d[3] + Randwalk1e[3] + Randwalk1f[3])/6))
print('-----------------------------------------------------------------')
print('For plot top-right')
print('Expected distance according to model: ' + str(Randwalk2a[2]))
print('Average of the distance covered: '+ str((Randwalk2a[3] + Randwalk2b[3] + Randwalk2c[3] + Randwalk2d[3] + Randwalk2e[3] + Randwalk2f[3])/6))
print('-----------------------------------------------------------------')
print('For plot bottom-left')
print('Expected distance according to model: ' + str(Randwalk3a[2]))
print('Average of the distance covered: '+ str((Randwalk3a[3] + Randwalk3b[3] + Randwalk3c[3] + Randwalk3d[3] + Randwalk3e[3] + Randwalk3f[3])/6))
print('-----------------------------------------------------------------')
print('For plot bottom-right')
print('Expected distance according to model: ' + str(Randwalk4a[2]))
print('Average of the distance covered: '+ str((Randwalk4a[3] + Randwalk4b[3] + Randwalk4c[3] + Randwalk4d[3] + Randwalk4e[3] + Randwalk4f[3])/6))


plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25, wspace=0.35)
plt.show()
