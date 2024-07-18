# Write a decorator function that wraps text output into quotes, e.g.:
# Hello world! ----> "Hello World!"
# You can use it to create quotes from text output.

def decorator_func(initial_func):
    print("(3) Running Decorator Function")
    def wrapper_func():
        print("(4) Calling the wrapper function")

        return initial_func()
    print("(5) returning wrapped function")
    return wrapper_func

def prettify():
    print("flowers")

print("(1) Decorating prettify")

decorated_prettify = decorator_func(prettify)

print("(2) Calling my Decorated_prettify")

decorated_prettify()

var1 = decorator_func(prettify)
var2 = decorator_func(prettify)
var3 = decorator_func(prettify)

print(var1)
print(var2)
print(var3)