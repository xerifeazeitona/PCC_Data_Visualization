"""
15-1. Cubes
A number raised to the third power is a cube. Plot the first five cubic
numbers, and then plot the first 5000 cubic numbers.
"""
import matplotlib.pyplot as plt

def plot_cubes(num_cubes, save_to_disk=False):
    """Plots n cubic numbers."""
    x_values = range(1, num_cubes+1)
    y_values = [x**3 for x in x_values]

    plt.style.use('dark_background')
    fig, ax = plt.subplots()
    ax.scatter(x_values, y_values, s=10)

    # Set chart title and label axes.
    title = f"Cubic Numbers from 1 to {num_cubes}"
    ax.set_title(title, fontsize=20)
    ax.set_xlabel("Value", fontsize=14)
    ax.set_ylabel("Cube of Value", fontsize=14)

    # Set size of tick labels.
    ax.tick_params(axis='both', which='major', labelsize=14)

    # Set the range for each axis
    #ax.axis([0, 1100, 0, 1100000])

    # If you want your program to automatically save the plot to a file, you
    # can replace the call to plt.show() with a call to plt.savefig()
    if save_to_disk:
        filename = f"{num_cubes}_cubes_plot.png"
        plt.savefig(filename, bbox_inches='tight')
    else:
        plt.show()

plot_cubes(5)
plot_cubes(5000)
