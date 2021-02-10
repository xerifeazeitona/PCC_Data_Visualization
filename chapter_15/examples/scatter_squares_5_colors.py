"""
To change the color of the points, pass c to scatter() with the name of
a color to use in quotation marks.
To define a color, pass the c argument a tuple with three decimal values
(one each for red, green, and blue in that order), using values between
0 and 1.

You use colormaps in visualizations to emphasize a pattern in the data.
The pyplot module includes a set of built-in colormaps. To use one of
these colormaps, you need to specify how pyplot should assign a color
to each point in the data set.
"""
import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('dark_background')
fig, ax = plt.subplots()
# Color by name example
#ax.scatter(x_values, y_values, c='red', s=10)
# Color by RGB value example
#ax.scatter(x_values, y_values, c=(0, 0.8, 0), s=10)
# Colormap example
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)

# Set the range for each axis
ax.axis([0, 1100, 0, 1100000])

# If you want your program to automatically save the plot to a file, you
# can replace the call to plt.show() with a call to plt.savefig()
#plt.savefig('squares_plot.png', bbox_inches='tight')

plt.show()
