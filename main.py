import inspect


def function(a, b):
    return a * b


print(inspect.getsource(function))
