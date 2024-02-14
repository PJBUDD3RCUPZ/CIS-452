import cv2
import matplotlib.pyplot as plt

# Read the BGR image
img_bgr = cv2.imread('Island.png')

# Convert BGR image to grayscale
img_bgr_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

# Convert RGB image to grayscale
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
img_rgb_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)



plt.subplot(1, 2, 1)
plt.imshow(img_bgr_gray, cmap='gray')
plt.title('img_bgr_gray')


plt.subplot(1, 2, 2)
plt.imshow(img_rgb_gray, cmap='gray')
plt.title('img_rgb_gray')

plt.show()

# Save the grayscale images
cv2.imwrite('img_bgr_gray.png', img_bgr_gray)
cv2.imwrite('img_rgb_gray.png', img_rgb_gray)

# Additional checks
t = cv2.imread('img_bgr_gray.png')
print("BGR Gray Image Shape:", t.shape)

s = cv2.imread('img_rgb_gray.png', 0)
print("RGB Gray Image Shape:", s.shape)

# Display one of the grayscale images using OpenCV
cv2.imshow('gray', img_bgr_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
