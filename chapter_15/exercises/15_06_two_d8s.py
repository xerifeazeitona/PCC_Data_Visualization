"""
15-6. Two D8s
Create a simulation showing what happens when you roll two eight-sided
dice 1000 times. Try to picture what you think the visualization will
look like before you run the simulation; then see if your intuition was
correct.
Gradually increase the number of rolls until you start to see the limits
of your system’s capabilities.
"""
from random import randint

from plotly.graph_objs import Bar, Layout
from plotly import offline

class Die:
    """A class representing a single die."""

    def __init__(self, num_sides=6):
        """Assume a six-sided die."""
        self.num_sides = num_sides

    def roll(self):
        """Return a random value between 1 and the number of sides."""
        return randint(1, self.num_sides)


# Create two d8
die_1 = Die(8)
die_2 = Die(8)

# Make some rolls, and store results in a list.
results = []
for roll in range(1_000_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

# The 'dtick': 1 setting tells Plotly to label every tick mark.
x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(
    title='Results of rolling two d8 1,000,000 times', xaxis=x_axis_config,
    yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='2d8.html')
