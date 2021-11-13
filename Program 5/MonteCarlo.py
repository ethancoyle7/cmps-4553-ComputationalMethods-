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
N = 5000

#initialize count of points inside
count = 0

#select good looking plot sorted
matplotlib.style.use("ggplot")
xlist = np.empty((0, 0))
ylist = np.empty((0, 0))

#generate points and count inside
for i in range (N):
  x= rand()
  y= rand()
  y_value= 1-y+(x+1)**-1
  if y_value<1: 
    count += 1

  xlist = np.append(xlist, x)
  ylist = np.append(ylist, y)

#Print out the calculation of the y value  using the random digits
# print out the actual value
# conclusion for this test case is the more number o
#f values we have, approximately a .14 gap
print("\r\nTesing Case for (x+1)**-1")
print("====================================" )
print ("Esimate of (x+1)**-1 is : ", 4*count/N)
print ("The Actual Value is     : ",1.099)

# for our subplots
plt.axis([0, 5, 0, 10])
figure, axis = plt.subplots(2,2)
axis[0, 0].set_title("((x+1)**-1)")
#plot the random numbers in graph
axis[0, 0].scatter(xlist, ylist, s=2)

f2 = np.empty((0,0))
x2 = np.linspace(0, 1, 100)
for x in x2:
  f2 = np.append (f2, (x+1)**-1)
# plotting the actual graph
axis[0, 0].plot(x2, f2,  color='b') # <--- pass ax=ax here




# reset values and empty the list and start again
# next values 
N = 5000
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



# resetting the values and emptying the lists
# next values 
N = 5000
#initialize count of points inside
count = 0
#select good looking plot sorted
xlist = np.empty((0, 0))
ylist = np.empty((0, 0))
# next value
for i in range (N):
  x= rand()
  y= rand()
  y_value= x**4-y+1
  if y_value<1: 
    count += 1

  xlist = np.append(xlist, x)
  ylist = np.append(ylist, y)

#Print out the calculation of the y value  using the random digits
# print out the actual value
# conclusion for this test case is the more number of 
#values we have, approximately a .14 gap
print("\r\nTesing Case for (x^4)")
print("====================================" )
print ("Esimate of (x^4) is : ", 8*count/N)
print ("The Actual Value is : ",6.400 )

# for our subplots
axis[1, 0].set_title("(x^4)")
#plot the random numbers in graph
axis[1, 0].scatter(xlist, ylist, s=2)

f2 = np.empty((0,0))
x2 = np.linspace(0, 1, 100)
for x in x2:
  f2 = np.append (f2, x**2)
# plotting the actual graph
axis[1, 0].plot(x2, f2,  color='b') # <--- pass ax=ax here
# now copy and past for each test case uni




plt.savefig("RandomValues.pdf")
