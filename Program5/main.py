#===========================================================#
# Author     : Ethan Coyle                                  #
# Teacher    : Dr. StringFellow                             #
# Class      : CMPS 4553/5443 Computational Methods         #
# Assignment : Program 5 Displaying a graph Texas nad US    #
#===========================================================#
# What this program does-                                   #
#                                                           #
# Use the file below USPopDatav3.csv for the following      #
# project.Write a python program that uses the US Census    #
# Bureau data to display how the population of Texas        #
# (relative to the total population of the US) changed      #
# between 2010 and 2019. Note: you will be using a plot     #
# (line, histogram, bar, barh).  When I say "relative to",  #
# you should divide the TX pop by the US pop each year.     #
# You may want to compute that first.  Turn in your python  #
# code and the display of the plot                          #
#===========================================================#


# Importing Libraries
import pandas as pd
import matplotlib.pyplot as plt

# Loading dataset as data frame
df = pd.read_csv('USPopDatav3.csv')
print(df.columns)

# population of United States and Texas
data = df[df['States'].isin(['United States', 'Texas'])]
data = data.get(["States"])


# Extracting population of United States and Texas
data = df[df['States'].isin(['United States', 'Texas'])].T.drop(index=['States'])
data.columns = ['United States', 'Texas']

# Adding column, 'Pop_Change' to the data frame
data['Pop_Change'] = (data['Texas'] / data['United States'])
data['Pop_Change'] = data['Pop_Change']*100
# LINE PLOT
plt.figure(figsize=(10, 5))
plt.title('Line Plot: Texas Population Change', fontsize=17)
# create the label for the x
plt.xlabel('Year', fontsize=15, color='red')
plt.ylabel('Population Change', fontsize=15)
plt.plot(data['Pop_Change'], color='cyan')
plt.show()

# HISTOGRAM
plt.figure(figsize=(10, 5))
plt.title('Histogram: Texas Population Change', fontsize=17)
plt.xlabel('Population Change', fontsize=15)
plt.ylabel('Frequency', fontsize=15)
plt.hist(data['Pop_Change'])
plt.show()

# BAR GRAPH
plt.figure(figsize=(10, 5))
plt.title('Bar graph: Texas Population Change', fontsize=17)
plt.xlabel('Year', fontsize=15)
plt.ylabel('Population Change', fontsize=15)
plt.bar(data.index, data['Pop_Change'])
plt.show()

# HORIZONTAL BAR GRAPH
plt.figure(figsize=(10, 5))
plt.title('Horizontal Bargraph: Texas Population Change', fontsize=17)
plt.xlabel('Population Change', fontsize=15)
plt.ylabel('Year', fontsize=15)
plt.barh(data.index, data['Pop_Change'])
plt.show()
