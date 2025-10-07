import random

# Simulatation of rolling a die 1000 times
trials = 1000
wins = 0

for i in range(trials):
    prev_roll = None
    while True:
        roll = random.randint(1, 6)
        if roll == 1:
            # Game ends with a loss
            break
        elif roll == 6 and prev_roll == 6:
            # Two consecutive 6s — win
            wins += 1
            break
        else:
            prev_roll = roll

# Empirical probability
empirical_probability = wins / trials

print(f"Number of wins in {trials} trials: {wins}")
print(f"Empirical probability: {empirical_probability:.4f}")
