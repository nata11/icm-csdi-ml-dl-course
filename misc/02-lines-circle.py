# %%
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Setup figure and axis
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)
polygon_line, = ax.plot([], [], 'b-', lw=2)
circle_line, = ax.plot([], [], 'r--', lw=1, alpha=0.5)

# Initialize function
def init():
    polygon_line.set_data([], [])
    theta = np.linspace(0, 2 * np.pi, 500)
    circle_line.set_data(np.cos(theta), np.sin(theta))
    return polygon_line, circle_line

# Update function
def update(frame):
    n = frame + 3  # Start from triangle (3 sides)
    theta = np.linspace(0, 2 * np.pi, n + 1)
    x = np.cos(theta)
    y = np.sin(theta)
    polygon_line.set_data(x, y)
    return polygon_line,

# Number of frames: from triangle to 100-gon
ani = FuncAnimation(fig, update, frames=97, init_func=init,
                    blit=True, interval=100, repeat=True)

plt.title("Polygon with Increasing Sides Approximating a Circle")
plt.show()



