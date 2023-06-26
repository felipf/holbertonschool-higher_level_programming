#!/usr/bin/python3
"""
task 0
"""


def read_file(filename=""):
	"""
	reads texts and prints it
	"""
	with open(filename, encoding='utf-8') as fileR:
		content = fileR.read()
		print(content, end="")
