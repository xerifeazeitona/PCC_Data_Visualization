"""
Before creating a visualization based on the Die class, let’s roll a D6,
print the results, and check that the results look reasonable
"""
from die import Die

# Create a D6
die = Die()

# Make some rolls, and store results in a list.
results = []
for roll in range(100):
    result = die.roll()
    results.append(result)

print(results)
