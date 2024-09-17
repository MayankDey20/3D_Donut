import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Function to generate the donut shape
def generate_donut(t):
    theta = np.linspace(0, 2 * np.pi, 100)
    phi = np.linspace(0, 2 * np.pi, 100)
    theta, phi = np.meshgrid(theta, phi)

    x = (2 + np.cos(phi)) * np.cos(theta)
    y = (2 + np.cos(phi)) * np.sin(theta)
    z = np.sin(phi)
    
    # Rotate the donut
    x_rot = x * np.cos(t) - z * np.sin(t)
    z_rot = x * np.sin(t) + z * np.cos(t)

    return x_rot, y, z_rot

# Create a figure and 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_zlim(-3, 3)

# Function to update the plot
def update(t):
    ax.clear()
    x, y, z = generate_donut(t)
    ax.plot_surface(x, y, z, color='c', edgecolor='k')
    return fig,

# Create animation
ani = FuncAnimation(fig, update, frames=np.linspace(0, 2 * np.pi, 120), interval=50)

plt.show()
