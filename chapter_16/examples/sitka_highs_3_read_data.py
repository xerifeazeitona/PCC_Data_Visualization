"""
First, we’ll read in the high temperature for each day
"""
import csv

filename = '../data/sitka_weather_07-2018_simple.csv'

with open(filename) as file_obj:
    reader = csv.reader(file_obj)
    header_row = next(reader)

    # Get high temperatures (TMAX) from this file.
    highs = [int(row[5]) for row in reader]

print(highs)
