# 1. Store the data
pop = {'UK':(66.7,69.2),'China':(1426,1410),'Italy':(59.4,58.9),'Brazil':(208.6,212.0),'USA':(331.6,340.1)}

# 2. Calculate the growth rate
gr = {}
for country,(pop20,pop24) in pop.items():
    rate = round((pop24 - pop20)/pop20 * 100,2)
    gr[country] = rate
# 3. Print the population data in descending order
print("The population growth rates are as follows(in descending order:)")
for country in sorted(gr,key=gr.get,reverse = True):
    print(country, ":", gr[country], "%")

# 4. print the countries with the largest increase and decrease
compare = (gr)
max_count = max(compare, key = compare.get)
min_count = min(compare, key = compare.get)
print("The country with the largest population growth rate is:",max_count)
print("The country with the largest population decreasing rate is:",min_count)
# 5. create a bar chart that shows pop changes 
import numpy as np
import matplotlib.pyplot as plt
N = len(pop)
growthrate = np.array(list(gr.values()))
country_names = list(pop.keys())
ind = np.arange(N)
width = 0.4
pl = plt.bar(ind,growthrate, width)
plt.ylabel('Growth rate')
plt.title('	Population growth rate of several countries from 2020-2024')
plt.xticks(ind, country_names)
plt.show()
