# -*- coding: utf-8 -*-
"""
Created on Fri May 31 12:35:18 2019

@author: sthornewillvonessen
"""

# Import Packages
import numpy as np
import matplotlib.pyplot as plt

from scipy.stats import beta

# Make Matplotlib Beautiful
plt.style.use("seaborn")

# Define functions
    
def plot_dist(dist):
    """
    Does a quick plot of a distribution between 0 and 1 with a resolution of 200.
    
    Args:
        dist: scipy distribution. The distribution that is to be quickly plotted
    """
    
    # Create linspace and get PDF
    X = np.linspace(0, 1, 200)
    y = dist.pdf(X)
    
    # Plot figure
    fig, ax = plt.subplots(figsize=(10,6),
                           facecolor='white',
                           edgecolor='k')
    
    plt.plot(X, y)
    plt.show()

def update_distribution(result_list):
    """
    Update Beta distribution based on responses.
    
    Args:
        result_list: list. Collection of 1s and 0s whether a question was answered yes or no
    Returns:
        new_dist: Scipy distribution. Posterior distribution based on result_list
    """
    
    # Calculate parameters for posterior
    a = 1 + np.array(result_list).sum()
    b = 1 + len(result_list) - np.array(result_list).sum()
    
    # Create posterior object
    new_dist = beta(a, b)
    
    return new_dist

# Main Function
def main():

    print("Welcome to AB test simulator")    

    # Initialize test results
    result_list = []
    loop_flag = True
    
    # Instantiate prior distribution
    prior_dist = beta(1, 1)
    plot_dist(prior_dist)
    
    # Get input from user
    while loop_flag:
        result = input('\n\t>>> ')

        # Create exit point
        if result == 'break':
            print("Breaking loop")
            break

        # Make sure the value is an int
        try:
            result = int(result)
        except ValueError:
            print("Input should be an int, try again.")
            continue

        # Make sure the value is equal to 1 or 0
        if (result == 1) or (result == 0):
            result_list.append(result)
        else:
            print("Input should either be a 1 or a 0, try again.")
            continue

        # Calculate posterior and plot result
        new_dist = update_distribution(result_list)
        plot_dist(new_dist)

if __name__ == '__main__':
    main()