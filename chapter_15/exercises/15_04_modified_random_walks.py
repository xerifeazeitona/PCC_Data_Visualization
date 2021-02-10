"""
15-4. Modified Random Walks
In the RandomWalk class, x_step and y_step are generated from the same
set of conditions. The direction is chosen randomly from the list
[1, -1] and the distance from the list [0, 1, 2, 3, 4].
Modify the values in these lists to see what happens to the overall
shape of your walks. Try a longer list of choices for the distance,
such as 0 through 8, or remove the −1 from the x or y direction list.
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
            #x_direction = choice([1, -1])
            x_direction = 1
            #x_distance = choice([0, 1, 2, 3, 4])
            x_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
            x_step = x_direction * x_distance

            #y_direction = choice([1, -1])
            y_direction = 1
            #y_distance = choice([0, 1, 2, 3, 4])
            y_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
            y_step = y_direction * y_distance

            # Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the new position.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)


# Make a random walk.
rw = RandomWalk()
rw.fill_walk()

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(15, 9))
point_numbers = range(rw.num_points)
ax.scatter(
    rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
    edgecolors='none', s=15)

# Emphasize the first and last points.
ax.scatter(0, 0, c='green', edgecolors='none', s=100)
ax.scatter(
    rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

# Remove the axes.
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.show()
