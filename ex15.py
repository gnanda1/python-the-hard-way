# Reading Files

from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}")
print(txt.read())

print("Type the file name again: ")
file_again = input("> ")

txt_again = open(filename)
print(txt_again.read())