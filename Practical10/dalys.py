import os
import pandas as pd
import matplotlib.pyplot as plt

# Set your file path
os.chdir("C:/Users/CXB/Desktop/IBI/IBI1_2025-26/Practical10")
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

# show the third and fourth column for the first 10 rows(in total)
print("=========show the third and fourth column for the first 10 rows(in total)===============")
print(dalys_data.iloc[0:10,2:4])
'''
first_ten_years = dalys_data.iloc[0:10,2:4]
print(first_ten_years.describe())
'''
# Zimbabwe use booleans to access entries: MARKER
# print(dalys_data.loc[2:4,"Year"])
print("===========Show all the years DALYs was recorded for Zimbabwe==========")
countries = dalys_data.loc[:,"Entity"]
for c in countries.index:
    if dalys_data.loc[c,"Entity"] == "Zimbabwe":
        print(dalys_data.loc[c,"Year"])

print("===========Examine situations across countries/regions: max and min DALYs=============")
data_2019 = dalys_data.loc[dalys_data.Year == 2019,["Entity","DALYs","Year"]]
max_DALYs = data_2019['DALYs'].max()
min_DALYs = data_2019['DALYs'].min()
max_country = data_2019.loc[data_2019['DALYs'] == max_DALYs,'Entity']
min_country = data_2019.loc[data_2019['DALYs'] == min_DALYs,'Entity']
print("In year 2019, the country/region with maximum DALYs is:",max_country.values[0])
print("In year 2019, the country/region with minimum DALYs is:",min_country.values[0])


# PLOT 1: Singapore (Figure 1)
plt.figure(1)
sing_data = dalys_data[dalys_data['Entity'] == 'Singapore']
plt.plot(sing_data.Year, sing_data['DALYs'], 'r+')
plt.title("Singapore DALYs Over Time")
plt.xlabel("Year")
plt.ylabel("DALYs")


# PLOT 2: distribution of DALYs across countries and regions in 2019
data_2019_sort = data_2019.sort_values(by="DALYs", ascending=True)
plt.figure(2, figsize=(20, 6))  # Create second window
plt.bar(range(len(data_2019_sort)), data_2019_sort['DALYs'], width=0.6)
plt.title('2019 DALYs Distribution Across All Countries and regions')
plt.ylabel('DALYs')
plt.xlabel('Country and region')
plt.xticks(range(len(data_2019_sort)), data_2019_sort['Entity'], rotation=90, fontsize=5)
plt.tight_layout()

# Show both plots at the same time
plt.show()