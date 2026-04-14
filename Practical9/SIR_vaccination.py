import numpy as np
import matplotlib.pyplot as plt

# initialize totol population, initial infection, infection pro, revocery pro
N = 10000
beta = 0.3
gamma = 0.05
I = 1
R = 0
vac_rate = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
time = 1000

plt.figure(figsize=(6,4), dpi=150)

for vac in vac_rate:
    V = int(N*vac)
    S = 9999 - V
    R = 0
    I = 1
    I_initial = [I]
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

        I_initial.append(I)
    plt.plot(I_initial, label=f'{int(vac*100)}% vaccinated')
         
    
        
    # Plot THIS simulation's infected curve
plt.xlabel('Time')
plt.ylabel('Number of people infected')
plt.title('SIR model with different vaccination rates')
plt.legend()
plt.savefig("SIR vaccination model.png", dpi=150, bbox_inches="tight")
plt.show()