"""
Rolling two dice results in larger numbers and a different distribution
of results. Let’s modify our code to create two D6 dice to simulate the
way we roll a pair of dice. Each time we roll the pair, we’ll add the
two numbers and store the sum in results.
"""
from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create two d6
die_1 = Die()
die_2 = Die()

# Make some rolls, and store results in a list.
results = []
for roll in range(1000):
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
    title='Results of rolling two d6 1000 times', xaxis=x_axis_config,
    yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6.html')
