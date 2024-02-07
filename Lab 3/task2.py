#Created By: Kirk Caponpon, Gabe Gonzales, and Benjamin Richards
#Lab 3
#02/04/2024
import matplotlib.pyplot as plt
import seaborn as sns


x = [0,1,2,3,4,5]
y = [0,1,2,3,4,5]

X1Curve = [0,1,2,3,4,5]
Y1Curve = [val**2 for val in X1Curve]


X2Curve = [0,1,2,3,4,5]
Y2Curve = [val**3 for val in X2Curve]


plt.plot(x, y, 'r--', label='Straight Line')  
plt.scatter(X1Curve, Y1Curve, color='blue', marker='o', label='Curve 1')  
plt.scatter(X2Curve, Y2Curve, color='green', marker='^', label='Curve 2')  


plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Task 2")

plt.show()