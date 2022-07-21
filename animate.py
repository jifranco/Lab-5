import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

pi = 2*np.pi

fig, axes = plt.subplots()
t = np.arange(0.0, pi, 0.001)
s = np.sin(t)
l = plt.plot(t, s)

ax = plt.axis([0,pi,-1,1])

redDot, = plt.plot([0], [np.sin(0)], 'ro')

def animate(i):
    redDot.set_data(i, np.sin(i))
    return redDot,

# create animation using the animate() function
myAnimation = FuncAnimation(fig, animate, frames=np.arange(0.0, pi, 0.1), \
interval=10, blit=True, repeat=True)
plt.show()