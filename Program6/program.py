
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


# create subplots 4 boxes to hold the cruve plots for best fit share the y and x axis
matplotlib.style.use("ggplot")

# read in the first file
# delimter must be space there is no comma inside of infiles
my_data = np.genfromtxt('input1.txt', delimiter='')
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
x_guess = 10 # intial guess
# calculate the prediction for the Gos Model and output
y_pred = GoSModel(x_guess, *popt)
print("Prediction For GoSModel on input 1 is : (", x_guess, ',', y_pred, ")")


#plot the data
plt.plot(xdata, ydata, 'bo', label='data')
plt.plot(xdata, GoSModel(xdata, *popt), '-', label='Go-S Data')
# plotting the scattered guesses
plt.scatter ([x_guess], [y_pred], color = 'red')
plt.legend() # legend for better understanding
# done with the first


# now we are plotting for the curve fit of the go model second model 
popt, pcov = curve_fit(GoModel, xdata, ydata, p0=InitialValues, bounds=([ydata[-1],0.0001], [500,180]))
# lower bounds ydata, 0.0001 below
# upperbounds whatever is above

# now to make predicted guess
x_guess = 10 # intial guess
# calculate the prediction for the Gos Model and output
y_pred = GoModel(x_guess, *popt)
print("Prediction For Go-Model on input 1 is : (", x_guess, ',', y_pred, ")")
     
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
plt.cla()
plt.close()
# now on for the second srgm file

my_data = np.genfromtxt('input2.txt', delimiter='')
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
print(popt)
# lower bounds ydata, 0.0001 below
# upperbounds whatever is above

# now to make predicted guess
x_guess = 10 # intial guess
# calculate the prediction for the Gos Model and output
y_pred = GoSModel(x_guess, *popt)
print("Prediction For GoSModel on input 2 is : (", x_guess, ',', y_pred, ")")


#plot the data
plt.plot(xdata, ydata, 'bo', label='data')
plt.plot(xdata, GoSModel(xdata, *popt), '-', label='Go-S Data')
# plotting the scattered guesses
plt.scatter ([x_guess], [y_pred], color = 'red')
plt.legend() # legend for better understanding
# done with the first


# now we are plotting for the curve fit of the go model second model 
popt, pcov = curve_fit(GoModel, xdata, ydata, p0=InitialValues, bounds=([ydata[-1],0.0001], [500,180]))
# lower bounds ydata, 0.0001 below
# upperbounds whatever is above

# now to make predicted guess
x_guess = 10 # intial guess
# calculate the prediction for the Gos Model and output
y_pred = GoModel(x_guess, *popt)
print("Prediction For Go-Model on input 2 is : (", x_guess, ',', y_pred, ")")
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
plt.cla()
plt.close()

# now for the third input file
my_data = np.genfromtxt('input3.txt', delimiter='')
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
x_guess = 10 # intial guess
# calculate the prediction for the Gos Model and output
y_pred = GoSModel(x_guess, *popt)
print("Prediction For GoSModel on input 3 is : (", x_guess, ',', y_pred, ")")


#plot the data
plt.plot(xdata, ydata, 'bo', label='data')
plt.plot(xdata, GoSModel(xdata, *popt), '-', label='Go-S Data')
# plotting the scattered guesses
plt.scatter ([x_guess], [y_pred], color = 'red')
plt.legend() # legend for better understanding
# done with the first


# now we are plotting for the curve fit of the go model second model 
popt, pcov = curve_fit(GoModel, xdata, ydata, p0=InitialValues, bounds=([ydata[-1],0.0001], [500,180]))
# lower bounds ydata, 0.0001 below
# upperbounds whatever is above

# now to make predicted guess
x_guess = 10 # intial guess
# calculate the prediction for the Gos Model and output
y_pred = GoModel(x_guess, *popt)
print("Prediction For Go-Model on input 3 is : (", x_guess, ',', y_pred, ")")
print("==================================================================\n")


#plot the data for go model
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
plt.cla()
plt.close()
