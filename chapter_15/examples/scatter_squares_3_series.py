"""
To plot a series of points, we can pass scatter() separate lists of x-
and y-values.
The x_values list contains the numbers to be squared, and y_values
contains the square of each number. When these lists are passed to
scatter(), Matplotlib reads one value from each list as it plots each
point.
"""
import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

plt.style.use('dark_background')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=100)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()
