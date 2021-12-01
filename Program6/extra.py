#============================================================#
# Author   - Ethan Coyle                                     #
#Instructor- Dr. StringFellow                                #
#Class     - CMPS 4553- comp. Methods                        #
#Assignment- Program 6                                       #
#============================================================#
#Your task is to determine the curve fit for two models for  #
#each of the three data files given. Plot the two fits for   #
#each file and print out a statement that says which one is  #
# better based on the fit score.                             #
#============================================================#
# extra credit using yamada is on the                        #
# bottom of the program.                                     #
#============================================================#
# User note-  the first portion of the program is calculating#
#             using the Go and Go-s models and outputting    #
#             the predictions, the true values & the         #
#             calculated score with nice easy to read format #
#             and then compares the scores and plots the     #
#             Yamada Expression which is the# extra credit.  #
#             The output of the Yamada is based off of SRGM2 #
#             and turns out to be the most accurate out of   #
#             all the tests but the third file the Go-s model#
#             is also almost right on the dot for the        #
#             extiates prediction                            #
#============================================================#

import numpy as np
from scipy.optimize import curve_fit
import matplotlib, matplotlib.pyplot as plt

# function definition methods we are using 
def GoSModel(t,a,b):
  return a*(1-(1+b*t)*np.exp(-b*t))
  #a(1-(1+bt)e-bt)
# create the function definition for the G-O
def GoModel(t,a,b):
  return a*(1-np.exp(-b*t))
  #a(1-e-bt)

#extra credit yamada expression for srgn 2
def Yamada(t,a,bc,d):
  return a * (1- np.exp(-bc * (1-np.exp(-d*t))))
#extra credit yamada expression


# nicce style plot to use for graphs of plots
matplotlib.style.use("ggplot")

# read in the first file
# delimter must be space there is no comma inside of infiles
my_data = np.genfromtxt('srgm1.txt', delimiter='')
my_data = my_data[my_data[:,0].argsort()]

#make it 1xN data instead of Nx1
xdata = my_data[:,0].transpose()
ydata = my_data[:,1].transpose()

# intial guesses for the data 
# ydat is last y value element in collum
# b is between 0 and 1
InitialValues = [ydata[-1],0.0001]

# fitting data in the curve fit
# formatting the bounds to fit bewlow the values lower bound upper bounds
popt, pcov = curve_fit(GoSModel, xdata, ydata, p0=InitialValues, bounds=([ydata[-1],0.0001], [900,200]))
# lower bounds ydata, 0.0001 below
# upperbounds whatever is above

# now to make predicted guess
x_guess = xdata[-1]+10 # intial guess
# calculate the prediction for the Gos Model and output
y_pred = GoSModel(x_guess, *popt)
print("The True value for the  input 1 is :" ,231 )
print('-----------------------------------------')
print("From Input 1, the GoS Model prediction was : (", x_guess, ',', y_pred, ")")

GO_S_score = popt
print('From Input 1, The GoS Model Score was      :', popt[0])



#plot the data
plt.title("SRGM1")
plt.plot(xdata, ydata, 'bo', label='data')
plt.plot(xdata, GoSModel(xdata, *popt), '-', label='Go-S Data')
# plotting the scattered guesses
plt.scatter ([x_guess], [y_pred], color = 'green')
plt.legend() # legend for better understanding
# done with the first


# now we are plotting for the curve fit of the go model second model 
popt, pcov = curve_fit(GoModel, xdata, ydata, p0=InitialValues, bounds=([ydata[-1],0.0001], [500,180]))
# lower bounds ydata, 0.0001 below
# upperbounds whatever is above

# now to make predicted guess
x_guess = xdata[-1]+10 # intial guess
# calculate the prediction for the Gos Model and output
y_pred = GoModel(x_guess, *popt)

print("From Input 1, The Go Model Prediction was  : (", x_guess, ',', y_pred, ")")
GOScore = popt
print('From Input 1, The Go  Model Score was      :', popt[0])
     
print("==================================================================\n")


#plot the data

plt.plot(xdata, GoModel(xdata, *popt), '-', label='Go Data')
# plotting the scattered guesses
plt.scatter ([x_guess], [y_pred], color = 'red')

#creating labels for the graph
plt.xlabel('x')
plt.ylabel('y')
plt.legend() # legend for better understanding
plt.savefig("plot1.pdf")
# next data done with this
# clear the data so can plot clean again
plt.clf()

# now on for the second srgm file


# extra credit
# def YamadaModel(t,a,b,c,d):
#   return a*(1-np.exp((-b*c)*(1-np.exp(-d*t))))
# #make an initial guess for a, b, c, d
# init_vals = [50, 0, 90, 63]

my_data = np.genfromtxt('srgm2.txt', delimiter='')
my_data = my_data[my_data[:,0].argsort()]

#make it 1xN data instead of Nx1
xdata = my_data[:,0].transpose()
ydata = my_data[:,1].transpose()

# intial guesses for the data 
# ydat is last y value element in collum
# b is between 0 and 1
InitialValues = [ydata[-1],0.0001]

# fitting data in the curve fit
# formatting the bounds to fit bewlow the values lower bound upper bounds
popt, pcov = curve_fit(GoSModel, xdata, ydata, p0=InitialValues, bounds=([ydata[-1],0.0001], [900,1]))

# lower bounds ydata, 0.0001 below
# upperbounds whatever is above

# now to make predicted guess
x_guess = xdata[-1]+10 # intial guess
# calculate the prediction for the Gos Model and output
y_pred = GoSModel(x_guess, *popt)

print("The True value for the  input 2 is :" ,245 )
print('-----------------------------------------')
print("From Input 2, the GoS Model prediction was : (", x_guess, ',', y_pred, ")")

GO_S_score = popt
print('From Input 2, The GoS Model Score was      :', popt[0])


#plot the data
plt.title("SRGM2")
plt.plot(xdata, ydata, 'bo', label='data')
plt.plot(xdata, GoSModel(xdata, *popt), '-', label='Go-S Data')
# plotting the scattered guesses
plt.scatter ([x_guess], [y_pred], color = 'green')
plt.legend() # legend for better understanding
# done with the first


# now we are plotting for the curve fit of the go model second model 
popt, pcov = curve_fit(GoModel, xdata, ydata, p0=InitialValues, bounds=([ydata[-1],0.0001], [500,180]))
# lower bounds ydata, 0.0001 below
# upperbounds whatever is above

# now to make predicted guess
x_guess = xdata[-1]+10 # intial guess
# calculate the prediction for the Gos Model and output
y_pred = GoModel(x_guess, *popt)

print("From Input 2, The Go Model Prediction was  : (", x_guess, ',', y_pred, ")")
GOScore = popt
print('From Input 2, The Go  Model Score was      :', popt[0])

print("==================================================================\n")


#plot the data for the gomodel
plt.plot(xdata, GoModel(xdata, *popt), '-', label='Go Data')
# plotting the scattered guesses
plt.scatter ([x_guess], [y_pred], color = 'red')

#creating labels for the graph
plt.xlabel('x')
plt.ylabel('y')
plt.legend() # legend for better understanding
plt.savefig("plot2.pdf")
# next data done with this
# clear the data so can plot clean again
plt.clf()


# now for the third input file
my_data = np.genfromtxt('srgm3.txt', delimiter='')
my_data = my_data[my_data[:,0].argsort()]

#make it 1xN data instead of Nx1

xdata = my_data[:,0].transpose()
ydata = my_data[:,1].transpose()

# intial guesses for the data 
# ydat is last y value element in collum
# b is between 0 and 1
InitialValues = [ydata[-1],0.0001]

# fitting data in the curve fit
# formatting the bounds to fit bewlow the values lower bound upper bounds
popt, pcov = curve_fit(GoSModel, xdata, ydata, p0=InitialValues, bounds=([ydata[-1],0.0001], [250,200]))
# lower bounds ydata, 0.0001 below
# upperbounds whatever is above

# now to make predicted guess
x_guess = xdata[-1]+10 # intial guess
# calculate the prediction for the Gos Model and output
y_pred = GoSModel(x_guess, *popt)

# hard code in the true value for visual comparison
print("The True value for the  input 3 is :" ,83 )
print('-----------------------------------------')
print("From Input 3, the GoS Model prediction was : (", x_guess, ',', y_pred, ")")
# finding the score for the gos model
GO_S_score = popt
print('From Input 3, The GoS Model Score was      :', popt[0])


#plot the data
plt.plot(xdata, ydata, 'bo', label='data')
plt.plot(xdata, GoSModel(xdata, *popt), '-', label='Go-S Data')
# plotting the scattered guesses
plt.scatter ([x_guess], [y_pred], color = 'green')
plt.legend() # legend for better understanding
# done with the first


# now we are plotting for the curve fit of the go model second model 
popt, pcov = curve_fit(GoModel, xdata, ydata, p0=InitialValues, bounds=([ydata[-1],0.0001], [500,180]))
# lower bounds ydata, 0.0001 below
# upperbounds whatever is above


# now to make predicted guess
x_guess = xdata[-1]+10 # intial guess
# calculate the prediction for the Gos Model and output
y_pred = GoModel(x_guess, *popt)
print("From Input 3, The Go Model Prediction was  : (", x_guess, ',', y_pred, ")")
GOScore = popt
print('From Input 3, the Go Model Score  was     :', popt[0])
print("==================================================================\n")


#plot the data for go model
plt.title("SRGM3")
plt.plot(xdata, GoModel(xdata, *popt), '-', label='Go Data')
# plotting the scattered guesses
plt.scatter ([x_guess], [y_pred], color = 'red')

#creating labels for the graph
plt.xlabel('x')
plt.ylabel('y')
plt.legend() # legend for better understanding
plt.savefig("plot3.pdf")
# next data done with this
# clear the data so can plot clean again
plt.clf()

# for score compariosn
if(GO_S_score[-1] >= GOScore[-1]):
    print("The Model with the best GOS Score was :",GO_S_score[-1])
    print('The Predicted Score Value was         :',(GO_S_score[0]))
else:
    print("The Model with the best G-O Score  was:", GOScore[-1])
    print('The Predicted Score Value was         :',GOScore[0])
print(" However, As we will see in a minute, the Yamada     ")
print('We get the most accurate almost spot on value      \n")
print("=====================================================")

# for extra credit, we visualize the yamada and we see that 
# with yamada the true value was 248 which is only 3 points less
# that the true value prediction for the go models
my_data = np.genfromtxt('srgm2.txt', delimiter='')
my_data = my_data[my_data[:,0].argsort()]

#make it 1xN data instead of Nx1
xdata = my_data[:,0].transpose()
ydata = my_data[:,1].transpose()
# next is creating the data
# now for the yamada extra credit
InitialVals=[ydata[-1],0,0.0001]
popt, pcov = curve_fit(Yamada, xdata, ydata, p0=InitialVals, bounds=([ydata[-1], 0, 0.0001], [500, 500, 1]))
print('From Imput 2, The Score of the Yamada Model is:', popt[0])
x_guess = xdata[-1]+10 # intial guess
y_pred = Yamada(x_guess, *popt)
print("From Input 2, The Yamada Model Prediction was : (", x_guess, ',', y_pred, ")")
plt.plot(xdata, Yamada(xdata, *popt), '-', label='Yamada')
plt.scatter ([x_guess], [y_pred], color = 'Lime')

plt.plot(xdata, ydata, 'bo', label='data')
plt.title("Yamada Expression")
plt.xlabel('x')
plt.ylabel('y')
plt.legend() # legend for better understanding
plt.savefig("Yamada.pdf")
