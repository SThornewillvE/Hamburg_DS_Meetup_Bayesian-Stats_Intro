# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 10:42:15 2019

@author: sthornewillvonessen
"""

import numpy as np
import matplotlib.pyplot as plt

from scipy.stats import norm ,t

# Make it beautiful
plt.style.use("Solarize_Light2")


# Parameter, Termometer on mean 100 with 95% CI between 98°C and 102°C
# Calculate parameters
therm_mean = 100
therm_std = (102-100)/norm.ppf(0.975)

# Generate sample
sample_n = 10
X_control = np.array([round(i, 3) for i in np.random.normal(100, 1.02, sample_n)])
X_test =np.array([round(i, 3) for i in np.random.normal(102, 1.02, sample_n)])


# Get bootstrapped means
X_means = [np.random.choice(X, len(X), replace=True).mean() for b in range(20)]

X = np.array([round(i, 3) for i in np.random.normal(100, 1.02, sample_n)])