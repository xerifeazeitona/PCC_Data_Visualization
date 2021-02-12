"""
We can construct an object representing July 1, 2018 using the
strptime() method from the datetime module.
"""
from datetime import datetime

first_date = datetime.strptime('2018-07-01', '%Y-%m-%d')

print(first_date)
