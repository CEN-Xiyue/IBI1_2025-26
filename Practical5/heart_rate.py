# 1. create a list of patients' heart rates
heart_rates	= [72,60,126,85,90,59,76,131,88,121,64]
# 2. print number of patients and mean heart rate
mean_heart_rates = sum(heart_rates)/len(heart_rates)
print("The number of patients: ",len(heart_rates))
print("The mean heart rate is:",mean_heart_rates)
# 3. count the number of patients in each category and determine which category has the biggest number of patients
low = 0
normal = 0
high = 0
for i in heart_rates:
    if i < 60:
        low += 1
    elif i<=120:
        normal += 1
    else:
        high += 1
num_dict = {'low':low,'normal':normal,'high':high}
max_count = max(num_dict, key = num_dict.get)
print("The number of patients in low(heart rate<60 bpm):",low)
print("The number of patients in normal(heart rate: 60~120 bpm):",normal)
print("The number of patients in high(heart rate>120bpm):",high)
print("The category with the most number of patients is:",max_count)

# 4. created a pie chart, report the number of patients for each category
import matplotlib.pyplot as plt
labels = []
for key, value in num_dict.items():
    labels.append(key + " (" + str(value) + " patients)")
sizes =list(num_dict.values())
explode = (0,0.1,0)
plt.pie(sizes,explode=explode, labels=labels,autopct='%1.1f%%',shadow = False, startangle = 90)
plt.axis('equal')
plt.title('Portion and number of paitients in each category')
plt.show()