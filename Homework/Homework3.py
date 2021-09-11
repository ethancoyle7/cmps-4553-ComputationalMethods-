###########################################################
##   Author-          Ethan Coyle                        ##
##   Instructor-      Dr. StringFellow                   ##
##   Class-           Computational Methods              ##
##   Assignment-      Homework 3                         ##
##                                                       ##
## In this program, i am demonstrating the use of calc   ##
## The mean the standard deviation for all ages groups   ##
## and the covid related deaths within a CSV File        ##
##                                                       ##
###########################################################

#importing the various mdules used in the program
import csv
import statistics
import math ## for the math.sqrt


#open file and read CsvFile
with open("CovidDeathCounts.csv") as infile:
  CsvFile = list(csv.reader(infile))

#examine header fow to find column of interest
ageIndex = CsvFile[0].index("Age")
covidDeathsIndex = CsvFile[0].index("COVID-19 Deaths")
#access field of interest in records and calculate/display stats
ages = [int(row[ageIndex]) for row in CsvFile[1:]]
deaths = [int(row[covidDeathsIndex]) for row in CsvFile[1:]]

#formatting a nice user friendly looking output will calculate the mean
#and standard deviation using the module for age collum and the covid
#death collum
print ("mean\tstdev")
print("{:.2f}".format(statistics.mean(ages)), "\t", 
      "{:.2f}".format(statistics.stdev(ages), "\n\n"))

##now calculate the sum and find the mean of people death with covid
DeathPerAge=[(float(row[ageIndex])*float(row[covidDeathsIndex])) 
  for row in CsvFile[1:]]
TotDeaths=[float(row[covidDeathsIndex]) for row in CsvFile[1:]]
MeanDeaths=sum(DeathPerAge)/sum(TotDeaths)

#now for the standard deviation
#StandDev=((float(ages)-[covidDeathsIndex])/(TotDeaths -1)).sqrt()

RunningTot= [(((float(row[ageIndex])-MeanDeaths)**2)*float(row[covidDeathsIndex]))/
        (sum(TotDeaths)) for row in CsvFile[1:]]
#take the deviation from each line create a running total and then divide
# by the sum of the total deaths and then we get our running
# total standard deviation

##time to do our running total
Col_length = len(RunningTot)
RT = float(0)

for i in range(Col_length):
  
  RT += RunningTot[i]
  
##now it is time to output the result
## use the math.sqrt to output the final standard deviaion
print("\nMean and Deviation for Covid Deaths")
print("------------------------------------\n")
print ("mean\t\t stdev")
print("----------------------")
print("{:.2f}".format(MeanDeaths),"\t\t","{:.2f}".format(math.sqrt(RT)))
