"""
Let’s create a six-sided die and a ten-sided die, and see what happens
when we roll them 50,000 times
"""
from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create two d6
die_1 = Die()
die_2 = Die(10)

# Make some rolls, and store results in a list.
results = []
for roll in range(50_000):
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
    title='Results of rolling a d6 and a d10 50000 times', xaxis=x_axis_config,
    yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d10.html')
