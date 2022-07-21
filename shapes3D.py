import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d  # in this code it is not required

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
u, v = np.ogrid[0:2*np.pi:20j, 0:1.5*np.pi:10j]
x = np.cos(u)*np.sin(v)
y = np.sin(u)*np.sin(v)
z = np.cos(v)
c=x+y
ax.plot_wireframe(x, y, z, color="rgb")
ax.set_title("Sphere")
plt.show()