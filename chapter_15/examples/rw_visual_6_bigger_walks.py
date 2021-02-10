"""
Increasing the number of points will give us more data to work with.
To do so, we increase the value of num_points when we make a RandomWalk
instance and adjust the size of each dot when drawing the plot
"""
import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    # Make a random walk.
    rw = RandomWalk(50_000)
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use('dark_background')
    # To make the plotting window better fit the screen, adjust the size of
    # Matplotlib's output
    fig, ax = plt.subplots(figsize=(15, 9))
    point_numbers = range(rw.num_points)
    ax.scatter(
        rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
        edgecolors='none', s=1)

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

    keep_running = input("Make another walk? (Y/n): ")
    if keep_running == 'n':
        break
