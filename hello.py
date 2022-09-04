import random
# write a hello function that prints "Hello, world!"


def hello():
    print("Hello World!")


# invoke hello function
hello()


# write a decorator function logs imput and output and times it to a function
def log(func):
    def wrapper(*args, **kwargs):
        print("Function: {} is called".format(func.__name__))
        print("Arguments: {}".format(args))
        print("Keyword Arguments: {}".format(kwargs))
        result = func(*args, **kwargs)
        print("Result: {}".format(result))
        return result
    return wrapper


# invoke decorator function using hello function
hello = log(hello)
hello()


# write a function that yileds a generator that randomly picks between three types of fruit and returns it
def fruit():
    import random
    fruits = ["apple", "orange", "banana"]
    while True:
        yield random.choice(fruits)


# invoke fruit function and print the result of the generator for five runs
for i in range(5):
    print(next(fruit()))
