import os # allows to work with different files and directoris
import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as py 

# change to the directory of where the file is stored
os.chdir("C:/Users/CXB/Desktop/IBI/IBI1_2025-26/Practical10")
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")
'''
print(dalys_data.head(5))
print(dalys_data.info())
print(dalys_data.describe())


print("========================")
print(dalys_data.iloc[0,3])

print("========================")
print(dalys_data.iloc[2,0:5])
print("========================")
print(dalys_data.iloc[0:2,:])
print("========================")
print(dalys_data.iloc[0:10:2,0:5])


# show the third and fourth column for the first 10 rows(in total)

print("========================")
print(dalys_data.iloc[0:10,2:4])
first_ten_years = dalys_data.iloc[0:10,2:4]
print(first_ten_years.describe())

# Zimbabwe use booleans to access entries: MARKER
# print(dalys_data.loc[2:4,"Year"])


countries = dalys_data.loc[:,"Entity"]
for c in countries.index:
    if dalys_data.loc[c,"Entity"] == "Zimbabwe":
        print(dalys_data.loc[c,"Year"])
'''
# Examine situations across countries: max and min DALYs
print("===========Examine situations across countries: max and min DALYs=============")
data_2019 = dalys_data.loc[dalys_data.Year == 2019,["Entity","DALYs","Year"]]
max_DALYs = data_2019['DALYs'].max()
min_DALYs = data_2019['DALYs'].min()
max_country = data_2019.loc[data_2019['DALYs'] == max_DALYs,'Entity']
min_country = data_2019.loc[data_2019['DALYs'] == min_DALYs,'Entity']
print("In year 2019, the country with maximum DALYs is:",max_country.values[0])
print("In year 2019, the country with minimum DALYs is:",min_country.values[0])

#choose one country from above and extract DALYs
# choose Singapore
print("===========DALYs plot for Singapore=============")
sing_data = dalys_data[dalys_data['Entity'] == 'Singapore']
plt.plot(sing_data.Year,sing_data['DALYs'],'r+')
plt.show()
