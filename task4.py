import random
import numpy as np
import matplotlib.pyplot as plt

def randomWalkCont(steps, start_pos):
  position = [start_pos] 
  time = [0]
  for  i in range(steps):
    position.append(position[-1] + random.uniform(0,1))
    time.append(time[-1] + 1)

  dist = position[-1]
  return [time , position, (dist*dist)**0.5 , 0.5*steps]

Randwalk1 = randomWalkCont(25, 0) 
Randwalk2 = randomWalkCont(25, 0)
Randwalk3 = randomWalkCont(25, 0)
Randwalk4 = randomWalkCont(25, 0)
Randwalk5 = randomWalkCont(25, 0)
Randwalk6 = randomWalkCont(25, 0)

plt.plot(Randwalk1[0], Randwalk1[1], '-b') 
plt.plot(Randwalk2[0], Randwalk2[1], '-g') 
plt.plot(Randwalk3[0], Randwalk3[1], '-y') 
plt.plot(Randwalk4[0], Randwalk4[1], '-m') 
plt.plot(Randwalk5[0], Randwalk5[1], '-r') 
plt.plot(Randwalk6[0], Randwalk6[1], '-c') 

plt.xlabel('time (t)')
plt.ylabel('position of the object')
print('Expected distance according to model: ' + str(Randwalk1[3]))
print('Average of the distance covered: '+ str((Randwalk1[2] + Randwalk2[2] + Randwalk3[2] + Randwalk4[2] + Randwalk5[2] + Randwalk6[2])/6))
plt.show()