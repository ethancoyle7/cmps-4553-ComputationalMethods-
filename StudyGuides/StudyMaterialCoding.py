import pandas as pd
import numpy as np


# now to read through sorting
 
data = {'Brand': ['Hyundai','Toyots','Ford','Audi','Mercedes'],
        'Price': [22000,25000,12000,35000,90000],
        'Year': [2015,2013,2018,2018,2003],
        'Carrots': [5,200,50000,3,87]
        }
 
df = pd.DataFrame(data, columns=['Brand','Price','Year','NumCarrots'])

# sort Brand in an ascending order
df.sort_values(by=['Brand'], inplace=True)
print (df)
df.sort_values(by=['Price'],inplace=True,ascending=True)
print(df)

# cutting into bins 
# readout is similar organizing on collumn name price 
# if the price is 0 to 10000 then low
# if the price if 10000 to 20000 then medium
# if price is 20-40000 average and anything past that is expensive
print("\r Now we gonna cut into bins the result list and label them  on their price point ")
print("\r\n Here is our orignal list\n", df,'\n')
result= pd.cut(
    df['Price'], 
    bins=[0, 10000, 20000, 40000,100000], 
    labels=['Low', 'Medium', 'Average', 'too Expensive'],
    ordered=True
)
print("\r\n And here is out cut and bin of the price point\n\n")
print(result)
# cutting and organizing on bins of year
resultyear= pd.cut(df['Year'], bins=[2000,2005,2010,2015,2020],labels=['clunker','semiclunker','junk','fancy'],ordered=False)

print(resultyear,"\n\n")


# sorting index

s = pd.Series(['a', 'b', 'c', 'd'], index=[3, 2, 1, 4])
s.sort_index(ascending=True, inplace=True)
print(s)

carrotstick = pd.DataFrame([[np.nan, 2, np.nan, 0],
                   [3, 4, np.nan, 1],
                   [np.nan, np.nan, np.nan, 5],
                   [np.nan, 3, np.nan, 4]],
                  columns=list("ABCD"))
print("\r\n Our Data Fram before filling in the nan value is : \n", carrotstick, "\r\nAnd after the fill \n\n")
# filling the nan values with name of the data frame.FILLNA
# then replaceing with value and then to keep it in
# place set the inplace to true
# then print out the results
carrotstick.fillna(1,inplace=True)
print(carrotstick)

print("\r\n Now We gonna show merging\n\n")

left = pd.DataFrame({
   'id':[1,2,3,4,5],
   'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
   'subject_id':['sub1','sub2','sub4','sub6','sub5']})
right = pd.DataFrame(
   {'id':[1,2,3,4,5],
   'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
   'subject_id':['sub2','sub4','sub3','sub6','sub5']})

print("First Data Fram is \n", right)
print("\nSecond Data Fram is : \n", left)

print("\r\n Now merged on id \n\n")
print (pd.merge(left,right,on='id'))
print (pd.merge(left, right, on='subject_id', how='left'))
print ("How= right\n", pd.merge(left, right, on='subject_id', how='right'))

print(pd)




df = pd.DataFrame(np.random.randn(20, 2), columns=list('AB'))
df['Tenant'] = np.random.choice(['Frodo', 'Bilbo','Sam the Brave','Bilbo', ''], 20)
print(df)

# on any empty space put in a np.nan inside inplace is true to hold the values
# now demonstrating dropping empty rows
# in pandas dataframe
print("\r\n We replace all the empty cells with np.nan\n To be able to drop the row with empyth cells\n")
df['Tenant'].replace('', np.nan, inplace=True)
print(df)

df.dropna(subset=['Tenant'], inplace=True)
print("\r\n With the dropped collumns :\n",df)

print("\r\n Now we gonna demonstrate summing up rows and\nputting them in new collum\n")
df = pd.DataFrame({'Col A': [1,2,3], 'Col B': [2,3,4], 'Col C':['dd','ee','ff'], 'Col D':[5,9,1]})
# create new collum named sum of rows and for each row place sum of that row and the collum will go on the axis 1 which is the top for co
df['Sum of Rows'] = df.sum(axis=1)
print("\r\n With New Collum E to hold the sum of each row\n", df)

# setting index values
print("\r\n We are now going to set the index display\n")

#initialize a dataframe
df = pd.DataFrame(
	[[21, 'Bilbo', 72, 67],
	[23, 'Chinky', 78, 69],
	[32, 'chunky', 74, 56],
	[52, 'potatoes', 54, 76]],
	columns=['rollno', 'name', 'physics', 'botony'])

print('DataFrame with default index\n', df)

#set column as index
df = df.set_index('rollno')

print('\nDataFrame with column as index\n',df)
df.sort_values(by=['physics'],inplace=True,ascending=True)
print("\r\n Here we gonna sort on the physics number :\n",df)

df.sort_values(by=['rollno'],inplace=True,ascending=True)
print("\r\n Now we sorting on the roll number\n",df)


# cerate new collum sum the value and place in new collumn
df['Sum of Rows'] = df.sum(axis=1)
print("\r\n With New Collum E to hold the sum of each row\n", df)

print("\r\n No we gonna set the index name:\n")
my_df = pd.DataFrame({
    'Applicant': ['Ratan', 'Anil', 'Mukesh', 'Kamal'],
    'Hometown': ['Delhi', 'Pune', 'Dhangadi', 'Kolkata'],
    'Score': [85,87,90,89],},index=["cheese","potatoes","cherrybutt","penguinsuit"])
print("\r\nour old index name is :", my_df.index.name, "\n")
print("Initial DataFrame:")
print(my_df,"\n")

my_df.index.name="Date"

print("DataFrame after setting the name of Index Column:")
print(my_df,"\n")
print(" our new index name is :", my_df.index.name)
my_df.sort_values(by=["Score"],inplace=True,ascending=True)
print("With the sorted\n",my_df)
