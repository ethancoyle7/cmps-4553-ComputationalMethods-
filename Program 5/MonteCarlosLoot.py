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
# 4. e^x                                         #
#                                                #
# user note : while working with the subplots,   #
#     there we a few wierd issues that i had     #
# with plotting all four such like this but I    #
# got the subplots to run from 0,2 except for the#
# x^2 value was having issues plotting this so it#
# is just ranging from 0,1 but the plot and the  #
# random numbers are working the way they should #
#================================================#


# imports for the numpy and random num generator
from random import random as rand
import numpy as np
# matplot for plotting library
import matplotlib, matplotlib.pyplot as plt

#number of random points to Generate
N = 5000
#initialize count of points inside
count = 0
# initilize upper and lower bounds
#get easier to view style plotter ggplot
matplotlib.style.use("ggplot")

# (1+x)**-1 graph is our runner up
xlist = np.empty((0, 0))
ylist = np.empty((0, 0))
#generate points and count inside
for i in range (N):
  # generate random x and y values
  x= rand()*2
  y= rand()*2
# the f is equal to (x+1)^-1
  y_value= 1-y+(x+1)**-1
  if y_value<1: 
    count += 1 # increment counter
  # append the y and x values to the list
  xlist = np.append(xlist, x)
  ylist = np.append(ylist, y)

# our first test case utilizing the 
# function (x+1)**-1
print("\r\nTesing Case for (x+1)**-1")
print("====================================" )
print ("Esimate of (x+1)**-1 is : ", 2*count/N)
print ("The Actual Value is     : ",1.099)
# to create subplots of our functions a 2 by 2
figure, axis = plt.subplots(2,2)
# title of the first plot
axis[0, 0].set_title("((x+1)**-1)")
# plot our random numbers x and y size is 2
axis[0, 0].scatter(xlist, ylist, s=2)
# now to plot our actual curve
f2 = np.empty((0,0))           # create empty list 
x2 = np.linspace(0, 2,100) # from 0 to 2 100 values
for x in x2:
  f2 = np.append (f2, (x+1)**-1)
# after appending the values plot the coordinats
axis[0, 0].plot(x2, f2,  color='b')

# set the limits of the x and y end
plt.xlim(0,2)
plt.ylim(0,2)

# x^2 graph
# reset values and empty the list and start again
# next values 
N = 2000
#initialize count of points inside
count = 0
#select good looking plot sorted
xlist = np.empty((0, 0))
ylist = np.empty((0, 0))
#generate points and count inside
for i in range (N):
  x= rand()
  y= rand()
  y_value= x**2-y+1
  if y_value<1: 
    count += 1

  # append the list for graphing
  xlist = np.append(xlist, x)
  ylist = np.append(ylist, y)

#Print out the calculation of the y value  using the random digits
# print out the actual value
# conclusion for this test case is the more number 
#of values we have, approximately a .14 gap
print("\r\nTesing Case for (x^2)")
print("====================================" )
print ("Esimate of (x^2) is : ", 4*count/N)
print ("The Actual Value is : ", 2.667)

# for our subplots
axis[0, 1].set_title("(x^2)")
#plot the random numbers in graph
axis[0, 1].scatter(xlist, ylist, s=2)

f2 = np.empty((0,0))
x2 = np.linspace(0, 1, 100)
for x in x2:
  f2 = np.append (f2, x**2)
# plotting the actual graph
axis[0, 1].plot(x2, f2,  color='b') # <--- pass ax=ax here
# now copy and past for each test case uni

# setting the y and x limits
plt.xlim(0,2)
plt.ylim(0,2)


# x^4 graph next
# our next graph and start by resetting variables
#initialize count of points inside
count = 0
N=5000
# new list set to read the x and ys for appendage
XList = np.empty((0, 0))
YList = np.empty((0, 0))
# next value

for i in range (N):
  XValue= rand()*4
  YValue= rand()*4
  y_value= XValue**4-YValue+1
  if y_value<1: 
    count += 1
  XList = np.append(XList, XValue)
  YList = np.append(YList, YValue)

# print out the result
print("\r\nTesing Case for (x^4)")
print("====================================" )
print ("Esimate of (x^4) is : ", 16*count/N)
print ("The Actual Value is : ",6.400 )

axis[1, 0].set_title("(x^4)")
#plot the random numbers in graph
axis[1, 0].scatter(XList, YList, s=2)

f2 = np.empty((0,0))
x2 = np.linspace(0, 2, 100)
for x in x2:
  f2 = np.append (f2, x**2)
# plotting the actual graph
axis[1, 0].plot(x2, f2,  color='b') # <--- pass ax=ax here
# now copy and past for each test case uni

plt.xlim(0,2)
plt.ylim(0,2)
# starting next case e^x
#generate points and count inside
N=6000
count = 0
ValueX = np.empty((0, 0))
ValueY = np.empty((0, 0))
for i in range (N):
  ValX= rand()*2
  ValY= rand()*2
  y_value = np.exp(ValX) - 1
  if y_value < 1: 
    count += 1
  # appending the x and y values
  ValueX = np.append(ValueX, ValX)
  ValueY = np.append(ValueY, ValY)

## calc e^x
print("\r\nTesing Case for (e^x)")
print("====================================" )
print ("Esimate of e^x is  : ", 16*count/N)
print ("The Actual Value is: ", 6.389)

# make title 
axis[1, 1].set_title("(e^x)")
#plot the scatter plot
axis[1, 1].scatter(ValueX, ValueY, s=2)

# plotting the e^x curve in between 0 and 2
f2 = np.empty((0,0))
x2 = np.linspace(0, 2, 100)
for x in x2:
  f2 = np.append (f2, np.exp(x))
# plot the line between 0 and 2
axis[1, 1].plot(x2, f2,  color='b') 

plt.xlim(0,2)
plt.ylim(0,2)
# output everything to the output will format to a 2 by
# 2
plt.savefig("Monte Carlo's Loot.pdf")
