# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 22:12:21 2019

@author: black
"""
import pandas as pd
from helper_funcs import to_categorical
import seaborn as sns
suicides = pd.read_csv(r'Toy Data\who_suicide_statistics.csv')
#print(suicides.info())
#print(suicides.isna().sum()) #population and suicides have NAs
to_categorical(suicides)  #to improve memory requirements

print(suicides.country.unique()) #141 unique countries

suicides.rename(columns={'suicides_no': 'suicides', 'sex':'gender'}, inplace=True)
#suicides.suicides.fillna(value=0, inplace=True)
suicides.dropna(inplace=True)

#populations_na = suicides[suicides.population.isna()]
#populations_na_grouped=populations_na.groupby(['country', 'age']).count()


##1985, IN order of countries na
#pops = [7293, 56898, 6212000, 13304, 19313, 73643, 6489000,
# 1850, 6384000, 4281000, 15580000, 2896000, #Jordan last
# 15600000, 28835, 10792, 22540000, 12025, 3709000,  #nicaragua last
# 15000, 19540000,  41669, 42013, 6024, 22708, 13019000, #Saudi arabia last
# 10650000, 4538000, 7322000, 9506, 8659000]
# 
# 
# #occupied palestinian 15000 is made up
# #rodriguez 41669 is a 2014 number
#countries_na = populations_na.country.unique()
#pops_basis = dict(zip(countries_na, pops)) 
#suicides['suicides_percent'] = (suicides['suicides'] / suicides['population'])*100 

#suicides_per_country_annual = suicides[['country', 'suicides_percent']].groupby(by=['year']).count()
by_gender=suicides.groupby('gender').sum()
by_gender[['suicides']].plot(kind='bar')