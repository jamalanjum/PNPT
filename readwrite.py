#!/bin/python3

months = open('months.txt')

#print(months.readlines())
#months.seek(0) # If you want to read the same lines again from a file months. We need to use the .seek() method/function months.seek(0)
#print(months.readlines())

# we could achieve the same results in a quick way by utilising the for loop

for month in months:
	print(month.strip())

months.close()

