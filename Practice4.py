# Write a program to display:
# Data type
# Memory address
# Size in bytes of a variable entered by the user.

import sys

x = input("Enter a value : ")

print("Data type : ",type(x))
print("Memory address : ",id(x))
print("Size in bytes : ",sys.getsizeof(x))

