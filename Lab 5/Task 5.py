import cv2
import matplotlib.pyplot as plt
import imutils


img_rgb = cv2.imread('Island.png')
img_rgb = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2RGB)

img5a = imutils.rotate(img_rgb, 32) # 32 degree
plt.imshow(img5a)

plt.show()