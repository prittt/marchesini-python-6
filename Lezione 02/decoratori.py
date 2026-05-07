# def parent(num):

#     def first_child():
#         return "Hi, I am Emma"

#     def second_child():
#         return "Call me Liam"

#     if num == 1:
#         return first_child
#     else:
#         return second_child
    
# ret = parent(1)
# print(type(ret)
# print(ret)

import functools
import time

def my_decorator(funz):
    @functools.wraps(funz)
    def wrapper(*args, **kwargs):
        print("Something before the function")
        ret = funz(*args, **kwargs)
        print("Something after the function")
        return ret
    return wrapper

@my_decorator
def foo(param):
    print(f"Hi, I'm the foo function, with parameter {param}")
    return 3

@my_decorator
def foo2():
    print("Hi, I'm the foo2 function")

start = time.perf_counter()
foo(5)
stop = time.perf_counter()
elapsed = stop - start

foo2()

print(help(foo))

# decorated_foo = my_decorator(foo)
# decorated_foo2 = my_decorator(foo2)
# decorated_foo()
# decorated_foo2()