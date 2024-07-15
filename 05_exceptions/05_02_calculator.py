# Write a script that takes in two numbers from the user and calculates the quotient.
# Use a try/except statement so that your script can handle:
#
# - if the user enters a string instead of a number
# - if the user enters a zero as the divisor
#
# Test it and make sure it does not crash when you enter incorrect values.

def calculator():
    try:
        dividend = float(input("Enter the dividend: "))
        divisor = float(input("Enter the divisor: "))
        print(f"The quotient is {dividend / divisor}")
    except ValueError:
        print("You must enter a number.")
    except ZeroDivisionError:
        print("You cannot divide by zero.")

calculator()

#Follow on - TTD framework where i test the return values to see if they match the different exceptions
#need to create a new function w/o input bc that messes up TTD (bc testing one primary operation at a time)
