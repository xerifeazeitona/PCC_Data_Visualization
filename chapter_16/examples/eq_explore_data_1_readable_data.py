"""
The json module provides a variety of tools for exploring and working
with JSON data. 
Let’s start by loading the data and displaying it in a format that’s
easier to read.
"""
import json

# Explore the structure of the data.
filename = '../data/eq_data_1_day_m1.json'
with open(filename) as file_obj:
    all_eq_data = json.load(file_obj)

readable_file = '../data/readable_eq_data.json'
with open(readable_file, 'w') as file_obj:
    json.dump(all_eq_data, file_obj, indent=4)
    