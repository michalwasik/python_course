# Task 1
"""
Write a Python program to make a chain of function decorators, decorators
should make output of decorated function surrounded with html elements bold,
italic or underline.

@make_bold
@make_italic
@make_underline
def hello():
    return 'hello world'

print(hello())  # -> '<b><i><u>hello world</u></i></b>'
"""

# Task 2
"""
Create decorator that will make decorated function return None in case of 
any Exception.

@ignore_exception
def divide(a: int, b:int) -> float | None:
    return a / b

divide(1, 2)
0.5
divide(1, 0)
Function divide called with args=(1, 0)  kwargs={} raised division by zero
"""

# Task 3
"""
Create decorator swap_with_number that will swap your function with random number from range 1-11

@swap_with_number
def fancy_function(number: int) -> float:
    return number / 2


print(fancy_function)  # -> 8
"""

# Task 4
"""
Create a decorator maybe_print that will swap decorated function with `print` function 
when decorated function's name stats with p

In [2]: @maybe_print
   ...: def tate():
   ...:     return 1
   ...:

In [3]: @maybe_print
   ...: def papa():
   ...:     return 2
   ...:

In [4]: tate()
Out[4]: 1

In [5]: papa('wow')
wow
"""


# Task 5
"""
https://adventofcode.com/2018/day/12

initial_state = '#..#.#..##......###...###'
"""
