# from typing import Callable
# 
# 
# def f():
#     return 1
# 
# 
# def check_function(func: Callable):
#     print(func())
# 
# 
# check_function(f)
from functools import wraps


# def parent():
#     print("Printing from the parent() function")
# 
#     def first_child():
#         print("Printing from the first_child() function")
# 
#     def second_child():
#         print("Printing from the second_child() function")
# 
#     second_child()
#     first_child()


# parent()

# def parent(num):
#     def first_child():
#         return "Hi, I am Emma"
# 
#     def second_child():
#         return "Call me Liam"
# 
#     if num == 1:
#         return first_child
#     else:
#         return second_child
# 
# 
# first = parent(1)
# second = parent(2)
# print(first)
# print(second())

# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper


# def say_whee():
#     print('Whee!')


# print(say_whee)
# say_whee = my_decorator(say_whee)
#
# say_whee()
# print(say_whee)

# from datetime import datetime
# 
# 
# def not_during_the_night(func):
#     def wrapper():
#         if 7 <= datetime.now().hour < 22:
#             func()
#         else:
#             print('its too late!')
#     return wrapper
# 
# 
# @not_during_the_night  # same as: say_whee = not_during_the_night(say_whee)
# def say_whee():
#     print('Whee!')
# 
# 
# # say_whee = not_during_the_night(say_whee)
# say_whee()

# def do_twice(func):
#     @wraps(func)
#     def wrapper_do_twice(*args, **kwargs):
#         func(*args, **kwargs)
#         return func(*args, **kwargs)
#     return wrapper_do_twice


# @do_twice
# def say_whee(name: str):
#     print(f'Whee mr. {name}!')


# @do_twice
# def return_greeting(name: str) -> str:
#     """This function creates greeting for some person"""
#     print('Creating greeting')
#     return f"Hi {name}"


# print(return_greeting('Michal'))
# help(return_greeting)

import functools


# def decorator(func):
#     @functools.wraps(func)
#     def wrapper_decorator(*args, **kwargs):
#         # Do something before
#         value = func(*args, **kwargs)
#         # Do something after
#         return value
#     return wrapper_decorator

import functools
import time


def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__} in {run_time:.4f} secs")
        return value
    return wrapper_timer


@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])


waste_some_time(999)
