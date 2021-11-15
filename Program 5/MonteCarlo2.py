#================================================#
#                                                #
# Author- Ethan Coyle                            #
# Inst-   Dr. StringFellow                       #
# Class - CMPS 4553 Computational Methods        #
# Prog  - Program 5 part 2                       #
#                                                #
# in this program, we are implementing the       #
# following equations  using matplotlib  to plot #
# and guestimate the  value of the alotte        #
# equations compared against the actual value and#
# plot the scatter dots and the actual line of   #
# the curve                                      #
#================================================#
# The equations computed are stated below        #
#                                                #
# 1. (x+1)^-1                                    #
# 2. x^4                                         #
# 3. X^2                                         #
#================================================#



from random import random as rand
import numpy as np
import matplotlib, matplotlib.pyplot as plt

#number of random points to Generate
#initialize count of points inside
#select good looking plot sorted
matplotlib.style.use("ggplot")


# creating axis guidelines and a placeholder
# for subplotting so can hold multiple plots
# in one graph
plt.axis([0, 5, 0, 10])
figure, axis = plt.subplots(2,2)
N=5000 # number of points to test

# function definition for the x^2 IntegraValueral
def FunctionOne(a, b):
    # analytical solution to IntegraValueral of f(x)
    return (1/3)*(b**3-a**3)
# create function definition for x^4 IntegraValueral
def FunctionThree(a,b):
  return (1/5)*(b**5-a**5)

def FirstEquation(x):
    # function f(x)=np.log(1+x) IntegraValueral
    return (x+1)**-1
# function definition for x**2
def SecondEquation(x):
    return x**2
# function definition for x^4
def ThirdEquation(x):
    return x**4

# when called, call the corresponding Function
# that holds equation and the upper and lower bound values
# and the number of points in this case is 5000
def FindValue(func, a, b, N):
    vals = np.random.uniform(a, b, N)
    y = [func(val) for val in vals]
    # assign the sum of all the values and assign it to meanof values/ number of points
    MeanofValues = np.sum(y)/N
    #then find the integral value and then return the 
    # integral value
    IntegraValue = (b-a) * MeanofValues
    return IntegraValue  


# now that all the definitions are done calculate the
# different equations

# first testing case 
# calculate the actual value and the value with 5000
# points then plot on the coressponding axis subgraph
print("\r\nTesing Case for (x+1)**-1")
print("====================================" )
print(f"Our Computed Solution is : {FindValue(FirstEquation, 0, 2, 5000): .4f}")
print ("The Actual Value is      : ",1.099)
# for our subplots
# create title for easier find
axis[0, 0].set_title("((x+1)**-1)")
#plot the random numbers in graph
xlist = np.empty((0, 0))
ylist = np.empty((0, 0))
for i in range (N):
    x= rand()
    y= rand()
    y_value= x**2-y+1
  #print(" y value is : ", y)
    xlist = np.append(xlist, x)
    ylist = np.append(ylist, y)
axis[0, 0].scatter(xlist, ylist, s=2)

# plot the equation on the graph
f2 = np.empty((0,0))
x2 = np.linspace(0, 1, 100)
for x in x2:
  f2 = np.append (f2, FirstEquation(x))
# plotting the actual graph
# plot the x^2 equation
axis[0, 0].plot(x2, f2,  color='b') 




# next testing case
print("\r\nTesing Case for (x^2)")
print("====================================" )
print(f"Our Computed Solution is : {FindValue(SecondEquation, 0, 2, 5000): .4f}")
print(f"Actual solution is       : {FunctionOne(0, 2): .4f}")

# for our subplots
axis[0, 1].set_title("(x^2)")
#plot the random numbers in graph
#create empty list an append the list 
# with x and y value so can plot scatter points
xlist = np.empty((0, 0))
ylist = np.empty((0, 0))
#generate points and count inside
for i in range (N):
  x= rand()
  y= rand()
  y_value= x**2-y+1
  #print(" y value is : ", y)
  xlist = np.append(xlist, x)
  ylist = np.append(ylist, y)
# plot all the scatter points
axis[0, 1].scatter(xlist, ylist, s=2)

f2 = np.empty((0,0))
x2 = np.linspace(0, 1, 100)
for x in x2:
  f2 = np.append (f2, SecondEquation(x))
# plotting the actual graph
# plot the line in the graph of equation
axis[0, 1].plot(x2, f2,  color='b') 




# start next equation
print("\r\nTesing Case for (x^4)")
print("====================================" )
print(f"Our Computed Solution is : {FindValue(ThirdEquation, 0, 2, 5000): .4f}")
print(f"Actual solution is       : {FunctionThree(0, 2): .4f}")

# create a title
axis[1, 0].set_title("(x^4)")
#plot the random numbers in graph
#empty the x and ylist
xlist = np.empty((0, 0))
ylist = np.empty((0, 0))
# next value
# setting up for the scatter plot
for i in range (N):
  x= rand()
  y= rand()
  y_value= x**4-y+1
  xlist = np.append(xlist, x)
  ylist = np.append(ylist, y)
# plot all the random points
axis[1, 0].scatter(xlist, ylist, s=2)

# now printing out the equation plot line
f2 = np.empty((0,0))
x2 = np.linspace(0, 1, 100)
for x in x2:
  f2 = np.append (f2, ThirdEquation(x))
# plotting the actual graph
#plot the line on the corresponding graph
axis[1, 0].plot(x2, f2,  color='b') 

# save the plot figure to file pdf so easier to pdf
plt.savefig("RandomValues.pdf")
