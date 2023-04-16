import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x,y = np.mgrid[-5:5:0.1,-5:5:0.1]
sigma = 2
z = 1/(2 * np.pi * (sigma**2)) * np.exp(-(x**2+y**2)/(2 * sigma**2))


fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap='jet',alpha = 0.9)

plt.show()
