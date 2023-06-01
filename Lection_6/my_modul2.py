import my_modul1
print("1", my_modul1.a)

my_modul1.a = 10
print("2", my_modul1.a)

import my_modul1
print("3", my_modul1.a)

import importlib
importlib.reload(my_modul1)

import my_modul1
print(" 4", my_modul1.a)
