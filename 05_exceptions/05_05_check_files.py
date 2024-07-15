# Read in the first number from `integers.txt`
# and perform a calculation with it.
# Make sure to catch at least two possible Exceptions (`IOError` and `ValueError`)
# with specific `except` statements, and continue to do the calculation
# only if neither of them applies.
import os

file_name = '05_exceptions\integers.txt'
file_path = os.path.join(os.getcwd(), file_name)

try:
    with open(file_name, 'r') as file:
        first_number = int(file.readline())
except IOError:
    print(f"Could not read the file {file_name}.")
except ValueError:
    print(f"The file {file_name} does not contain an integer.")
else:
    print(f"The first number in the file is {first_number}.")
    print(f"The result of the calculation is {first_number * 2}.")
