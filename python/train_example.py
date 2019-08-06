# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 13:28:31 2019

@author: sthornewillvonessen
"""

# import packages
import numpy as np
import matplotlib.pyplot as plt

# Make it beautiful
plt.style.use("Solarize_Light2")

# Hypotheses
hypo = [i for i in range(1_000)]

# Prior
prior = [1/len(hypo) for i in hypo]

# Likelihood of data given prior
likelihood = [1/n if n >= 60 else 0 for n in hypo]

# Calculate posterior (unnormalised)
unnorm_post = np.array(likelihood) * np.array(prior)

# Calculate norm
normalisation = np.sum(unnorm_post)

# Calculate posterior
posterior = unnorm_post/normalisation

# Find MLE
non_zero_post = posterior[60:]
mean_post = np.mean(non_zero_post)

non_zero_post[non_zero_post < mean_post][0]

# Plot Result
fig, ax = plt.subplots(facecolor='#002b36', edgecolor='k', figsize=(10, 6))
plt.plot(hypo, posterior)
plt.title("Likelihood of seeing train 60 given hypotheses \n P(T=60 | T=60) = {}"\
          .format(round(posterior[60], 5)),
          color='#586e75')
plt.xlabel("Hypothesis of train number")
plt.ylabel("Likelihood of seeing train 600 given hypotheses")
plt.axvline(x=333, linestyle='dotted', label="Expectation Value")
plt.legend()
plt.savefig("./plots/train_posterior.png", facecolor='#002b36')
plt.show()



