import time
from functools import wraps


def time_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Time of execution of function '{func.__name__}': {execution_time:.4f} seconds")
        return result

    return wrapper
