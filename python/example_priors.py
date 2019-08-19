#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 12:06:24 2019

@author: simonthornewillvonessen
"""


# Import packages
import numpy as np
import matplotlib.pyplot as plt

# Make it beautiful
plt.style.use("Solarize_Light2")
color_cycle = plt.rcParams['axes.prop_cycle'].by_key()['color']


def normalise(v):
    norm=np.linalg.norm(v, ord=1)
    if norm==0:
        norm=np.finfo(v.dtype).eps
    return v/norm

# Create linspace
X = np.linspace(0, 1, 200)

# Create example priors
uniform = [1/(X.max() - X.min()) for i in X]

triangle = [i if i<=0.5 else 1-i for i in X]
triangle = normalise(triangle)

exponential = [1/i if i > 0 else np.inf for i in X]
exponential = normalise(exponential[1:])


# Create final plot
fig, ax = plt.subplots(3, facecolor='#002b36', edgecolor='k', figsize=(10, 6))
ax[0].plot(X, uniform, color=color_cycle[0])
ax[1].plot(X, triangle, color=color_cycle[1])
ax[2].plot(X[1:], exponential, color=color_cycle[2])
plt.savefig("./plots/example_priors.png", facecolor='#002b36')
plt.show()
