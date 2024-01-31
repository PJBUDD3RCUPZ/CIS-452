import matplotlib.pyplot as plt
import seaborn as sns


x = [1,2,3,4]
y = [1,4,9,16]


plt.xlim(0,6)
plt.ylim(0,20)


plt.scatter(x, y, color='red', marker='s')

plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Task 1")

plt.show()