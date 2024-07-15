# In this exercise, you will practice both File I/O as well as using Exceptions
# in a real-world scenario.
#
# This folder contains another folder called `books/` that contains three text files
# of books from Project Gutenberg:
# 1. war_and_peace.txt
# 2. pride_and_prejudice.txt
# 3. crime_and_punishment.txt
#
# 1) Open `war_and_peace.txt`, read the whole file content and store it in a variable
# 2) Open `crime_and_punishment.txt` and overwrite the whole content with an empty string
# 3) Loop over all three files and print out only the first character each. Your program
#    should NEVER terminate with a Traceback.
#     a) Which exception can you expect to encounter? Why?
#     b) How do you catch it to avoid the program from terminating with a traceback?

import os

file_names = ['war_and_peace.txt', 'pride_and_prejudice.txt', 'crime_and_punishment.txt']
file_path = os.path.join(os.getcwd(), '05_exceptions', 'books')

#open war_and_peace.txt, read the whole file content and store it in a variable
try:
    with open(os.path.join(file_path, file_names[0]), 'r', encoding='utf-8') as file:
        war_and_peace = file.read()
except IOError:
    print(f"Could not read the file {file_names[0]}.")

# make a copy of crime_and_punishment.txt, the open the copy and overwrite the whole content with an empty string
try:
    with open(os.path.join(file_path, file_names[2]), 'r', encoding='utf-8') as file:
        crime_and_punishment = file.read()
        # create a copy of the file
        with open(os.path.join(file_path, 'crime_and_punishment_copy.txt'), 'w', encoding='utf-8') as copy:
            copy.write('')
except IOError:
    print(f"Could not read the file {file_names[2]}.")

# loop over all three files and print out only the first character each
for file_name in file_names:
    try:
        with open(os.path.join(file_path, file_name), 'r', encoding='utf-8') as file:
            first_char = file.read(1)
    except IOError:
        print(f"Could not read the file {file_name}.")
    except ValueError:
        print(f"The file {file_name} does not contain any characters.")
    else:
        print(f"The first character in the file {file_name} is {first_char}.")