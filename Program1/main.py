#############################################################
##                                                         ##
## Author     :  Ethan Coyle                               ##
## Instructor :  Dr.StringFellow                           ##
## Class      :  Computational Methods CMPS 4553           ##
## Assignment :  Project 1 File Indexer                    ##
##                                                         ##
## for example purposes, I am creating a four file reader  ##
## thus by doing so, I will be indexing multiple DataFile  ##
## properly integrate a file indexer for ripe pickling and ##
## unpickling                                              ##
#############################################################

FileStrings = set()

DataFile = ['Crazy.txt','Things.txt','People.txt','Fun.txt']
FileIndexer = {}## placeholder for the desired output 
#each file contains ten lines of random sentances
print("The listed Files we are Reading From is : \n",DataFile,"\n")
print("We are going to sample the text from one of the Files \n")
print("------------------------------------------------------")

#Visual for the user to see contents of one of our files
a_file = open("Things.txt")
print("The Contents of the Things.Txt File is : \n") 
lines = a_file. readlines()
for line in lines:
    print(line)
print("------------------------------------------------",
  "---------------------------")
##with the opening of the datafiles, we get the FileStrings inside of the 
## files and then we output the string of indexes even ones with 


for f in DataFile:
  #with opening, we need to  open as read online
    with open(f,'r') as file:
        for line in file:
          # to read throught the file create split to read 
          #through the white space and on to the next word
            for data in line.split():
                FileStrings.add(data)

# Now to check and see if the FileStrings are present in other fikes
# according to our program, 
for data in FileStrings:
    FileIndexer[data] = []## where the word is occuring
    for f in DataFile:
        with open(f,'r') as file:##when opening and reading the 
            for line in file: # for each line chek the data
                if data in line:
                  ## add element to the list by appending 
                    FileIndexer[data].append(f)
                    

# printing the FileIndexer
# in tune with the example if the occured words occur in multiple filter
#will join them in the indexing whenever they occur multiple times
print("After perusing All our files, We will display the Index Files \n\n",FileIndexer,"\n\n")
print("As we can see our indexer is taking the words inside of our ",
  "files and if it occurs multiple times it is shown where they",
  "occur and also will display if the word only shows up in one file\n")
