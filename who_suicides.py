# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 22:12:21 2019

@author: black
"""
import pandas as pd
from helper_funcs import to_categorical
import seaborn as sns
import matplotlib.pyplot as plt
suicides = pd.read_csv(r'Toy Data\who_suicide_statistics.csv')
#print(suicides.info())
#print(suicides.isna().sum()) #population and suicides have NAs
to_categorical(suicides)  #to improve memory requirements

print(suicides.country.unique()) #141 unique countries

suicides.rename(columns={'suicides_no': 'suicides', 'sex':'gender'}, inplace=True)
#suicides.suicides.fillna(value=0, inplace=True) #Does not make sense to assume this
suicides.dropna(inplace=True)

by_gender=suicides.groupby('gender').sum()
by_age = suicides.groupby('age').sum()
by_gender[['suicides']].plot(kind='bar'); 
plt.title('Suicides by gender'); plt.ylabel('Suicides'); plt.show()

by_age.plot.pie(y='suicides', autopct='%1.1f%%', figsize=(6,8)); plt.show()

by_country_year = suicides.groupby(['country', 'year']).sum().dropna()
by_country_year['normalized'] = (by_country_year['suicides'] / by_country_year['population'])*100

by_country_year.reset_index(inplace=True)
by_country = suicides.groupby('country').sum().drop(columns=['year', 'population'])
top_countries = by_country.sort_values(by='suicides',ascending=False).index.values.tolist()[0:15]
legend = top_countries
by_country_year.set_index(keys='country', drop=True, inplace=True)
top_countries = by_country_year.loc[top_countries]
plt.figure(figsize=(14,9))
plt.title('Aggregate Suicide Statistics over last 35 years')
g = sns.lineplot(x="year", y="suicides", hue="country", data=top_countries.reset_index(),
                 hue_order=legend); plt.show()

by_year = suicides.groupby(['year']).sum().drop(columns=['population']).reset_index()
plt.figure(figsize=(15,5))
plt.title('Suicides over year, aggregated')
plt.xticks(rotation=90)
sns.barplot(x='year', y='suicides', data=by_year)

#More detailed breakdown by age in RU, US, Japan ie the three most problematic ones as seen above
most_problematic_countries=suicides.set_index('country',drop=True).loc[legend[:3]] 
for country in legend[:3]:
    selected=most_problematic_countries.loc[country]
    #plt.title('Suicides per age in {}'.format(country))
    selected.groupby('age').sum()[['suicides']].sort_values(by='suicides').plot(kind='bar')
    plt.title('Suicides per age in {}'.format(country))
    plt.ylabel('Suicides total')
    plt.show()
