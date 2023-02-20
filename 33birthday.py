# 33birthday.py

# You may have heard of the 'birthday paradox' before
# https://en.wikipedia.org/wiki/Birthday_problem
# Write a program that simulates it
# Make the number of days and the number of people command line arguments

# Hint: make the problem smaller to aid visualization and debugging

# Variation: try making the calendar a list
# Variation: try making the birthdays a list


import sys

days = int(sys.argv[1])
people = int(sys.argv[2])

fact_days = 1
fact_people = 1

# calculate factorial number of days
for i in range(1, days + 1):
	fact_days = fact_days * i
	
# calculate factorial of number of days - number of people 
for i in range(1, (days - people) + 1):
	fact_people = fact_people * i

bday_norep = fact_days/fact_people # birthdays without repetition
bday_total = days**people
prob = 1 - (bday_norep/bday_total)

print("%.3f" % prob)

"""
python3 33birthday.py 365 23
0.571
"""

