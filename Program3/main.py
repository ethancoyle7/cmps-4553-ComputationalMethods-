
#====================================================================================================================#
#                                                                                                                    #
#  Author - Ethan Coyle                                                                                              #
#  Instr  - Dr. StringFellow                                                                                         #
#  Class  - CMPS 4553- Computational Methods                                                                         #
#  Assign - Program 3(alcohol consumption in 2018)                                                                   #
# ===================================================================================================================#
#  Program Guidelines -                                                                                              #
#                                                                                                                    #
#   data files for the GDB Growth of Countries by percentage from 2000-2020 and for Alcohol Consumption for          #
#   Countries from 3 years ago (2018).    You are to write a program that uses pandas and this data to merge         #
#   and cross-tabulate GDP level (2-bins: above average vs. below average) vs. alcohol consumption level (2 bins:    #
#   above average vs. below average) for the year 2018.  Use the total_litres_of_pure_alcohol column.Do the two      #
#   measures seem correlated?To answer this, count the number of times the GDP level == Alcohol consumption level    #
#   (in terms of the bins they are in).Compute a % of the number of agreements, eg. 72.5%? Print out the percentage. #
#   Note, clean up the data before processing (may be some ..'s values). Replace these with mean of the clean        #
#   values in the column. Output should print first 10 and last 10 rows of the dataframe sorted in order of GDP in   #
#   descending order.                                                                                                #
# ===================================================================================================================#
# ===================================================================================================================#
# import the pandas and the numpy for utilization in program
import pandas as pd
import numpy as np

# first we need to read in the Panda for gdp growth
GDP = pd.read_csv("GDPGrowth2000-2020.csv")
# edit the index to be reading the index for Country column
# GDP = GDP.reset_index().set_index('Country')
GDP = GDP.set_index('Country')
# set all the country names at the index to upper case
GDP.index = GDP.index.str.upper()
# Drop all the irrelevant columns including the index
GDP = GDP.drop(columns={
    "Country Code", "2000 [YR2000]", "2001 [YR2001]", "2002 [YR2002]",
    "2003 [YR2003]", "2004 [YR2004]", "2005 [YR2005]", "2006 [YR2006]",
    "2007 [YR2007]", "2008 [YR2008]", "2009 [YR2009]", "2010 [YR2010]",
    "2011 [YR2011]", "2012 [YR2012]", "2013 [YR2013]", "2014 [YR2014]",
    "2015 [YR2015]", "2016 [YR2016]", "2017 [YR2017]", "2019 [YR2019]",
    "2020 [YR2020]"
}, axis=1)
# Rename

GDP.rename(columns={'2018 [YR2018]': '2018 GDP'}, inplace=True)

# inside of the GDP Collum, replace the .. with Nan value
GDP['2018 GDP'] = GDP['2018 GDP'].replace("..", 'NaN')


# read in the csv file using pandas and then set the index to be reading from the index of country
AlcoholConsumption2018 = pd.read_csv("Alco2018byCountry.csv")
AlcoholConsumption2018 = AlcoholConsumption2018.set_index('Country')

# setting the country names to all upper case to match the GDP country names
AlcoholConsumption2018.index = AlcoholConsumption2018.index.str.upper()

# get rid of our unnecessay collums
AlcoholConsumption2018.drop(columns={"Wine", "Beer", "Spirits"}, inplace=True, axis=1)


AlcoholConsumption2018.rename(columns={'total_litres_of_pure_alcohol': '     Alc. Consumption'}, inplace=True)
# we rename the collum of the total litres of pure alcohol to a easier to read format and set the
# inplace to be true
# we need to merge the two files to be merged on the country's
mf = pd.merge(GDP, AlcoholConsumption2018, on='Country', how='outer')

# Next we need to convert the values to floating to utilize mean and the calculations
mf['2018 GDP'] = mf['2018 GDP'].astype(np.float64)
mf['     Alc. Consumption'] = mf['     Alc. Consumption'].astype(np.float64)

# Replace any of the values that hold Nan to hold the mean of column
# fill the nan values with the mean of the gdp values
mf.fillna((mf.mean()), inplace=True)

# as per guidelines, we don't use ascending order and make this inplace
mf.sort_values('2018 GDP', ascending=False, inplace=True)

# Next we organize the bins holding above and below average
# create the bins using the labeling for the Below Average and Above Average
mf['2018 GDP'] = pd.cut(mf['2018 GDP'], 2, labels=("Below Avg", "Above Avg"))

# after comparing, cut the mf and then create the labels for the bins abv and below average
mf['     Alc. Consumption'] = pd.cut(mf['     Alc. Consumption'], 2, labels=("Below Avg", "Above Avg"))
# print out ten from the head and ten from the tail
print("Our Head Displaying 10 is\n"
      "=============================================\n", mf.head(10), "\n")

print("Our Tail Displaying 10 is\n",
      "==========================================================\n", mf.tail(10))
# wherever the two files gdp and the consumption are equivalent store in equivalency countries
EquivalencyCountries = (mf['2018 GDP'] == mf['     Alc. Consumption'])
print(len(mf))
AreEqual = EquivalencyCountries.sum()
EquivalentPercent = (AreEqual / len(mf) * 100)
print("\n\nThe % of The Countries That Were Equal Was: \n", "============================================\n",
      "{:.2f}%".format(EquivalentPercent))
