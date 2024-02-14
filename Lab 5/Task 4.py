import cv2
import matplotlib.pyplot as plt

img_rgb = cv2.imread('Island.png')
img_rgb = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2RGB)


sizex, sizey, _ = img_rgb.shape

# Crop a portion of the image
img4a = img_rgb[int(sizex*0.25):int(sizex*0.75), int(sizey*0.25):int(sizey*0.75)]

plt.imshow(img4a)

plt.show()
