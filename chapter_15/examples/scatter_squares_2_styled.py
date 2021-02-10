"""
Styling the output make it more interesting. We’ll add a style and a
title, label the axes, and make sure all the text is large enough to
read.
"""
import matplotlib.pyplot as plt

plt.style.use('dark_background')
fig, ax = plt.subplots()
ax.scatter(2, 4, s=200)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()
