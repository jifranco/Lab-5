import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
ax = plt.axes(projection='3d')
x = np.linspace(-1, 1, 30)
y = np.linspace(-1, 1, 30) 
X, Y = np.meshgrid(x, y)           # make a mesh, a 2D array, and assign 2D arrays to X and Y
a,b = 0.5, 1
Z = X*X/a - Y*Y/b                  # make a 2D array and assign it to Z
ax.contour3D(X, Y, Z, 50)
ax.set_title('Hyperbolic Paraboloid')
plt.show()

#Circle
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# Make data
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = 10 * np.outer(np.cos(u), np.sin(v))
y = 10 * np.outer(np.sin(u), np.sin(v))
z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))

# Plot the surface
ax.plot_surface(x, y, z)

plt.show()

#Square Pyramid
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# vertices of a pyramid
v = np.array([[-1, -1, -1], [1, -1, -1], [1, 1, -1],  [-1, 1, -1], [0, 0, 1]])
ax.scatter3D(v[:, 0], v[:, 1], v[:, 2])

verts = [ [v[0],v[1],v[4]], [v[0],v[3],v[4]],
 [v[2],v[1],v[4]], [v[2],v[3],v[4]], [v[0],v[1],v[2],v[3]]]

ax.add_collection3d(Poly3DCollection(verts, 
 facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))

plt.show()


#Cone
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

# Set up the grid in polar
theta = np.linspace(0,2*np.pi,90)
r = np.linspace(0,3,50)
T, R = np.meshgrid(theta, r)

# Then calculate X, Y, and Z
X = R * np.cos(T)
Y = R * np.sin(T)
Z = (np.sqrt(X**2 + Y**2) - 1)*-1
print("z1:"+repr(Z)+"\nz2"+repr(np.sqrt(X**2 + Y**2) - 1))
# Set the Z values outside your range to NaNs so they aren't plotted
Z[Z < 0] = np.nan
Z[Z > 2.1] = np.nan
ax.plot_surface(X, Y, Z,  rstride=4, cstride=4, color='b')

ax.set_zlim(0,2)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()