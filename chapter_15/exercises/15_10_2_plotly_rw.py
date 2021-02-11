"""
15-10. Practicing with Both Libraries
Use Plotly to make the visualization for a random walk.
"""
from random import choice

from plotly.graph_objs import Scatter, Layout
from plotly import offline

class RandomWalk:
    """A class to generate random walks."""

    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points

        # All walks start at (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculate all the points in the walk."""

        # Keep taking steps until the walk reachs the desired length.
        while len(self.x_values) < self.num_points:
            # Decide how far to go in which direction
            x_step = self.get_step()
            y_step = self.get_step()

            # Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the new position.
            x_position = self.x_values[-1] + x_step
            y_position = self.y_values[-1] + y_step

            self.x_values.append(x_position)
            self.y_values.append(y_position)

    def get_step(self):
        """
        Decide which direction to go and how far to go in that
        direction.
        """
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        step = direction * distance
        return step


# Make a random walk.
rw = RandomWalk()
rw.fill_walk()

# Visualize the results.
x_values = list(range(5_001))
data = Scatter(
    x=rw.x_values,
    y=rw.y_values,
    mode='markers',
    name='Random Walk',
    marker=dict(
        color=[list(range(5_001))],
        size=8,
        colorscale='Greens',
        showscale=True
    )
)

my_layout = Layout(title='Random Walk')
offline.plot({'data': data, 'layout': my_layout}, filename='random_walk.html')
