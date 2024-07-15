# Write a script that demonstrates a try/except/else statement.
# For example, you can revisit the course module about database interactions
# and include a try/except/else statement based on what to do whether or not
# the database connection can be established.

import sqlite3

def connect_to_database():
    try:
        connection = sqlite3.connect("example.db")
    except sqlite3.Error:
        print("Could not connect to the database.")
    else:
        print("Database connection established.")
        connection.close()
    
connect_to_database()

# 
