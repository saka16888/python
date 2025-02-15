import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time} seconds")
        return result
    return wrapper


@measure_time
def some_function():
    # Function code here
    for i in range(10):
        print(i)
        #time.sleep(1)
    pass

some_function()
