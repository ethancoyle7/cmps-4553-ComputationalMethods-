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

figure, axis = plt.subplots(2,2)
N=5000 # number of points to test
# create upper and lower bounds
a=0
b=2
# intitalize counter, will be reset after each test
# because it will just bleed over into the next one with 
# subplot count
count=0


#NEXT CASE
# initialize xlist and y list to empty
xlist = np.empty((0, 0))
ylist = np.empty((0, 0))

# for rand val within rang of N
for i in range (N):
    # generate random x and y values
    x= rand()*2
    y= rand()*2

    #put in the equation
    y_value= 1-y+(x+1)**-1

    # get the count and calculate the integral between
    # see if we get close approximation to actual
    if y_value<1: 
      count += 1
    CountSum = np.sum(count)/N
    CalculatedValue= (b-a) * CountSum

    # append the list so can plot scatter plot
    xlist = np.append(xlist, x)
    ylist = np.append(ylist, y)
# plot the scatter plot
axis[0, 0].scatter(xlist, ylist, s=2)
# now that all the definitions are done calculate the
# different equations

# printout to show table
print("\r\nTesting Case for (x+1)**-1")
print("====================================" )
print ("Esimate of (x+1)**-1 is  : ", CalculatedValue)
print ("The Actual Value is      : ",1.099)
# for our subplots
# create title for easier find
axis[0, 0].set_title("((x+1)**-1)")
#plot the random numbers in graph

# plot the equation on the graph
f2 = np.empty((0,0))
x2 = np.linspace(0, 2, 100)
for x in x2:
  # appending the actual curve line
  f2 = np.append (f2, (x+1)**-1)
# plotting the actual graph
axis[0, 0].plot(x2, f2,  color='b') 



#NEXT CASE
# empty out the x and y list and then
# reset the count to 0
xlist = np.empty((0, 0))
ylist = np.empty((0, 0))
count=0
# repeat the above steps for the test case x^2
for i in range (N):
    x= rand()*2
    y= rand()*2
    y_value= (x**2)-y+1
    if y_value<1: 
      count += 1
    # get sum divide by the N which is 5000
    # then calculate for the integral
    CountSum = np.sum(count)/N
    CalculatedValue= (b-a) *CountSum*3

    # append the x and y values to corresponding
    # list so can plot the scatter plot
    xlist = np.append(xlist, x)
    ylist = np.append(ylist, y)

# plot the scatter plot with x and y list
axis[0, 1].scatter(xlist, ylist, s=2)
print("\r\nTesing Case for (x^2)")
print("====================================" )
print ("Esimate of x^2 is   : ", CalculatedValue)
print ("The Actual Value is : ", 2.667)
# call the store value of the function and pass in a and b

# title the graph subplot
axis[0, 1].set_title("(x^2)")
#plot the random numbers in graph
#create empty list an append the list 
# with x and y value so can plot scatter points


# plotting the graph of equation within boundaries
# was having issues getting this to format properly
# so i set the linspace to 1.4 which got it on the graph
# without the graph looking wierd 
f2 = np.empty((0,0))
x2 = np.linspace(0, 1.4, 100)
for x in x2:
  f2 = np.append (f2, x**2)
# plotting the actual graph
# plot the line in the graph of equation
axis[0, 1].plot(x2, f2,  color='b') 


#NEXT CASE
# reset the list and count 
# we figuing our e^x
xlist = np.empty((0, 0))
ylist = np.empty((0, 0))
count=0

# get the x rand and y rand and calculate the value
# after getting count of y values greater than 1
# then calculating the integral to see if we get close
# to actual value
for i in range (N):
    x= rand()*2
    y= rand()*2
    y_value= np.exp(x)-1
    if y_value<1: 
      count += 1
    CountSum = np.sum(count)/N
    CalculatedValue= (b-a) *CountSum*8

    # append x and y
    xlist = np.append(xlist, x)
    ylist = np.append(ylist, y)
# plot the scatter plot
axis[1, 0].scatter(xlist, ylist, s=2)
## calc e^x
print("\r\nTesing Case for (e^x)")
print("====================================" )
print ("Esimate of e^x is  : ", CalculatedValue)
print ("The Actual Value is: ", 6.389)

# make title 
axis[1, 0].set_title("(e^x)")

# plotting the e^x curve 
f2 = np.empty((0,0))
x2 = np.linspace(0, 1, 100)
for x in x2:
  f2 = np.append (f2, np.exp(x))
# plot the line between 0 and 2
axis[1, 0].plot(x2, f2,  color='b') 




#NEXT CASE
# clear the list and rest count to 0
xlist = np.empty((0, 0))
ylist = np.empty((0, 0))
count=0

# testing to see if random numbers
# et close to the actual value of equation
# with and b
for i in range (N):
  x= rand()
  y= rand()
  y_value= x**4-y+1
  if y_value<1: 
      count += 1
  CountSum = np.sum(count)/N
  CalculatedValue= (b-a) *CountSum*4

  # appen the list
  xlist = np.append(xlist, x)
  ylist = np.append(ylist, y)

# plot all the random points
axis[1, 1].scatter(xlist, ylist, s=2)

# visual comparison
print("\r\nTesing Case for (x^4)")
print("====================================" )
print ("Esimate of x^4 is    : ", CalculatedValue)
print ("The Actual Value is  : ",6.400 )

# plotting the actual graph of the line
f2 = np.empty((0,0))
x2 = np.linspace(0, 1, 100)
for x in x2:
  f2 = np.append (f2,x**4)
# plotting the actual graph
#plot the line on the corresponding graph
axis[1, 1].plot(x2, f2,  color='b') 


plt.savefig("RandomValues.pdf")
