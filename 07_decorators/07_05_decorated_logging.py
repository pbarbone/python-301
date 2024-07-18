# Create a custom decorator function that records the execution time of
# the decorated function and prints the time to your console when the function
# has finished execution.

import time

def record_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start} seconds")
        return result
    return wrapper

@record_time
def wait(seconds):
    time.sleep(seconds)

wait(3)  # Execution time: 3.000000238418579 seconds
            
