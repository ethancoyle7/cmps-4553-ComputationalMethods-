#######################################################
### Ethan coyle                                      ##
###  Instructor:  Dr.StringFellow                    ##
###  Class     :  CMPS 4553Computational Methods     ##
###  Assignment:  in class programming assignment    ##
###  Date      :  Spetember 16 2021                  ##
#######################################################


#Note:  Due to privacy and logistic issues, only physicochemical (inputs) and sensory (the output) variables are available (e.g. there is no data about grape types, wine brand, wine selling price, etc.)
import csv
import statistics
import numpy as np

#open winequality-red.csv file
with open("winequality-red.csv",'r') as f:
  wines=list(csv.reader(f,delimiter=';')) # reading file the semicolon is the separator


# practice with slicing 
#reading the first three lines
#print first 3 rows to make sure everything read properly, note wines is a list of lists pf strings
print(wines[:3],"\n")

#find the average quality of wines
#extract the last column after the header row
#convert each extracted element to a float and assign to list qualities
qualities =[float(item[-1]) for item in wines[1:]]

# item is a row and interested in the one from the end


QualIndex= wines[0].index("quality")
print("The collum for the Quality is ",QualIndex)
#looking for the index holding the string and data for qualitity
#get the location of the quality column in wines header


#print the quality column
#compute and print the mean
QualityMean = statistics.mean(qualities)
print("The mean of our Wine Qualitiy is :","{:.2f}".format(statistics.mean(qualities)))
print("--------------------------------------------------\n")

#create a numPy array by passing the list of lists wines into the array function, excluding the header row with list slicing
#specify dtype as a float
#creating an array in numpy  
redwines = np.array(wines[1:], dtype=np.float64)
print("Our Numpy Array for Our Wines\n")

print(redwines)


#print the shape property of the NumPy array
print("--------------------------------------------------\n\n")
print("The shape of our Numpy Array For redwines = ", redwines.shape)


qualities= np.array([row[QualIndex] for row in redwines])
print("The First Three Qualities Are ", qualities[:3],"\n")
print("--------------------------------------------------\n")
#print the shape property of the NumPy array

#print the first 3 rows of qualities


#print the sum of the quality ratings and the mean using numpy
print("Sum is  ","{:.2f}".format(np.sum(qualities)))
print("AVG is  ","{:.2f}".format(np.mean(qualities)))
print("--------------------------------------------------\n\n")

#good wines will be a boolean
#print number of high quality ratings
GoodWines = qualities >= 7 # for each item compare it to 7
print("The Number of High Qualitiy Red Wines is ", \
         np.count_nonzero(GoodWines))
print("--------------------------------------------------\n\n")

#change all the qualities < 7 to 0 and print out first 10 rows
Changes = np.where(GoodWines,qualities, 0)
print("Changes Are : ", Changes[:10])

indicies = np.nonzero(Changes) # this returns a tuple  which inside is array and the data type
GoodWineData = qualities[indicies] # returns array

#print out indicies from index 0 to 10
for i in range(np.count_nonzero(GoodWines)):
  print(" In Row ", (indicies[0])[i],"We Had a Wine Quality of ", GoodWineData[i], "\n")

## Read directly in to numpy array instead of reading like aBOVE
white_wines = np.genfromtxt("winequality-white.csv", delimiter=";", skip_header=1)
print("--------------------------------------------------\n\n")
print(" Our Shape of White Wines is Now ", white_wines.shape)
white_wines =np.array(wines[1:],dtype =np.float64)

if white_wines.shape[1]== redwines.shape[1]:
  print(" Our shapes are the same\n")
else:
  print("They are not the same\n")
#printing out the shape of wines
allwines=np.vstack((redwines,white_wines))
print("They shape of our wines are ", allwines.shape)




