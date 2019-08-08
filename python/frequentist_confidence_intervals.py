# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 10:42:15 2019

@author: sthornewillvonessen
"""

import numpy as np
import matplotlib.pyplot as plt

from scipy.stats import norm

# Make it beautiful
plt.style.use("Solarize_Light2")
color_cycle = plt.rcParams['axes.prop_cycle'].by_key()['color']

# Parameter, Termometer on mean 100 with 95% CI between 98°C and 102°C
# Calculate parameters
therm_mean = 100
therm_std = (102-100)/norm.ppf(0.975)

# Generate X confidence intervals
CI_list = []
B = 100  # Number of CIs to bootstrap
sample_size = 1_000
alpha = 0.05

for b in range(B):
    draw_sample = norm.rvs(therm_mean, therm_std, size=sample_size)
    
    sample_mean = draw_sample.mean()
    sample_std = draw_sample.std()

    h = norm.ppf(1-(alpha/2)) * (sample_std/np.sqrt(sample_size))

    h_lower = sample_mean - h
    h_upper = sample_mean + h
    
    CI_list.append(tuple([h_lower, h_upper]))

# Calculate distribution for plotting
X = np.linspace(therm_mean-5*therm_std,
                therm_mean+5*therm_std,
                200)
y = norm.pdf(X, therm_mean, therm_std)

# Number of means outside of CI
n_outside = np.sum([0 if 100 > CI_list[i][0] and 100 < CI_list[i][1] else 1 for i in range(len(CI_list))])

# Create final plot
fig, ax = plt.subplots(facecolor='#002b36', edgecolor='k', figsize=(10, 6))
plt.plot(X, y)
plt.title("Calculating {} confidence intervals from bootstaps of size {}\n Number w/ mean outside: {}".format(B, sample_size, n_outside),
          color='#586e75')
for i, b in enumerate(np.linspace(y.min(), y.max(), len(CI_list))):
    if 100 > CI_list[i][0] and 100 < CI_list[i][1]:
        plt.plot(list(CI_list[i]), 
                 np.repeat(b, 2),
                 color = color_cycle[1])
    else:
        plt.plot(list(CI_list[i]), 
                 np.repeat(b, 2),
                 color = color_cycle[4])
plt.savefig("./plots/frequentist_confidence_intervals.png", facecolor='#002b36')
plt.show()