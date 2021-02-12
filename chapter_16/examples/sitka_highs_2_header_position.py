"""
To make it easier to understand the file header data, we print each
header and its position in the list
"""
import csv

filename = '../data/sitka_weather_07-2018_simple.csv'

with open(filename) as file_obj:
    reader = csv.reader(file_obj)
    header_row = next(reader)

    # The enumerate() function returns both the index of each item and
    # the value of each item as you loop through a list
    for index, column_header in enumerate(header_row):
        print(index, column_header)
