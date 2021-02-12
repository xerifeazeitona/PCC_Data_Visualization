"""
Here, we’ll make a list that contains all the information about every
earthquake that occurred.
We take the data associated with the key 'features' and store it in
all_eq_dicts.
Notice how short this code is. The neatly formatted file
readable_eq_data.json has over 6,000 lines. But in just a few lines,
we can read through all that data and store it in a Python list.
"""
import json

# Explore the structure of the data.
filename = '../data/eq_data_1_day_m1.json'
with open(filename) as file_obj:
    all_eq_data = json.load(file_obj)

all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))
