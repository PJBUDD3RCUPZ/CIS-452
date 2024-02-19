import cv2
import matplotlib.pyplot as plt
import numpy as py

x6 = cv2.imread('stopSign.png')
cv2.imshow('x6', x6)
copyImage = x6.copy()


x6 = cv2.cvtColor(x6, cv2.COLOR_BGR2HSV)




lower1 = py.array([0,100,20])
upper1 = py.array([10,255,255])


lower2 = py.array([160,100,20])
upper2 = py.array([179,255,255])






lowermask = cv2.inRange(x6, lower1, upper1)
uppermask = cv2.inRange(x6, lower2, upper2)


full_mask = lowermask + uppermask


copyImage = cv2.bitwise_and(copyImage, copyImage, mask=full_mask)




cv2.imshow('mask', full_mask)
cv2.imshow('result x6', copyImage)




cv2.waitKey(0)
cv2.destroyAllWindows()
