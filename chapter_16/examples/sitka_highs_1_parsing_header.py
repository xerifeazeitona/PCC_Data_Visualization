"""
Python’s csv module in the standard library parses the lines in a CSV
file and allows us to quickly extract the values we’re interested in.
"""
import csv

filename = '../data/sitka_weather_07-2018_simple.csv'

with open(filename) as file_obj:
    reader = csv.reader(file_obj)
    header_row = next(reader)
    print(header_row)
