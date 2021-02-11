"""
15-7. Three Dice
When you roll three D6 dice, the smallest number you can roll is 3 and
the largest number is 18. Create a visualization that shows what happens
when you roll three D6 dice.
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


# Create three d6
die_1 = Die()
die_2 = Die()
die_3 = Die()

# Make some rolls, and store results in a list.
results = []
for roll in range(1_000_000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
for value in range(3, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
x_values = list(range(3, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

# The 'dtick': 1 setting tells Plotly to label every tick mark.
x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(
    title='Results of rolling three d6 1,000,000 times', xaxis=x_axis_config,
    yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='3d6.html')
