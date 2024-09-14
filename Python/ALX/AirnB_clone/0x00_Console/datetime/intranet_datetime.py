#!/usr/bin/python3

"""
Learning how to use the datetime module
"""
# import os
# import sys

from datetime import datetime

# An example of creating an instance with datetime
date_now = datetime.now()
print(type(date_now))    # <class 'datetime.datetime'>
print(date_now)          # An example: 2017-06-08 20:42:42.170922
print()


# Manpulating datetime as an object
from datetime import timedelta
date_tomorrow = date_now + timedelta(days=1)
# We manipulated the date by moving it a day forward using timedelta(days=1)
print(date_tomorrow) # An example: 2017-06-09 20:42:42.170922


# Storing datetime
a_dict = { 'my_date': date_now }    # Remember that date_now = datetime.now()
print(type(a_dict['my_date'])) # <class 'datetime.datetime'>
print(a_dict) # {'my_date': datetime.datetime(2017, 6, 8, 20, 42, 42, 170922)}

# Making datetime readable
print(date_now.strftime("%A")) # %A is for the day. This was coded on a Monday.
print(date_now.strftime("%A %d %B %Y at %H:%M:%S")) # Monday 17 July 2023 at 20:53:30

