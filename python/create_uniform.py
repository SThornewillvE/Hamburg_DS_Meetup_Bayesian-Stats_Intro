# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 16:04:59 2019
@author: sthornewillvonessen
"""

# Import Libraries
import matplotlib.pyplot as plt
import numpy as np

# Make it beautiful
plt.style.use("Solarize_Light2")

# Create uniform function
class Uniform:
    def __init__(self):
        self.h_0 = 0
        self.h_1 = 1
    
    def fit(self, h_0, h_1):
        """
        Sets start and finish of uniform distribution
        
        :Input:
            :h_0: Where the uniform dist starts
            :h_1: Where the uniform dist ends
        :Returns:
            :: Does not return anything
        """
        
        # Make sure data type makes sense
        try:
            h_0 = float(h_0)
            h_1 = float(h_1)
        except: 
            print("Error: Must pass a number")
            return ValueError
        
        # Make sure h_0 < h_1
        if h_0 < h_1:        
            self.h_0 = h_0
            self.h_1 = h_1
        else:
            print("Error: h_0 must be smaller than h_1")
            return ValueError
        
    def predict(self, X):
        """
        Predicts value of x given fitted distribution
        
        :Input:
            :x: Value to be predicted
        :Returns:
            :y_pred: Predicted value based on x
        """
        
        y_pred = []
        
        for x in X:
            if x < self.h_0:
                y_pred.append(0)
            elif x > self.h_1:
                y_pred.append(0)
            else:
                y_pred.append(1/(self.h_1 - self.h_0))
                
        return y_pred
        
# Instantiate uniform distribution    
u_1 = Uniform()
u_2 = Uniform()
u_3 = Uniform()
u_4 = Uniform()
u_5 = Uniform()

u_2.fit(0, 2)
u_3.fit(1, 3)
u_4.fit(-4, 4)
u_5.fit(-4, -3.5)

# Create Linspace
X = np.linspace(-5, 5, 2_000)
y_pred_1 = u_1.predict(X)
y_pred_2 = u_2.predict(X)
y_pred_3 = u_3.predict(X)
y_pred_4 = u_4.predict(X)
y_pred_5 = u_5.predict(X)

# Create plots
fig, ax = plt.subplots(facecolor='#002b36', edgecolor='k', figsize=(10, 6))
plt.plot(X, y_pred_1, label="Uniform(0, 1)", alpha=0.6)
plt.plot(X, y_pred_2, label="Uniform(0, 2)", alpha=0.6)
#plt.plot(X, y_pred_3, label="Uniform(1, 3)", alpha=0.6)
#plt.plot(X, y_pred_4, label="Uniform(-4, 4)", alpha=0.6)
#plt.plot(X, y_pred_5, label="Uniform(-4, -3.5)", alpha=0.6)
plt.title("Examples of uniform distributions", color='#586e75')
plt.xlabel("theta")
plt.ylabel("p(theta)")
plt.legend()
plt.savefig("./plots/uniform_plots.png", facecolor='#002b36')
plt.show()

