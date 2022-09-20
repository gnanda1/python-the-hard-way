# Parameters, unpacking variables.
# Terminal command to run this program: python ex13.py first second thrid
from sys import argv

script, first, second, thrid = argv

print("The script is called: ", script)
print("Your first variable is: ", first)
print("Your second variable is: ", second)
print("Your thrid variable is: ", thrid)