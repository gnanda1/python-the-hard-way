# Reading Files 
"""
Opening a file refers to getting the file ready either for reading or for writing.
This can be done using the open() function. 
"""

from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}")
print(txt.read())

print("Type the file name again: ")
file_again = input("> ")

txt_again = open(filename)
print(txt_again.read())