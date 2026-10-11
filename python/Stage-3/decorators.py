def logger(func):

    def wrapper(*args):
        print("Calling function...")
        result = func(*args)
        print("Function completed")
        return result

    return wrapper


@logger
def add(a, b):
    return a + b


print(add(10, 20))