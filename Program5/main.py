# Importing Libraries
import pandas as pd
import matplotlib.pyplot as plt

# Loading dataset as data frame
df = pd.read_csv('USPopDatav3.csv')

# population of United States and Texas
data = df[df['States'].isin(['United States','Texas'])]

# Extracting population of United States and Texas
data = df[df['States'].isin(['United States','Texas'])].T.drop(index=['States']) 
data.columns=['United States','Texas']

# Adding column, 'Pop_Change' to the data frame
data['Pop_Change'] = data['Texas']/data['United States']

# LINE PLOT
plt.figure(figsize=(10,7))
plt.title('Line Plot: Texas Population Change', fontsize=17)
plt.xlabel('Year', fontsize=15)
plt.ylabel('Population Change', fontsize=15)
plt.plot(data['Pop_Change'])
plt.show()

# HISTOGRAM
plt.figure(figsize=(10,7))
plt.title('Histogram: Texas Population Change', fontsize=17)
plt.xlabel('Population Change', fontsize=15)
plt.ylabel('Frequency', fontsize=15)
plt.hist(data['Pop_Change'])
plt.show()

# BAR GRAPH
plt.figure(figsize=(10,7))
plt.title('Bar graph: Texas Population Change', fontsize=17)
plt.xlabel('Year', fontsize=15)
plt.ylabel('Population Change', fontsize=15)
plt.bar(data.index, data['Pop_Change'])
plt.show()

# HORIZONTAL BAR GRAPH
plt.figure(figsize=(10,7))
plt.title('Horizontal Bargraph: Texas Population Change', fontsize=17)
plt.xlabel('Population Change', fontsize=15)
plt.ylabel('Year', fontsize=15)
plt.barh(data.index, data['Pop_Change'])
plt.show()
