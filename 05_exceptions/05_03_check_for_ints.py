# Create a script that asks a user to input an integer, checks for the
# validity of the input type, and displays a message depending on whether
# the input was an integer or not.
# The script should keep prompting the user until they enter an integer.

def check_for_ints():
    while True:
        try:
            user_input = int(input("Enter an integer: "))
            print("You entered an integer.")
            break
        except ValueError:
            print("You must enter an integer.")

check_for_ints()
