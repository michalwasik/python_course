# Task 1
import time
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from typing import Generator


def timeit(func, *args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    print(f'It took {round(time.time() - start, 2)}s to execute given function')
    return result


# print(timeit(sum, map(lambda x: x**2, range(10_000_000))))
# print(timeit(sum, list(map(lambda x: x**2, range(10_000_000)))))

# Task 2

def is_leap_year(year: int) -> bool:
    if year % 4 != 0:
        return False
    elif year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    else:
        return True

# print(is_leap_year(1900))
# print(is_leap_year(2004))

# import calendar
#
# print(calendar.isleap(1900))
# print(calendar.isleap(2004))

# Task 3


def check_date(date: datetime) -> bool:
    next_week = date + timedelta(weeks=1)
    if next_week.month == date.month:
        return True
    else:
        return False


# print(check_date(datetime(2022, 6, 20)))
# print(check_date(datetime(2022, 6, 25)))

# Task 4

def unix_converter(unix_str: str) -> str:
    converted = datetime.fromtimestamp(float(unix_str)).strftime("%Y-%m-%d %H:%M:%S")
    return converted


data_time = str(time.time() + 420_000_000)
# print(unix_converter(data_time))

# Task 5
data = open('puzzle_2018_4').read().splitlines()
date_format = '%Y-%m-%d %H:%M'
watch = []
for line in data:
    puzzle = line.split(']')
    date = puzzle[0][1:]
    command = puzzle[1][1:]
    if command[0] == 'G':
        command = int(command.split(' ')[1][1:])
    else:
        command = command[0]
    converted_date = datetime.strptime(date, date_format)
    watch.append((converted_date, command))
watch.sort(key=lambda x: x[0])
minute = timedelta(minutes=1)
guards_min = {}
guards_asleep = {}
guard = 0
asleep = 0
for item in watch:
    if isinstance(item[1], int):
        guard = item[1]
    elif item[1] == 'f':
        asleep = item[0].minute
    else:
        awake = item[0].minute
        for min in range(asleep, awake):
            if guard not in guards_min:
                guards_min[guard] = {}
            if min not in guards_min[guard]:
                guards_min[guard][min] = 1
            else:
                guards_min[guard][min] += 1
            if guard not in guards_asleep:
                guards_asleep[guard] = 1
            else:
                guards_asleep[guard] += 1

sleepyhead = max(guards_asleep, key=guards_asleep.get)
most_minutes = max(guards_min[sleepyhead], key=guards_min[sleepyhead].get)

# print(sleepyhead * most_minutes)

rep_num = 0
most_rep_min = 0
most_rep_guard = 0
for key, value in guards_min.items():
    max_min = max(value, key=value.get)
    if value[max_min] > most_rep_min:
        most_rep_min = value[max_min]
        rep_num = max_min
        most_rep_guard = key

# print(most_rep_guard * rep_num)

# ------------------------------------------------

# Task 1


def print_numbers(sec: int):
    for x in range(1, sec + 1):
        print(x)
        time.sleep(1)


# print_numbers(3)

# Task 2

def seconds(date:datetime):
    first = date.replace(hour=0, minute=0, second=0)
    last = date.replace(hour=23, minute=59, second=59)
    date_format = '%H:%M:%S'
    first_str = first.strftime(date_format)
    last_str = last.strftime(date_format)
    # print(first_str)
    # print(last_str)
    import datetime
    print(f'First Second: {datetime.time.min}')
    print(f'Last Second: {datetime.time.max}')


# seconds(datetime.now())

# Task 3

def daterange(begin: datetime, stop: datetime) -> Generator[datetime, None, None]:
    begin = begin.replace(hour=0, minute=0, second=0, microsecond=0)
    yield begin
    current_date = begin
    while current_date < stop:
        current_date = current_date+relativedelta(days=+1)
        yield current_date

    for days in range((date_to - date_from).days + 1):
        yield date_from + timedelta(days)


# print(*daterange(datetime(2022, 12, 25), datetime(2023, 1, 5)), sep='\n')

# Task 4

def get_date(date: datetime):
    week_nr = date.strftime('%V')
    day_nr = date.strftime('%u')
    year_nr = date.strftime('%Y')
    print(f'Year: {year_nr},  week number: {week_nr}, weekday: {day_nr}')

    my_date = datetime(2021, 12, 29)
    year, week_number, weekday = my_date.isocalendar()
    print(f'Year: {year}, week number: {week_number}, weekday: {weekday}')



# get_date(datetime(2021, 12, 29))

# Task 5

def sec_diff(date_1: datetime, date_2: datetime) -> int:
    difference = date_1 - date_2
    result = difference.total_seconds()
    result = abs(int(result))
    return result


date_1 = datetime(2022, 12, 29, 21, 37, 00)
date_2 = datetime(2022, 12, 30, 14, 30, 45)
# print(f'seconds difference is: {sec_diff(date_1, date_2)}')

# Task 6
data = open('puzzle_2019_12').read().splitlines()
num_data = []
for moons in data:
    coords = moons[1:-1].split(',')
    row = []
    for dim in coords:
        dim = int(dim.strip().split('=')[1])
        row.append(dim)
    num_data.append(row)

vel = []
for _ in range(4):
    vel.append([0, 0, 0])

for _ in range(1000):
    for moon_idx, moon in enumerate(num_data):
        for dim_idx, pos in enumerate(moon):
            value = 0
            another_moons = list(range(4))
            another_moons.remove(moon_idx)
            for x in another_moons:
                if pos > num_data[x][dim_idx]:
                    value -= 1
                if pos < num_data[x][dim_idx]:
                    value += 1
            vel[moon_idx][dim_idx] += value
    for x in range(4):
        for y in range(3):
            num_data[x][y] += vel[x][y]
result = 0
for z in range(4):
    moon_sum = sum([abs(ele) for ele in num_data[z]])
    vel_sum = sum([abs(ele) for ele in vel[z]])
    result += moon_sum * vel_sum

# print(result)
