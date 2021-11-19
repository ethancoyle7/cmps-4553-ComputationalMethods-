#=================================================#
#                                                 #
# Author- Ethan Coyle                             #
# Inst-   Dr. StringFellow                        #
# Class - CMPS 4553 Computational Methods         #
# Prog  - Program 5 part 2                        #
#                                                 #
# in this program, we are implementing the        #
# following equations  using matplotlib  to plot  #
# and guestimate the  Functionue of the alotte    #
# equations compared against the actual Functionu #
# e and plot the scatter dots and the actual      #
# line of the curve                               #
#                                                 #
# IN THE SECOND HALF OF THE PROGRAM               #
#=================================================#
# In this program, i will be demonstrating        #
# the calculation of four different calculations  #
# using simsons composite rule that will plot the #
# results in the corresponding subgraphs  and  wil#
# display the exact value and the value that i got#
# from calculating the the screen where the viewer#
# can see the comparison between the two          #
#=================================================#
#=================================================#
# The equations computed are stated below         #
#                                                 #
# 1. (x+1)^-1                                     #
# 2. x^4                                          #
# 3. X^2                                          #
# 4. e^x                                          #
#=================================================#



import random
import numpy as np
import matplotlib, matplotlib.pyplot as plt

#number of random points to Generate
#initialize count of points inside
#select good looking plot sorted
matplotlib.style.use("ggplot")



# create a subplot graph for all our other subplots
figure, axis = plt.subplots(2,2)
# set axis y and axis x range
plt.axis([0, 5, 0, 30])

# initilize  umber of points to test
N=5000 
#start counters
FunctionOneCount=0
FunctionTwoCount=0
FunctionThreeCount=0
FunctionFourCount=0

# FOR READER UNDERSTANDING PRINT WHAT THE FIRST SECTION
#DOING 
print("================================================")
print("\r\n FIRST WE WILL TESTING USING MONTE CARLO    \n")
print("================================================\n\n")


# clear the x and y lists
# then repeat the whole process for the next function
# this function will be  x+1^-1
xlist = np.empty((0, 0))
ylist = np.empty((0, 0))
axis[1, 1].set_title("((x+1)**-1")
# for rand Function within rang of N
for i in range (N):
    # generate random x and y Functionues
  x= random.uniform(0, 2)
  y= random.uniform(0, 4)

    #put in the equation
  FirstFunction= (x+1)**-1
  if y < FirstFunction: 
    FunctionOneCount += 1
    # append the list so can plot scatter plot
  xlist = np.append(xlist, x)
  ylist = np.append(ylist, y)
# plot the scatter plot
axis[0, 0].scatter(xlist, ylist, s=2)
# now that all the definitions are done calculate the
# now to plot the actual line equation within boundaries
f2 = np.empty((0,0))
x2 = np.linspace(0, 2, 100)
for x in x2:
  # appending the actual curve line
  f2 = np.append (f2, (x+1)**-1)
# plotting the actual graph
axis[0, 0].plot(x2, f2,  color='b') 

#set the limits of te graph x and y
axis[0,0].set_xlim(0,2)
axis[0,0].set_ylim(0,4)
# printout to show table for x+1**-1
# for reader viewing
print("\r\nTesting Case for (x+1)**-1")
print("====================================" )
print ("Esimate of (x+1)^-1   :  ",8*FunctionOneCount/N) 
print ("Act. Value (x+1)^-1   :  ", 1.099,'\n')

# NEXT CASE x^4
#---------------#

#Reset points for next function
xlist = np.empty((0, 0))
ylist = np.empty((0, 0))
# create a title for the graph
axis[0, 1].set_title("(x^4")
#generate points and count inside
for i in range (N):
  # generate the random numbers for x and y 
  # to approximate for the function
  x= random.uniform(0, 2)
  y= random.uniform(0, 16)
  #check the count of the random x nd y value
  FunctionTwo = x**4
  if y < FunctionTwo: 
    FunctionTwoCount += 1
  # if the count of the function y values are less than 
  # that in the function, increment the compile
  # append the randomly generate numbers to x and y list
  xlist = np.append(xlist, x)
  ylist = np.append(ylist, y)

#now we plotting the scatter plot for all the 
# rndomly generated values within the confine 
# of the generated which will appear above and below the
# actual function so we can approximate
axis[0,1].scatter(xlist, ylist, s=2)

# now we generate the actual line function within
# the confines of the a and b values 0 to 2 100 points
# and make it line for visual
f2 = np.empty((0,0))
x2 = np.linspace(0, 2, 100)
for x in x2:
  f2 = np.append (f2, x**4)

axis[0,1].plot(x2, f2,  color='b')

# we have to set the x and y limits to fall within that
# of the randomly generate numbers
axis[0,1].set_xlim(0,2)
axis[0,1].set_ylim(0,16)

# print out the compariosn
print("\r\nTesting Case for (x**4)")
print("====================================" )
print ("Esimate of x^4        :  ",32*FunctionTwoCount/N) 
print ("Act. Value of x^4     :  ", 6.400,'\n')


# NEXT CASE x^2
#---------------#

# initilize the x and y list to 0
xlist = np.empty((0, 0))
ylist = np.empty((0, 0))
axis[1, 0].set_title("(x^2")
#randomly generate the x and y and points inside graph
for i in range (N):
  # generate the random x between 0 and 2
  # genereate between 0 and 4 for y vals
  x = random.uniform(0, 2) 
  y = random.uniform(0, 4)

  # function is x^2
  FunctionThree = x**2
  # get count of y< function y
  if y < FunctionThree: 
    FunctionThreeCount += 1
  # append the x and y randomly generated
  # values
  xlist = np.append(xlist, x)
  ylist = np.append(ylist, y)

#plot the scatter plot with appended list values
axis[1,0].scatter(xlist, ylist, s=2)

# now plot the actual line 
f2 = np.empty((0,0))
x2 = np.linspace(0, 2, 100)
for x in x2:
  f2 = np.append (f2, x**2)

axis[1,0].plot(x2, f2,  color='b')
# set x and y limits
axis[1,0].set_xlim(0,2)
axis[1,0].set_ylim(0,4)

# print out the compariosn for x**2
print("\r\nTesting Case for (x**2")
print("====================================" )
print ("Esimate of x^2        :  ",8*FunctionThreeCount/N) 
print ("Act. Value of x^2     :  ", 2.667,'\n')


# NEXT CASE e^x
#---------------#

# reselt the x and y list
# doing the calulcation for e^x
# bottom right grpah
xlist = np.empty((0, 0))
ylist = np.empty((0, 0))
axis[1, 1].set_title("(e^x")
for i in range (N):
    x= random.uniform(0, 2)
    y= random.uniform(0, 4)
    # read in the function value e^x
    FunctionFour= np.exp(x)

    # get the count of those y values less than function
    if y < FunctionFour: 
      FunctionFourCount += 1

    # append x and y to empty lsits accordingly
    xlist = np.append(xlist, x)
    ylist = np.append(ylist, y)
# plot the scatter plot using appended values
# s is the size so small dots
axis[1, 1].scatter(xlist, ylist, s=2)

# plotting the e^x curve 
f2 = np.empty((0,0))
x2 = np.linspace(0, 2, 100)
for x in x2:
  f2 = np.append (f2, np.exp(x))
# plot the line between 0 and 2
axis[1, 1].plot(x2, f2,  color='b') 
# set the x and y limits of the function
axis[1,1].set_xlim(0,2)
axis[1,1].set_ylim(0,4)

# print out the table for e^x to view compariosn
print("\r\nTesing Case for (e^x)")
print("====================================" )
print ("Esimate of e^x        :  ",8*FunctionFourCount/N) 
print ("Act. Value of e^x     :  ", 6.389,'\n')



# save the output plotting to file pdf
plt.savefig("MonteCarloTesting.pdf")


# now start on simpsons rule and save to another output file
print("\n\n")
print("================================================")
print("\r\n NOW WE ARE TESTING USING SIMSONS RULE      \n")
print("================================================\n\n")
# now we running simssons rule
matplotlib.style.use("ggplot")
plt.axis([0, 5, 0, 10])
# declare variable for calculation
A = 0
B = 2
N =11
#Compute width
H = (B - A) / (N - 1)

x = np.linspace(A, B, N)
# the f is equal to (x+1)^-1
FunctionOne= (x+1)**-1


C_simp = (H/3) * (FunctionOne[0] + 2*sum(FunctionOne[:N-2:2]) \
            + 4*sum(FunctionOne[1:N-1:2]) + FunctionOne[N-1])
# display the intervals over intervals and then the 
# approximated simson value


print ("\r\nIntegral of f(x) = (x+1)^-1 on intvl [", A, ",", B, "]")
print("---------------------------------------------------")
print("The exact value of S.R. (x+1)^-1 is  :  1.099")
print("Our Calc. using S.R of  (x+1)^-1 is  : " ,C_simp)
figure, axis = plt.subplots(2,2)
axis[0, 0].plot(x, FunctionOne,color='b')
axis[0, 0].set_title("(x+1)^-1")
#plt.axis([0, 2, 0, 1])
plt.axis([0, 5, 0, 10])

# next function to plot is x^4
Function2= x**4

# plug the function into the simsons rule
C_simp = (H/3) * (Function2[0] + 2*sum(Function2[:N-2:2]) \
            + 4*sum(Function2[1:N-1:2]) + Function2[N-1])
print ("\r\nIntegral of f(x) = (x^4) on intvl [", A, ",", B, "]")
print("---------------------------------------------------")
print("The exact value of S.R. x^4 is  :  6.400")
print("Our Calc. using S.R of  x^4 is  : " ,C_simp)
# we now going to plot the composite simson rule calulation
# over the intervals with "ro" in ggplot for red dots
axis[0, 1].plot(x, Function2,color='b')
axis[0, 1].set_title("(x^4)")


# We now are going to figure out the 3rd function
# using simsons rule (x^2)
# declare the function
Function3= x**2
# calculate simsoms rule on the function
C_simp = (H/3) * (Function3[0] + 2*sum(Function3[:N-2:2]) \
            + 4*sum(Function3[1:N-1:2]) + Function3[N-1])
# now we find out how close our calculation is 
print ("\r\nIntegral of f(x) = (x^2) on intvl [", A, ",", B, "]")
print("---------------------------------------------------")
print("The exact value of S.R. x^2 is  :  2.667")
print("Our Calc. using S.R of  x^2 is  : " ,C_simp)

axis[1, 0].plot(x, Function3,color='b')
axis[1, 0].set_title("(x^2)")
# plot the graph and set the title, this will go in the bottom left corner graph

#calculate and plot the graph for e^x
Function4= np.exp(x)
# simsons rule with the f replace with new f value
# calculate then graph in the lower right corner
C_simp = (H/3) * (Function4[0] + 2*sum(Function4[:N-2:2]) \
            + 4*sum(Function4[1:N-1:2]) + Function4[N-1])
print ("\r\nIntegral of f(x) = (e^x) on intvl [", A, ",", B, "]")
print("---------------------------------------------------")
print("The exact value of S.R. e^x is  :  6.389")
print("Our Calc. using S.R of  e^x is  : " ,C_simp)
axis[1, 1].plot(x, Function4,color='b')
axis[1, 1].set_title("(e^x")


# plot all four graphs inside of the subgraph output
plt.savefig("Simsons Composite Rule Graph.pdf")
