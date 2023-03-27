import pandas as pd
import datetime
# load data
df  = pd.read_csv('docs\database.csv')

add_year = lambda str: str.split("/")[-1].split('-')[0]

df["Year"] = df.Date.apply(add_year)
# print data
df2 = df[['Date', 'Latitude', 'Longitude', 'Type', 'Depth', 'Magnitude', 'Magnitude Type', 'ID', 'Year']]

print(df2)


print(df2.groupby(['Year'])['ID'].count())