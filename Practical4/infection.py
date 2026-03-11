# 1. set the number of initially infected students, a
a = 4
# 2. set a growth rate, b
b = 0.5
# 3. set the initial condition, the infected students(infected), days(n)
infected = a
n = 0
print("Initially, there are a total of",a,"students infected, with infection at the growth rate of",b)
#4. calculate the infected students(c), use the while loop
while infected < 91:
    n += 1
    infected = a*(1+b)**n
    print("On day",n,"there are a total of",infected,"students infected")
print("It will take",n,"days for 91 students to get infected.")