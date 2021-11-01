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
# Bureau ComparisonData to display how the population of Texas        #
# (relative to the total population of the US) changed      #
# between 2010 and 2019. Note: you will be using a plot     #
# (line, histogram, bar, barh).  When I say "relative to",  #
# you should divide the TX pop by the US pop each year.     #
# You may want to compute that first.  Turn in your python  #
# code and the display of the plot                          #
#===========================================================#


# import pandas for the dataframe to read the dataframe
# and matplotlib to be used in the creation of the graph plots
import pandas as pd
import matplotlib.pyplot as plt

# read in the csv data file and assign it to DataFrame
DataFrame = pd.read_csv('USPopDatav3.csv')
# to see the head of the d
print(DataFrame.head())
# the population of united states and texas
ComparisonData = DataFrame[DataFrame['States'].isin(['United States','Texas'])]
print(ComparisonData)

# extract the population of united states and texas
ComparisonData = DataFrame[DataFrame['States'].isin(['United States','Texas'])].T.drop(index=['States']) 
ComparisonData.columns=['United States','Texas']

# create a new collum called Populationchange to store the compares
# values of the Texas divide by the united States
ComparisonData['PopulationChange'] = ComparisonData['Texas']/ComparisonData['United States']

# Plot and display the line graph
plt.figure(figsize=(10,7))
# creating a title for the line plot graph
plt.title('Line Plot: Texas Population Change', fontsize=17)
# create the x and y labels for the line graph
plt.xlabel('Year', fontsize=15)
plt.ylabel('Population Change', fontsize=15)
# plot on the line the population change
plt.plot(ComparisonData['PopulationChange'])
# display the graph
plt.show()

# plot and display the histograpm graph
plt.figure(figsize=(10,7))
# create a head title for the graph
plt.title('Histogram: Texas Population Change', fontsize=17)
# labelling the x and y 
plt.xlabel('Population Change', fontsize=15)
plt.ylabel('Frequency', fontsize=15)
# plotting the population change data
plt.hist(ComparisonData['PopulationChange'])
# display the graph
plt.show()

# plot and display the bargraph
plt.figure(figsize=(10,7))
# creating a title for bar graph 
plt.title('Bar graph: Texas Population Change', fontsize=17)
# labelling the x and y axis for user readability and comprehension
plt.xlabel('Year', fontsize=15)
plt.ylabel('Population Change', fontsize=15)
# plotting the data to be displayed in the graph
plt.bar(ComparisonData.index, ComparisonData['PopulationChange'])
# plot the graph and show it
plt.show()

# create and dispkay the bar histogram graph barh()
plt.figure(figsize=(10,7))
# create the head for graph 
plt.title('Horizontal Bargraph: Texas Population Change', fontsize=17)
# label the x and y axis for user understanding
plt.xlabel('Population Change', fontsize=15)
plt.ylabel('Year', fontsize=15)
# what is being displaued in the graph population change
plt.barh(ComparisonData.index, ComparisonData['PopulationChange'])
# plot and display the graph
plt.show()
