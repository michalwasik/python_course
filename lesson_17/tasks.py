""" Task 1
Create decorator that checks whether arguments passed to decorated functions
are:
    1. of right amount (positional arguments)
    2. all arguments (positional and keyword) are of type declared in
       function annotations (assume all annotations exist)
    3. check type of returned value
If
    1. if not True print warning and don't execute function but return None
    2. print warning if arguments don't match
    3. print warning if return type doesn't match

* use func.__code__.co_argcount for required amount of positional arguments
* use func.__code__.co_varnames for key-word arguments
* use func.__annotations__ for argument and return types


Example usage:

In [108]: @check_arguments
     ...: def divide(a: int, b: int, *, to_int: bool = True, to_str: bool = False) -> float | int | None:
     ...:     val = a // b if to_int else a / b
     ...:     return str(val) if to_str else val
     ...:

In [109]: divide(10, 3)
Out[109]: 3

In [110]: divide(10, 3.5)
Warning: argument b is of wrong type<class 'float'>, should be <class 'int'>
Out[110]: 2.0

In [111]: divide(10, 3, to_int=False)
Out[111]: 3.3333333333333335

In [112]: divide(10, 3, to_int=0)
Warning: argument to_int is of wrong type<class 'int'>, should be <class 'bool'>
Out[112]: 3.3333333333333335

In [113]: divide(10, 3, to_str=True)
Warning: return value 3 is of wrong type<class 'str'>, should be float | int | None
Out[113]: '3'

In [114]: @check_arguments
     ...: def divide(a: int, b: int, *, to_int: bool = True, to_str: bool = False) -> float | int | str | None:
     ...:     val = a // b if to_int else a / b
     ...:     return str(val) if to_str else val
     ...:

In [115]: divide(10, 3, to_str=True)
Out[115]: '3'

In [116]: divide(10, 3, to_str='True')
Warning: argument to_str is of wrong type<class 'str'>, should be <class 'bool'>
Out[116]: '3'

In [117]: divide(10, 3, to_int=False, to_str=True)
Out[117]: '3.3333333333333335'

In [118]: divide()
Incorrect number of positional arguments 0, required 2

In [119]: divide('first')
Incorrect number of positional arguments 1, required 2

In [120]: divide('first', 'second')
Warning: argument a is of wrong type<class 'str'>, should be <class 'int'>
Warning: argument b is of wrong type<class 'str'>, should be <class 'int'>

TypeError                                 Traceback (most recent call last)
Input In [120], in <cell line: 1>()
-> 1 divide('first', 'second')

Input In [114], in divide(a, b, to_int, to_str)
      1 @check_arguments
      2 def divide(a: int, b: int, *, to_int: bool = True, to_str: bool = False) -> float | int | str | None:
-> 3     val = a // b if to_int else a / b
      4     return str(val) if to_str else val

TypeError: unsupported operand type(s) for //: 'str' and 'str'
"""

# Task 2
"""
both parts
https://adventofcode.com/2018/day/13
or
https://adventofcode.com/2020/day/10
"""
