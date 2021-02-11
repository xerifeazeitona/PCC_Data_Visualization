"""
15-9. Die Comprehensions
For clarity, the listings in this section use the long form of for
loops. If you’re comfortable using list comprehensions, try writing a
comprehension for one or both of the loops in each of these programs.
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
results = [die_1.roll() + die_2.roll() for roll in range(1000000)]

# Analyze the results.
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result+1)]

# Visualize the results.
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

# The 'dtick': 1 setting tells Plotly to label every tick mark.
x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(
    title='Results of rolling two d8 1,000,000 times', xaxis=x_axis_config,
    yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='die_comprehension.html')
