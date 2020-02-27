""" game where a dice roll dictates random steps and subsequentially,
a random walk
1) roll a dice
2) if the result is a 1 or 2, take a step back
3) if the result is a 3, 4 or 5, take a step forward
4) if the result is a 6, roll the dice again and the result
is the number of steps forward
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
np.random.seed(123)

all_walks = []
for x in range(250):
    random_walk = [0]
    for x in range (100):
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        if np.random.rand() <= 0.001: #random chance to bust my ass
            step = 0
        random_walk.append(step)
    all_walks.append(random_walk)

a_w_t = np.transpose(all_walks) #transpose to correctly handle viz
end_step = a_w_t[-1]
success = end_step > 60 #chance you'll end up above 60 steps
np.mean(success)
plt.plot(a_w_t)
plt.figure()
plt.hist(end_step)
plt.show()

""" would be interesting to show if the success rate converges to anything 
with increasing simulation runs, i.e. 100, 250, 1000 walks, etc. """
