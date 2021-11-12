##=================================================#
# Author - Ethan Coyle                             #
# Inst   - Dr. StringFellow                        #
# Class  - CMPs 4553 Computational Methods         #
# Assig  - Program 5 Composit Simsons Rule         #
#                                                  #
# In this program, i will be demonstrating         #
# the calculation of four different calculations   #
# using simsons composite rule that will plot the  #
# results in the corresponding subgraphs  and  will#
# display the exact value and the value that i got #
# from calculating the the screen where the viewer #
# can see the comparison between the two           #
#==================================================#

# creating our imports numpy for the plotting data
# and matlib for the actual plotting
import numpy as np
import matplotlib, matplotlib.pyplot as plt


# using nice ggplot to plot the data with dots and 
# a grid
matplotlib.style.use("ggplot")
# declare variable for calculation
A = 0
B = 2
N =11
#Compute width
H = (B - A) / (N - 1)

x = np.linspace(A, B, N)
# the f is equal to (x+1)^-1
f= (x+1)**-1

Y_Function=(x+1)**-1
C_simp = (H/3) * (f[0] + 2*sum(f[:N-2:2]) \
            + 4*sum(f[1:N-1:2]) + f[N-1])
# display the intervals over intervals and then the 
# approximated simson value


print ("\r\nIntegral of f(x) = (x+1)^-1 on intvl [", A, ",", B, "]")
print("---------------------------------------------------")
print("The exact value of S.R. (x+1)^-1 is  :  1.099")
print("Our Calc. using S.R of  (x+1)^-1 is  : " ,C_simp)
figure, axis = plt.subplots(2,2)
# we now going to plot the composite simson rule calulation
# over the intervals with "ro" in ggplot for red dots
axis

# we graph the function by itself using line 
# initialize hat it is and then sub in the value x for it and 
# then print in the subgraph corresponding to the plotting
# thus we have side by side comparison
X_Function = np.linspace(A, B, 100)
Y_Function=(X_Function+1)**-1 # takes the same function but this time we graphing

axis[0, 0].scatter(x, f,s=10)
axis[0,0].plot(X_Function,Y_Function, color='b')
axis[0, 0].set_title("(x+1)^-1")
#plt.axis([0, 2, 0, 1])
plt.axis([0, 5, 0, 10])
# copy and pasting the data to reinitialize with the next test 
#function for simson rule this one is x^4
# only difference in this one is rename the f to f2 to
# show that is is the second test not necessary beacuse once
#initialized, python will voerride the values accoringly 
# but just give better understanding to know whats going on
# the setup is the exact same

# the new f is equal to (x^4)
f2= x**4
C_simp = (H/3) * (f2[0] + 2*sum(f2[:N-2:2]) \
            + 4*sum(f2[1:N-1:2]) + f2[N-1])
print ("\r\nIntegral of f(x) = (x+1)^-1 on intvl [", A, ",", B, "]")
print("---------------------------------------------------")
print("The exact value of S.R. x^4 is  :  6.400")
print("Our Calc. using S.R of  x^4 is  : " ,C_simp)
# we now going to plot the composite simson rule calulation
# over the intervals with "ro" in ggplot for red dots
X_Function = np.linspace(A, B, 100)
Y_Function=X_Function**4 # takes the same function but this time we graphing
axis[0,1].plot(X_Function,Y_Function,color='b')

# print out the scatter plot and then the line plot for the function 
# the line plot will plot the actual function and the 
# scatter plot will plot our alloted ammount 
axis[0, 1].scatter(x, f2,s=11)
axis[0, 1].set_title("(x^4)")

# just for fun, we are going to plot 4 different tests to fill up one graph figure 
# copy the values two more times, set up is similar only for 
# reader better understanding the f will increment by one for the others as well
# demonstrating (x^2)
f3= x**2
C_simp = (H/3) * (f3[0] + 2*sum(f3[:N-2:2]) \
            + 4*sum(f3[1:N-1:2]) + f3[N-1])
print ("\r\nIntegral of f(x) = (x^2) on intvl [", A, ",", B, "]")
print("---------------------------------------------------")
print("The exact value of S.R. x^2 is  :  2.667")
print("Our Calc. using S.R of  x^2 is  : " ,C_simp)
# we now going to plot the composite simson rule calulation
# over the intervals with "ro" in ggplot for red dots
X_Function = np.linspace(A, B, 100)
Y_Function=X_Function**2 # takes the same function but this time we graphing
axis[1,0].plot(X_Function,Y_Function,color='b')
axis[1, 0].scatter(x, f3,s=10)
axis[1, 0].set_title("(x^2)")
# plot the graph and set the title, this will go in the bottom left corner graph

# now for the fourth and final one
# e^x for scalar 
# to do our calculation and assign this value to the new f
f4= np.exp(x)
# simsons rule with the f replace with new f value
# calculate then graph in the lower right corner
C_simp = (H/3) * (f4[0] + 2*sum(f4[:N-2:2]) \
            + 4*sum(f4[1:N-1:2]) + f4[N-1])
print ("\r\nIntegral of f(x) = (x^2) on intvl [", A, ",", B, "]")
print("---------------------------------------------------")
print("The exact value of S.R. e^x is  :  6.389")
print("Our Calc. using S.R of  e^x is  : " ,C_simp)
# we now going to plot the composite simson rule calulation
# over the intervals with "ro" in ggplot for red dots

X_Function = np.linspace(A, B, 100)
Y_Function= np.exp(X_Function)# takes the same function but this time we graphing
axis[1,1].plot(X_Function,Y_Function,color='b')
# plot the line plot and then the actual function plot with
# scatter plotting
axis[1, 1].scatter(x, f4,s=10)
axis[1, 1].set_title("(e^x")
# this graph looks very very aweful there is only one dot that shows up and
#it looks like the top left the red dots shows there but the calculation is correct

# plot all four graphs inside of the subgraph output
plt.savefig("Simsons Composite Rule Graph.pdf")
