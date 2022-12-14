"""
Reading and Writing Files

close - Close the file. Like File -> Save. in your editor
read - Reads the contents of a file. You can assign the result to a variable.
readline - reads just one line of a text file.
truncate - Empties the file. Watch out if you care about the file.
write(stuff) - Writes "stuff" to the file.
seek(0) - Move the read/write location to the beginning of the file.

"""
# To run the code from terminal: python3 ex16.py test16.txt
from sys import argv

script, filename = argv

print(f"We'are going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

# Open the file and store in a variable.
print("Opening the file...")
target = open(filename, 'w')

#print(target)

# Empty the file
print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I am going to write these to the file.")

# Writing the content to the file.
target.write(line1)
target.write("\n")

target.write(line2)
target.write("\n")

target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()