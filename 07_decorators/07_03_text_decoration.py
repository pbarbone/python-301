# Write a decorator that literally decorates text output.
# Make it so the symbol it uses can be an argument to the decorator
#
# The output of a function that returns `"Hello"` that has been
# decorated like with `@decorate("*")` should look like this:
#
# ******************************
# Hello
# ******************************

def decorate(symbol):
    print("(1) Decorating")
    def inner_decorator(func):
        print("(2) Inner decorating")
        def wrapper(*args, **kwargs):
            print("(3) Wrapping")
            text = func(*args, **kwargs)
            return f"{symbol * 30}\n{text}\n{symbol * 30}"
        print("(4) Returning wrapper")
        return wrapper
    print("(5) Returning inner_decorator")
    return inner_decorator

@decorate("*")
def text():
    return "Hello"

print(text)

print(text())