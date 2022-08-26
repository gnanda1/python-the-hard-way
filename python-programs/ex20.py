# Functions and Files.

# import args 

from sys import argv

script, input_file = argv

# Reading a file.
def print_all(f):
    print(f.read())

# Python file method seek() sets the file's current position at the offset
def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline())

# open input_file and store in variable current_file.
current_file = open(input_file)
print("First let's print the whole file: \n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")
rewind(current_file)

print("Let's print three lines: ")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)