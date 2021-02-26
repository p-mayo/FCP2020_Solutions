#!/usr/bin/env python3
# Add some relevant comments here, such as author
# date, purpose of the script, etc.

# This is followed by importing any module
# you might use
import sys		# You could also comment here why you're using this module

# Now some constants
PI = 3.1415		# Constants are, by standard, declared all in capitals.
				# Their values are not intended to change

# Now define some functions
def add_arguments(argument_1, argument_2):
	""" Add two values and returns the result
	"""
	result = argument_1 + argument_2
	return result

def print_result(result):
	""" Receives one argument and prints it on screen
	"""
	print("My argument is", argument)

def main():
	""" Function to be called when the script is executed """
	# Getting some values to add from the user:
	value_1 = int(input("Provide the first value to add"))
	value_2 = int(input("Provide the second value to add"))

	# Calling the function to add the values
	result = add_arguments(value_1, value_2)

	# Printing the result
	print_argument(result)



if __name__ == '__main__':
	# Calling the main function when the script is run
	main()