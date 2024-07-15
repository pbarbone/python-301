# Write a script that generates an exception.
# Handle this exception with a try/except block.
# For example:
#
# list_ = ["hello world!"]
# print(list_[1])
#
# This raises and exception that needs to be handled.

list_ = ["hello world!"]
try:
    #raise ValueError
    print(list_[1])
except IndexError:
    print("The list index is out of range.")
except ValueError:
    print("You've got a value error")

