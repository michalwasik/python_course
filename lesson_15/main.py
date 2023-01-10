# 18:16

# import time
# print(time.time())

# YYYY-MM-DD HH:MM:SS - ISO 8601

import datetime

# now = datetime.datetime(year=2022, month=11, day=10, hour=12)
# print(now)

# now_date = datetime.date(year=2022, month=6, day=15)
# now_time = datetime.time(hour=19, minute=32, second=45)
# print(now_date)
# print(now_time)
# print(datetime.datetime.combine(now_date, now_time))

# print(datetime.date.today())
# now = datetime.datetime.today()
# just_time = datetime.time(now.hour, now.minute, now.second)
# print(just_time)

# michal_birthday = '2000-01-03'
# date = datetime.date.fromisoformat(michal_birthday)
# print(date)
# date = date.replace(day=2)
# print(date)

# date_string = '01-31-2022 14:45:15'
# format_string = '%m-%d-%Y %H:%M:%S'
#
# date_obj = datetime.datetime.strptime(date_string, format_string)
# date_obj.replace(year=2023)
# date_str = date_obj.strftime('Year: %Y, Month: %m, Day: %d')
# print(date_str)

from datetime import datetime, timedelta
from dateutil import tz, parser
# from dateutil.zoneinfo import get_zonefile_instance

PYCON_DATE = datetime(year=2023, month=4, day=19, hour=8)
countdown = PYCON_DATE - datetime.now()
print(type(countdown))
print(f'Countdown to PyCon US 2023: {countdown}')

# print((datetime.now() + timedelta(days=100)).weekday())

# now = datetime.now(tz=tz.tzlocal())
# print(repr(now))

# japan_tz = tz.gettz('Asia/Tokyo')
# now = datetime.now(tz=japan_tz)
# print(now)
# print(now.tzname())

# print(list(get_zonefile_instance().zones))

# PYCON_DATE = parser.parse('April 19, 2023 8:00 AM')
# PYCON_DATE = PYCON_DATE.replace(tzinfo=tz.gettz('Etc/GMT-6'))
# now = datetime.now(tz=tz.tzlocal())
#
# countdown = PYCON_DATE - now
# print(f'Countdown to PyCon US 2021: {countdown}')

# now = datetime.now()
# one_day = timedelta(days=+1)
# minus_one_day = timedelta(days=-1)
# print(now + minus_one_day)

# delta = timedelta(days=+3_000, hours=-20)
# print(now + delta)

from dateutil.relativedelta import relativedelta

# one_day = relativedelta(days=+1)
# print(now + one_day)

# delta = relativedelta(years=+3, months=-4, days=+14, hours=-4, minutes=-30)
# print(now + delta)

# tomorrow = datetime(2022, 11, 18, 13, 12, 54, 385375)
#
# print(relativedelta(tomorrow, now))

# MUST READ: https://dateutil.readthedocs.io/en/stable/examples.html#relativedelta-example
