""" Task 1
Create package that has dwo submodules
    1. first one allows you to fetch some online random data
    (using requests library and url https://random-data-api.com/api/bank/random_bank)
    2. second one will give you insights about downloaded data (print dict using json library)
that will be used is such way:

import date_insider

data = data_insider.fetch_data.fetch_data()
data_insider.describe_data.describe_data(data)  # this will print something like:
{
    "account_number": "3153234255",
    "bank_name": "ABC INTERNATIONAL BANK PLC",
    "iban": "GB14MAKW99182485061975",
    "id": 3251,
    "routing_number": "714205560",
    "swift_bic": "AAHVGB21",
    "uid": "754b0641-7bee-4805-a595-d8c459f4cb6a"
}
"""


""" Task 2
Manually add this package to site-packages of your venv, in cmd navigate outside of your project, activate your venv,
open python interactive shell and try your library
"""


""" Task 3
google some example python packages and create new project with requirements.txt file containing these libraries,
create script that will make use of at least one of these libraries.
"""


""" Task 4 part 1
Snake game - create 2D ascii game, it should work like this:
https://drive.google.com/file/d/1l2wbSOk_hTnFRAys7qT_-tJ6PJmmL4aj/view?usp=sharing

AI for snake is for you to figure out, just make sure it can run for a while :)
"""


""" Task 4 part 2
Add requirements.txt file to this project and termcolor library inside of it, 
use this library to make color of printed snake green
"""
