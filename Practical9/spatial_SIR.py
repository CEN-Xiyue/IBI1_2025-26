import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
population = np.zeros((100,100))
outbreak = np.random.choice(range(100),2)
population[outbreak[0],outbreak[1]] = 1
grid_size = 100
beta = 0.3
gamma = 0.05
times = 100 # run for 100 times
# Adapted from Practical 9 materials
# find infected points
infectedIndex = np.where(population==1)
# loop through all infected points
for _ in range(times):
    new_infections = np.zeros_like(population)
    infectedIndex = np.where(population == 1)
    for i in range(len(infectedIndex[0])):
        # get x, y coordinates for each point
        x = infectedIndex[0][i]
        y = infectedIndex[1][i]
        # infect each neighbour with probability beta
        # infect all 8 neighbours
        for xNeighbour in range(x-1,x+2):
            for yNeighbour in range(y-1,y+2):
                # don't infect yourself! (Is this strictly necessary?)
                if (xNeighbour,yNeighbour) != (x,y):
                    # make sure I don't fall off an edge
                    if xNeighbour != -1 and yNeighbour != -1 and xNeighbour!=100 and yNeighbour!=100:
                        # only infect neighbours that are not already infected!
                        if population[xNeighbour,yNeighbour]==0:
                            population[xNeighbour,yNeighbour]=np.random.choice(range(2),1,p=[1-beta,beta])[0]
    
    new_recoveries = np.zeros_like(population)
    infectedIndex = np.where(population == 1)
    for i in range(len(infectedIndex[0])):
        x = infectedIndex[0][i]
        y = infectedIndex[1][i]
        if np.random.random() < gamma:
            new_recoveries[x, y] = 1

    population[new_infections == 1] = 1
    population[new_recoveries == 1] = 2

# Plot final result
# 0 = blue (susceptible)
# 1 = yellow (infected)
# 2 = purple (recovered)
plt.figure(figsize=(6, 4), dpi=150)
plt.imshow(population, cmap='viridis', interpolation='nearest')
plt.title(f'2D Spatial SIR after {times} steps\nBeta=0.3, Gamma=0.05')
plt.xlabel('X Coordinate')  
plt.ylabel('Y Coordinate')  
plt.xticks([0, 25, 50, 75, 100])  
plt.yticks([0, 25, 50, 75, 100])


plt.show()
