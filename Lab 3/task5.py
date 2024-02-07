#Created By: Kirk Caponpon, Gabe Gonzales, and Benjamin Richards
#Lab 3
#02/04/2024
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np 
import pandas as pd

#saving this as dataframe "df"
df = pd.read_csv("BostonHousing.csv")

#use seaborn to draw boxplot of "dis"
sns.boxplot(x=df['dis'])

plt.xlabel('Distance')
plt.title('Boxplot')
plt.title('Task 5')
plt.show()