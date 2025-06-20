import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create data
X = np.linspace(-5, 5, 100)
Y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(X, Y)
Z = np.sin(np.sqrt(X**2 + Y**2))

# 1. 3D Line Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
z_line = np.linspace(0, 15, 100)
x_line = np.sin(z_line)
y_line = np.cos(z_line)
ax.plot3D(x_line, y_line, z_line, 'green')
ax.set_title("3D Line Plot")
plt.show()

# 2. 3D Scatter Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x_scatter = np.random.rand(100)
y_scatter = np.random.rand(100)
z_scatter = np.random.rand(100)
ax.scatter(x_scatter, y_scatter, z_scatter, c=z_scatter, cmap='viridis')
ax.set_title("3D Scatter Plot")
plt.show()

# 3. 3D Surface Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='plasma')
ax.set_title("3D Surface Plot")
plt.show()

# 4. 3D Wireframe Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(X, Y, Z, color='blue')
ax.set_title("3D Wireframe Plot")
plt.show()

# 5. 3D Bar Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
_x = np.arange(4)
_y = np.arange(3)
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()
top = np.random.rand(len(x))
bottom = np.zeros_like(top)
width = depth = 1
ax.bar3d(x, y, bottom, width, depth, top, shade=True)
ax.set_title("3D Bar Plot")
plt.show()

# 6. 3D Contour Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.contour3D(X, Y, Z, 50, cmap='coolwarm')
ax.set_title("3D Contour Plot")
plt.show()
