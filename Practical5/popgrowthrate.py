# 1. Store the data
pop2020 = {'UK':66.7,'China':1426,'Italy':59.4,'Brazil':208.6,'USA':331.6}
pop2024 = {'UK':69.2,'China':1410,'Italy':58.9,'Brazil':212.0,'USA':340.1}
# 2. Calculate the growth rate
import numpy as np
pop2020_list = np.array(list(pop2020.values()))
pop2024_list = np.array(list(pop2024.values()))
rate_list = (pop2024_list - pop2020_list)/pop2020_list * 100
growthrate = dict(zip(pop2020.keys(), rate_list.round(2)))
# 3. Print the population data in descending order
items = list(growthrate.items())
sorted_items = sorted(items, key=lambda x: x[1])
sorted_items.reverse()
print("The population growth rates are as follows(in descending order:)")
for country, rate in sorted_items:
    print(country, ":", rate, "%")
# 4. print the countries with the largest increase and decrease
compare = (growthrate)
max_count = max(compare, key = compare.get)
min_count = min(compare, key = compare.get)
print("The country with the largest population growth rate is:",max_count)
print("The country with the largest population decreasing rate is:",min_count)
# 5. create a bar chart that shows pop changes 
import matplotlib.pyplot as plt
N = len(pop2020)
growthrate = np.array(list(growthrate.values()))
country_names = list(pop2020.keys())
ind = np.arange(N)
width = 0.4
pl = plt.bar(ind,growthrate, width)
plt.ylabel('Growth rate')
plt.title('	Population growth rate of several countries from 2020-2024')
plt.xticks(ind, country_names)
plt.show()
