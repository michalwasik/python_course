import functools
from typing import Union


def check_arguments(func):
    def wrapper(*args, **kwargs):
        flag = False
        if len(args) != func.__code__.co_argcount:
            print(f'Warning {func.__name__} requires {func.__code__.co_argcount} arguments, {len(args)} given')
            return None
        idx = 0
        for key, value in func.__annotations__.items():
            if key == 'return':
                pass
            if idx in range(len(args)):
                if type(args[idx]) != value:
                    print(f'Warning {key} argument was passed with {type(args[idx])}, {value} expected')
                    flag = True
                idx += 1
            else:
                if key in kwargs:
                    if type(kwargs[key]) != value:
                        print(f'Warning {key} key word argument was passed with {type(kwargs[key])}, {value} expected')
                        flag = True
        if flag:
            return None
        result = func(*args, **kwargs)
        if 'return' in func.__annotations__:
            result = func(*args, **kwargs)
            if Union[type(result), func.__annotations__['return']] != Union[func.__annotations__['return']]:
                print(f"Warning {func.__name__} returned {type(result)}, {func.__annotations__['return']} expected")
        return result
    return wrapper


@check_arguments
def divide(a: int, b: int, *, to_int: bool = True, to_str: bool = False) -> float | int | None:
    val = a // b if to_int else a / b
    return str(val) if to_str else val


print(divide(10, 3, to_str=True))

# Task 2

data = open('2020_10').read().splitlines()
data = sorted(list(map(int, data)))

one_jolts = 0
two_jolts = 0
three_jolts = 0
recent_voltage = 0
for idx, adapter in enumerate(data):
    if idx == 0:
        one_jolts = 1
        recent_voltage = 1
    else:
        diff = adapter - recent_voltage
        if diff == 1:
            one_jolts += 1
        elif diff == 2:
            two_jolts += 1
        elif diff == 3:
            three_jolts += 1
        else:
            print(recent_voltage)
            break
    recent_voltage = adapter
# print(recent_voltage)

# print(one_jolts * (three_jolts + 1))
# print(max(data))
# part 2


def possible_ways(number, adapters, lookup=None):
    lookup = {} if lookup is None else lookup
    if number in adapters[-2:]:
        return 1
    if number not in lookup:
        lookup[number] = 0
        for diff in range(1, 4):
            if diff + number in adapters:
                lookup[number] += possible_ways(diff + number, adapters, lookup)
    return lookup[number]


data.extend([max(data)+3, 0])
data.sort()
# print(possible_ways(0, data))

