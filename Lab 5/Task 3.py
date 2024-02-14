import cv2
import matplotlib.pyplot as plt

# Read the RGB image
img_rgb = cv2.imread('Island.png')
img_rgb = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2RGB)

# Apply transformations
img3a = cv2.rotate(img_rgb, cv2.ROTATE_90_CLOCKWISE)
img3b = cv2.rotate(img_rgb, cv2.ROTATE_180)
img3c = cv2.rotate(img_rgb, cv2.ROTATE_90_COUNTERCLOCKWISE)
img3d = cv2.resize(img_rgb, (600, 480))

# Display all four images
plt.figure(figsize=(12, 12))

plt.subplot(1, 4, 1)
plt.imshow(img3a)
plt.title('ROTATE_90_CLOCKWISE')


plt.subplot(1, 4, 2)
plt.imshow(img3b)
plt.title('ROTATE_180')


plt.subplot(1, 4, 3)
plt.imshow(img3c)
plt.title('ROTATE_90_COUNTERCLOCKWISE')


plt.subplot(1, 4, 4)
plt.imshow(img3d)
plt.title('Resize to 600x480')


plt.show()
