# Create a decorator that censors potentially offensive words from a text.
# For example, assuming that "shoot" was considered an offensive word:
# A function that would normall return this text:
#    "I bumped my toe! Shoot!"
# Would, after decorating it with `@censor()`, return:
#    "I bumped my toe! S****!"

def censor(*args):
    def inner_decorator(func):
        def wrapper(*args, **kwargs):
            text = func(*args, **kwargs)
            for word in args:
                if word in text:
                    text = text.replace(word, '*' * len(word))
            return text
        return wrapper
    return inner_decorator

@censor('shoot', 'darn')
def text():
    return "I bumped my toe! Shoot!"

print(text())  # I bumped my toe! S****!
