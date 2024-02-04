#Created By: Kirk Caponpon, Gabe Gonzales, and Benjamin Richards
#Lab 3
#02/04/2024
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np 


mu = 100 
sigma = 10 

x = np.random.randn(1000) * sigma + mu

plt.hist(x, bins= 20, edgecolor= 'black', alpha= 0.75)


plt.grid(True, linestyle='--', alpha=0.5)

# Add labels and title
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Task 3')

# Display the plot
plt.show()
