"""
15-10. Practicing with Both Libraries
Try using Matplotlib to make a die-rolling visualization
"""
from random import randint

import matplotlib.pyplot as plt

class Die:
    """A class representing a single die."""

    def __init__(self, num_sides=6):
        """Assume a six-sided die."""
        self.num_sides = num_sides

    def roll(self):
        """Return a random value between 1 and the number of sides."""
        return randint(1, self.num_sides)


# Create two d6
die_1 = Die()
die_2 = Die()

# Make some rolls, and store results in a list.
results = [die_1.roll() + die_2.roll() for roll in range(1000000)]

# Plot the results
plt.style.use('seaborn-dark')
fig, ax = plt.subplots(figsize=(15, 9))
ax.hist(results, bins=11)

# Set chart title and label axes.
ax.set_title("Results of rolling two d6 1,000,000 times", fontsize=24)
ax.set_xlabel("Result", fontsize=14)
ax.set_ylabel("Frequency of Result", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)
plt.xticks([value for value in range(2, 12+1)])

plt.show()
