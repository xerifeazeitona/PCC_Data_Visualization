"""
It would be useful to see where each walk begins and ends. To do so, we
can plot the first and last points individually after the main series
has been plotted.
"""
import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    # Make a random walk.
    rw = RandomWalk()
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use('classic')
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(
        rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
        edgecolors='none', s=15)

    # Emphasize the first and last points.
    # The starting point is plotted in green in a larger size
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    # The end point is plotted in red, also in a larger size
    ax.scatter(
        rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
