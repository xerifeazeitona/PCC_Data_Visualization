"""
15-5. Refactoring
The fill_walk() method is lengthy. Create a new method called get_step()
to determine the direction and distance for each step, and then
calculate the step. You should end up with two calls to get_step() in
fill_walk():
    x_step = self.get_step()
    y_step = self.get_step()

This refactoring should reduce the size of fill_walk() and make the
method easier to read and understand.
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
            # Decide how far to go in which direction
            x_step = self.get_step()
            y_step = self.get_step()

            # Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the new position.
            x_position = self.x_values[-1] + x_step
            y_position = self.y_values[-1] + y_step

            self.x_values.append(x_position)
            self.y_values.append(y_position)

    def get_step(self):
        """
        Decide which direction to go and how far to go in that
        direction.
        """
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        step = direction * distance
        return step



# Make a random walk.
rw = RandomWalk()
rw.fill_walk()

# Plot the points in the walk.
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(15, 9))
point_numbers = range(rw.num_points)
ax.scatter(
    rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
    edgecolors='none', s=10)

# Emphasize the first and last points.
ax.scatter(0, 0, c='green', edgecolors='none', s=100)
ax.scatter(
    rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

# Remove the axes.
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.show()
