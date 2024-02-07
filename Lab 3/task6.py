#Created By: Kirk Caponpon, Gabe Gonzales, and Benjamin Richards
#Lab 3
#02/04/2024
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np 
import pandas as pd


df = pd.read_csv("BostonHousing.csv")
newdf = pd.melt(df, var_name = 'var', value_name = 'val')

sns.boxplot(data = newdf, x='var', y = 'val')

plt.xlabel('Distance')
plt.title('Boxplot')
plt.title('Task 6')
plt.show()