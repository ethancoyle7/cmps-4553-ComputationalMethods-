######################################################
## Author:       Ethan Coyle                        ##
## Instructor:    Dr StringFellow                   ##
## Class     :    CMPS 4553-Computational Methods   ##
## Class Time:    Tuesday,Thursday 9:30AM           ##
## Assignment:    Homework 1 and 2                  ##
## Due Date  :    Thursday September 2, 2021        ##
######################################################

# The purpose of this program is to create a simple 
# Hello World Program as well as a summation of 
# two numbers

##Part 1 : Hello World
print("Hello World")


#part 2: summation of 2 numbers

#user input 2 numbers
Num1 = input(" Please Enter the First Number: ")
Num2 = input(" Please Enter the second number: ")

# Using arithmetic + Operator to add two numbers
#read in as a string and converted to int or else
#will concatinata as a string input
sum = int(Num1) + int(Num2)

#print the result
print("The summation of ",Num1," and ",Num2," is: ",sum )
