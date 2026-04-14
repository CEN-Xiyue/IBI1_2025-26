import numpy as np
import matplotlib.pyplot as plt

# initialize totol population, initial infection, infection pro, revocery pro
N = 10000
beta = 0.3
gamma = 0.05
I = 1
R = 0
S = 9999

time = 1000
# history lists
S_initial = [S]
I_initial = [I]
R_initial = [R]

# repeat 1000 times
for _ in range(time):
    I_new = 0       
    for _ in range(S):
        if np.random.random() < beta*(I/N):
            I_new = I_new + 1
    R_new = 0   
    for _ in range(I):
        if np.random.random() < gamma:
            R_new += 1
                
    S = S - I_new
    I = I + I_new - R_new
    R = R + R_new

    S_initial.append(S)
    I_initial.append(I)
    R_initial.append(R)
         
# Plot
plt.figure(figsize=(6,4), dpi=150)
plt.plot(S_initial, label='Susceptible')
plt.plot(I_initial, label='Infected')
plt.plot(R_initial, label='Recovered')
plt.xlabel('Time')
plt.ylabel('Number of people')
plt.title('SIR model')
plt.legend()
plt.savefig("SIR model.png", dpi=150, bbox_inches="tight")
plt.show()