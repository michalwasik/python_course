# Task 1

def make_bold(func):
    def wrapper(*args, **kwargs):
        text = func(*args, **kwargs)
        html_text = '<b>' + text + '</b>'
        return html_text
    return wrapper


def make_italic(func):
    def wrapper(*args, **kwargs):
        text = func(*args, **kwargs)
        html_text = '<i>' + text + '</i>'
        return html_text
    return wrapper


def make_underline(func):
    def wrapper(*args, **kwargs):
        text = func(*args, **kwargs)
        html_text = '<u>' + text + '</u>'
        return html_text
    return wrapper


@make_bold
@make_italic
@make_underline
def hello():
    return 'hello world'


# print(hello())

# Task 2


def ignore_exception(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except Exception as err:
            print(f'Function {func.__name__} called with args={args}  kwargs={kwargs} raised {err}')
            return None
        else:
            print(result)
    return wrapper


@ignore_exception
def divide(a: int, b: int) -> float | None:
    return a / b


divide(1, 2)
divide(1, 0)
# Task 3
from random import randint
import functools


def swap_with_number(func):
    return randint(1, 10)
    # @functools.wraps(func)
    # def wrapper(*args, **kwargs):
    #     number = randint(1, 11)
    #     return number
    # return wrapper()


@swap_with_number
def fancy_function(number: int) -> float:
    return number / 2


print(fancy_function)

# Task 4


def maybe_print(func):
    if str(func.__name__).lower().startswith('p'):
        return print
    return func


@maybe_print
def tate():
    return 1


@maybe_print
def papa():
    return 2


# print(papa())
# print(tate())

# Task 5
data = open('2018_12').read().splitlines()
initial_state = data[0][15:]
puzzle = data[2:]
healthy = []
sick = []
for pattern in puzzle:
    if pattern[-1] == '.':
        sick.append(pattern)
    else:
        healthy.append(pattern)
grown_pattern = []
death_pattern = []

for pattern in sick:
    death_pattern.append(pattern[:5])
for pattern in healthy:
    grown_pattern.append(pattern[:5])

ctr_idx = 0
for _ in range(2000):
    plantation = ''
    if '....' + initial_state[:1] in grown_pattern:
        print('..' + initial_state[:3])
        ctr_idx -= 2
        initial_state = '....' + initial_state
    elif '...' + initial_state[:2] in grown_pattern:
        ctr_idx -= 1
        initial_state = '...' + initial_state
    else:
        initial_state = '..' + initial_state
    if initial_state[-5:] != '.....':
        initial_state += '.....'
    for idx in range(len(initial_state) - 4):
        part = initial_state[idx:idx+5]
        if part in grown_pattern:
            plantation += '#'
        else:
            plantation += '.'
    initial_state = plantation
result = 0
last_season = list(initial_state)
for pot_nr, pot in enumerate(last_season, start=ctr_idx):
    if pot == '#':
        result += pot_nr
print(ctr_idx)
print(result)1