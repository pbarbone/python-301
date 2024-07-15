# Write a decorator function that wraps text output into quotes, e.g.:
# Hello world! ----> "Hello World!"
# You can use it to create quotes from text output.

def decorator_func(initial_func):
    def wrapper_func():

        return initial_func()
    return wrapper_func

def prettify():
    print("flowers")

decorated_prettify = decorator_func(prettify)

decorated_prettify()