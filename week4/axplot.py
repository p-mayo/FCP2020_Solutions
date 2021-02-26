# axplot.py

import matplotlib.pyplot as plt
import numpy as np

#
# Create a figure (a window)
# Add two subplots in a 1x2 grid (one plot on the left and one on the right)
# ax_left will be the left axes (number 1)
# ax_right will be the right axes (number 2)
#
fig = plt.figure(figsize=(6, 3))
ax_left = fig.add_subplot(1, 2, 1)
ax_right = fig.add_subplot(1, 2, 2)

# x values [0, 0.05, 0.10, ...]
x = np.linspace(0, 15, 300)
sinx = np.sin(xi)
cosx = np.cos(xi)

# Plot sinx on the left
ax_left.plot(x, sinx, color='green', linewidth=3)
ax_left.set_title('Plot of sin(x)')

# Plot cosx on the right
ax_right.plot(x, cosx, color='red', linewidth=3)
ax_right.set_title('Plot of cos(x)')

plt.show()