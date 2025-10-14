# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 22:52:04 2025

@author: walam
"""

import numpy as np

# Parameters
N_FLOORS = 40  # Total number of floors
K_PEOPLE = 21  # Total number of people
EXITS = 3 # Exactly 3 people exiting
N_TRIALS = 1000 # Number of trials

# Array to store the value of X (number of 3-exit stops) for each trial
X_values = np.zeros(N_TRIALS)

# Simulation Loop
for i in range(N_TRIALS):
    # Randomly choose a floor for each of the 21 people
    # The choices are floors 1 to 40
    # Replace=True, as people can choose the same floor
    choices = np.random.choice(
        a=np.arange(1, N_FLOORS + 1),
        size=K_PEOPLE,
        replace=True
    )

    # Count the number of people exiting at each floor.
    floors, counts = np.unique(choices, return_counts=True)

    # Find the number of stops where the count is exactly 3.
    X_i = np.sum(counts == EXITS)
    X_values[i] = X_i

# Calculate E[X])
E_X = np.mean(X_values)

# Calculate E[X^2]
E_X2 = np.mean(X_values**2)

# Print results
print(f"E[X]: {E_X:.4f}")
print(f"E[X^2]: {E_X2:.4f}")
