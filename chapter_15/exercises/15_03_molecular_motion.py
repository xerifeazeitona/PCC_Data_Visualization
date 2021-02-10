"""
15-3. Molecular Motion
Modify rw_visual.py by replacing plt.scatter() with plt.plot().
To simulate the path of a pollen grain on the surface of a drop of
water, pass in the rw.x_values and rw.y_values, and include a linewidth
argument. Use 5000 instead of 50,000 points.
"""

from random import choice

import matplotlib.pyplot as plt

class RandomWalk:
    """A class to generate random walks."""

    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points

        # All walks start at (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculate all the points in the walk."""

        # Keep taking steps until the walk reachs the desired length.
        while len(self.x_values) < self.num_points:
            # Decide which direction to go and how far to go in that
            # direction.
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the new position.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
            
while True:
    # Make a random walk.
    rw = RandomWalk(500)
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use('classic')
    fig, ax = plt.subplots()
    ax.plot(rw.x_values, rw.y_values, linewidth=2)
    # Emphasize the first and last points.
    # The starting point is plotted in green in a larger size
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    # The end point is plotted in red, also in a larger size
    ax.scatter(
        rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
