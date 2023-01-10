import functools
from random import choice

def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]                      # 1
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
        signature = ", ".join(args_repr + kwargs_repr)           # 3
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__} returned {value!r}")           # 4
        return value
    return wrapper_debug
#
#
# @debug
# def make_greeting(name, age=None):
#     if age is None:
#         return f"Howdy {name}!"
#     else:
#         return f"Whoa {name}! {age} already, you are growing up!"
#
#
# print(make_greeting('Michał'))

# PLUGINS = {}
#
#
# def register(func):
#     PLUGINS[func.__name__] = func
#     return func
#
#
# @register
# def say_hello(name):
#     return f"Hello {name}"
#
#
# @register
# def be_awesome(name):
#     return f"Yo {name}, together we are the awesomest!"
#
#
# greet_func = choice(list(PLUGINS.values()))
# print(greet_func('Michal'))


# def do_twice(func):
#     def wrapper_do_twice(*args, **kwargs):
#         func(*args, **kwargs)
#         return func(*args, **kwargs)
#     return wrapper_do_twice
#
#
# @do_twice
# @debug
# def greet(name):
#     print(f"Hello {name}")
#
#
# greet('Monika')


def counter(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        return func(*args, **kwargs)
    wrapper.count = 0
    return wrapper


# @counter
# def add(a, b):
#     return a + b
#
#
# add(1, 2)
# add(1, 2)
# add(1, 2)
# add(1, 2)
# print(add.count)


def cache(func):
    def wrapper(*args, **kwargs):
        key = args + tuple(kwargs.items())
        if key not in wrapper._cache:
            wrapper._cache[key] = func(*args, **kwargs)
        return wrapper._cache[key]
    wrapper._cache = {}
    return wrapper


@counter
@cache
def fibonacci(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


@counter
@cache
def fibonacci_rec(n: int) -> int:
    if n in {0, 1}:
        return n
    return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)



print(fibonacci(34))
print(fibonacci.count)
print(fibonacci_rec(34))
print(fibonacci_rec.count)
# --------------------------
# circle_idx = 0
# ctr_idx = 0
# curr_idx = 0
# map_generations = {}
# left_idx_dict = {}
# while circle_idx < 130:
#     circle_idx += 1
#     plantation = ''
#     if initial_state[:5] != '.....':
#         initial_state = '.....' + initial_state
#         ctr_idx -= 3
#     else:
#         ctr_idx += 2
#     if initial_state[-5:] != '.....':
#         initial_state += '.....'
#     for idx in range(len(initial_state) - 4):
#         part = initial_state[idx:idx+5]
#         if part in grown_pattern:
#             plantation += '#'
#         else:
#             plantation += '.'
#     if circle_idx >= 30:
#         map_generations[circle_idx % 100] = plantation
#         left_idx_dict[circle_idx % 100] = ctr_idx
#     initial_state = plantation
#
# result = 0
#
# last_season = list(map_generations[50000000000%100])
# for pot_nr, pot in enumerate(last_season, start=left_idx_dict[50000000000%100]):
#     if pot == '#':
#         result += pot_nr
# print(result)
