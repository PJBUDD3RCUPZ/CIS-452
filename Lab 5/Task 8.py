import cv2
import matplotlib.pyplot as plt
import numpy as py
x6 = cv2.imread('Yellow_traffic_sign.png')
cv2.imshow('x6', x6)
copyImage = x6.copy()


x6 = cv2.cvtColor(x6, cv2.COLOR_BGR2HSV)




lower1 = py.array([20,100,100])
upper1 = py.array([30,255,255])




full_mask = cv2.inRange(x6, lower1, upper1)




copyImage = cv2.bitwise_and(copyImage, copyImage, mask=full_mask)




cv2.imshow('mask', full_mask)
cv2.imshow('result x6', copyImage)




cv2.waitKey(0)
cv2.destroyAllWindows()
