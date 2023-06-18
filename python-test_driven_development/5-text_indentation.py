#!/usr/bin/python3
"""
task5
"""



def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: ., ? and :
    """
	if not isinstance(text, str):
		raise TypeError('text must be a string')


	delimiters = {'.', '?', ':'}
	i = 0


	while i < len(text):
		if text[i] in delimiters:
			print(text[i] + "\n\n", end="")
			i += 1
			while i < len(text) and text[i] == " ":
				i += 1
		else:
			print(text[i], end="")
			i += 1
