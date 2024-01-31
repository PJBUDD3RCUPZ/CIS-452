#Created By: Kirk Caponpon, Gabe Gonzales, and Benjamin Richards
#Lab 3
#02/04/2024
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np 


mu = 100 
sigma = 10 

x = np.random.randn(1000, 3) * sigma + mu

plt.hist(x, bins= 20, edgecolor= 'black', alpha= 0.75, color=['red', 'green', 'blue'], label=['Red Set', 'Green Set', 'Blue Set'])


plt.grid(True, linestyle='--', alpha=0.5)


plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Task 4')

plt.legend()

plt.show()