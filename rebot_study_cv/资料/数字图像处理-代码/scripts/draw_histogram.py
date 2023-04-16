import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def show(img):
    if img.ndim == 2:
        plt.imshow(img, cmap='gray')
    else:
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        plt.imshow(img)
    plt.show()

img = cv.imread("pic/computer200x200.jpg")
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
hist = cv.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
# hist = hist / hist.sum()

hist = np.log(hist + 1)

plt.imshow(hist, interpolation='nearest', cmap='jet')
plt.ylim([0, 180])
plt.xlabel('S')
plt.ylabel('H')
plt.show()


xx = np.arange(0, hist.shape[1])
yy = np.arange(0, hist.shape[0])

xx, yy = np.meshgrid(xx, yy)
fig = plt.figure()
ax = fig.gca(projection='3d')
# ax.bar3d(xx.ravel(), yy.ravel(), hist.ravel(), 1,1,1,cmap='jet')
ax.plot_surface(xx, yy, hist, cmap='jet')
ax.set_xlabel('S')
ax.set_ylabel('H')
plt.show()