# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 12:40:29 2019

@author: sthornewillvonessen
"""

import numpy as np
import matplotlib.pyplot as plt

plt.style.use("seaborn")

# Set seed
np.random.seed(42)

def chance_of_rain(day_in_year):
    """
    Calculates the change of rain given a day in the year
    """
    
    p = 0.3*np.sin(day_in_year/365 * 2*np.pi) + 0.3

    return p


# Create list for days
days_in_year = [i for i in range(365)]

# Get chance of rain
chance_of_rain = chance_of_rain(np.array(days_in_year))

# Does it rain?
rainy_days = [np.random.choice([0, 1], p=[1-p, p]) for p in chance_of_rain]


fig, ax = plt.subplots(figsize=(10, 6), edgecolor='k', facecolor='white')
plt.title("Probability that it rains in a year")
plt.plot(0, 0, alpha=0)
plt.plot(days_in_year, chance_of_rain, alpha=0.8, label = "Probability of Rain")
plt.scatter(days_in_year, rainy_days, alpha=0.1, label="Days where it rains")
plt.legend()
plt.xlabel("Day number")

plt.savefig("./plots/chances_of_rain.png")

year_chance_rain = np.mean(rainy_days)
X = np.linspace(0, 365, 365)

fig, ax = plt.subplots(figsize=(10, 6), edgecolor='k', facecolor='white')
plt.title("Probability that it rains in a year")
plt.plot(0, 0, alpha=0)
plt.plot(days_in_year, chance_of_rain, alpha=0.8, label = "Probability of Rain")
plt.plot(X, np.repeat(year_chance_rain, 365), alpha=0.8, label = ("Freq. Est. Chance of Rain"))
plt.scatter(days_in_year, rainy_days, alpha=0.1, label="Days where it rains")
plt.legend()
plt.xlabel("Day number")

plt.savefig("./plots/chances_of_rain_w-est.png")