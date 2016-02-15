#! /usr/bin/python

'''Make decent estimates
'''

estimate = float(raw_input("How many hours should the task take you? (Estimate) "))
best_case = float(raw_input("Best case. How many hours? "))
worst_case = float(raw_input("Client says \"You've done it all wrong!\". How many hours? "))

# the three point estimate
howlong = (estimate * 4 + best_case + worst_case) / 6

# rounded to 2 decimal places
print "\nThe task should take you %.2f hours\n" % howlong
