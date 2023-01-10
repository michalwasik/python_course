```
# Task 1
"""
using time module create a function that takes one positional argument func,
*args and **kwargs arguments, executes given function func with given
parameters and prints how long it took to execute the function. (remember
to return value returned by func)

print(timeit(sum, map(lambda x: x**2, range(10_000_000))))
It took 2.97s to execute given function
333333283333335000000

print(timeit(sum, list(map(lambda x: x**2, range(10_000_000)))))
It took 0.23s to execute given function
333333283333335000000
"""

```

---

```
# Task 2
"""
write a function to determine whether a given year is a leap year.

print(is_leap_year(1900))  # -> False
print(is_leap_year(2004))  # -> True
"""

```

---

```
# Task 3
"""
create a function that takes datetime object and checks whether datetime
one week from it is still in the same month.

In [15]: check_date(datetime(2022, 6, 20))
Out[15]: True

In [16]: check_date(datetime(2022, 6, 25))
Out[16]: False
"""

```

---

```
# Task 4
"""
convert unix timestamp string to readable date, you can use 
datetime.datetime.fromtimestamp function

In [25]: print_timestamp(time.time() + 420_000_000)
2035-10-07 15:13:37
"""

```

---

```
# Task 5 part 1
# https://adventofcode.com/2018/day/4 - both part

```

```
# Task 1
"""
Write a function that prints n consecutive numbers once every second
In [5]: print_numbers(3)
1
2
3
"""

```

---

```
# Task 2
"""
Using datetime library write a Python program to get the first and last 
second of the day. Output should be:

First Second: 00:00:00
Last Second: 23:59:59.999999
"""

```

---

```
# Task 3
"""
Write a generator that yields list of dates between two dates.

print(*daterange(datetime(2022, 12, 25), datetime(2023, 1, 5)), sep='\n')
2022-12-25 00:00:00
2022-12-26 00:00:00
2022-12-27 00:00:00
2022-12-28 00:00:00
2022-12-29 00:00:00
2022-12-30 00:00:00
2022-12-31 00:00:00
2023-01-01 00:00:00
2023-01-02 00:00:00
2023-01-03 00:00:00
2023-01-04 00:00:00
2023-01-05 00:00:00
"""

```

---

```
# Task 4
"""
Write a Python program to get year, week number and weekday of given date.
for 
my_date = datetime(2021, 12, 29)
your program should print
Year: 2021, week number: 52, weekday: 3
"""

```

---

```
# Task 5
"""
Write a Python program to calculate two date difference in seconds.
date_1 = datetime(2022, 12, 29, 21, 37, 00)
date_2 = datetime(2022, 12, 30, 14, 30, 45)
should produce
'60825 seconds'
"""

```

---

```
# Task 6
"""
https://adventofcode.com/2019/day/12 - only first part
"""

```