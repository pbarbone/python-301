# Write a custom exception  that inherits from `Exception()`
# Open and read in the content of the book `.txt` files in the `books/` folder
# like you did in the previous exercise.
# Raise your `PrinceException()` if the first 100 characters of a book
# contain the string "Prince".

# Open War and peace.txt, store the file as a variable and read the first word

import os

class PrinceException(Exception):
    pass

file_path = os.path.join(os.getcwd(), '05_exceptions', 'books')
books = ['war_and_peace.txt','crime_and_punishment.txt','pride_and_prejudice.txt']

for book in books:
    try:
        with open(os.path.join(file_path, book), 'r', encoding='utf-8') as file:
            first_words = file.read(100)
            if 'Prince' in first_words:
                raise PrinceException
            else:
                print(f'Prince was not in {book}')
    except IOError:
        print("Book does not exist in the directory")
    except PrinceException:
        print(f"Prince is in the text of {book}!")

