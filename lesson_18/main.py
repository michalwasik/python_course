# import my_package
#
# print(my_package.my_script_1.func_1())
# print(my_package.my_subpackage.my_script_2.func_2())

# from my_package import *
#
# print(my_script_1.func_1())
# print(dupa)
# print(my_subpackage.my_script_2.func_2())

# import sysconfig
# print(sysconfig.get_path("purelib"))
# import pip
#
# print(pip.main(['list']))

# import venv
#
# print(venv.main)

# import requests
# import marshmallow

import sys
print(*sys.path, sep='\n')
