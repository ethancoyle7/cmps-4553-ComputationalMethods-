import pandas as pd



df1 = pd.DataFrame({'user_id': ['id001', 'id002', 'id003', 'id004', 'id005', 'id006', 'id007'],
                    'Name': ['Ethan', 'Jonathan', 'Loic', 'Byron', 'Fowzy', 'Paxton', 'Sam the Brave'],
                    'LName': ['Coyle', 'Hogan', 'Konan', 'Dowling', 'The Slacker', 'Proctor', 'Avid Potatoe Lover'],
                    'FavFood': [' Cheese','Potatoe','Celery','Brocolli','Slacing','Chees Curds','Taters']
                    })
df2 = pd.DataFrame({'user_id': ['id001', 'id002', 'id003', 'id004', 'id005'],
                    'Eats Cheese?': ['Yes','yes','no','yes','brocolli']
                    })


print("our first data frame is :\n", df1)
print("\nOur second data frame is :\n", df2)

df3=pd.merge(df1,df2)
print(" Here we merging except merges all identical:\n",df3)

df4=pd.merge(df1,df2,how="left")
print("\nData frame 4 merged left\n\n",
 "Here merging left, will merge all the rows together so anything from both data frams will be together and anything not matching in the collumns will be replaced witha Nan value\n\n",df4)
df4.sort_values(by=['Name'], inplace=True)
print("\n\nNow sorted on the names:\n" ,df4)

df5=pd.merge(df1,df2, how='right')
print(" Now Merged Right we get :\n",df5)


df_left = pd.merge(df1, df2, how='left', indicator=True)
print(" Now we gonna show outter left merging Indicator will say is found in one or both\n:",df_left)

df_outer = pd.merge(df1, df2, how='outer', indicator=True)

print(" Now printing outter as how: and indicator to see where what appears:\n",df_outer )

df_inner = pd.merge(df1, df2, how='inner', indicator=True)
print("Now we gonna see the inner\n:", df_inner)
# will print inside to right of id if there a match and then eats cheese will be on the outside think as a sandwhich
