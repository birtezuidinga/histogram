#This is main script

import numpy as np
import matplotlib.pyplot as plt

rand = np.random.randint(1,100,1000)

fig, ax = plt.subplot(figsize = (10,5))
ax = plt.hist(x=rand, bins='auto', color='#0504aa',
                            alpha=0.7, rwidth=0.85)