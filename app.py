import pandas as pd
import datetime
# load data
df  = pd.read_csv('docs\database.csv')

add_year = lambda str: str.split("/")[-1].split('-')[0]

df["Year"] = df.Date.apply(add_year)
# print data
df2 = df[['Date', 'Latitude', 'Longitude', 'Type', 'Depth', 'Magnitude', 'Magnitude Type', 'ID', 'Year']]

df_quake_freq = df2.groupby(['Year'])['ID'].count().reset_index().rename(columns={'ID': 'Counts'})

print(df_quake_freq.head())

df_max = df2.groupby(['Year'])['Magnitude'].max().reset_index().rename(columns={'Magnitude': 'Max Magnitude'})

print(df_max.head())

df_avg = df2.groupby(['Year'])['Magnitude'].mean().reset_index().rename(columns={'Magnitude': 'Avg Magnitude'})

print(df_avg.head())

df_full = df_quake_freq.set_index('Year').join(df_max.set_index('Year')).join(df_avg.set_index('Year'))

print(df_full)