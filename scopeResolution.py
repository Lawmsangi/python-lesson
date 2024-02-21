# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global ->Built-in

# 1.Local
# def func1():
#     a = 1
#     print(a)
#
# def func2():
#     b = 2
#     print(b)
#
# func1()
# func2()

# 2.Enclosed
# def func1():
#     x = 1
#     def func2():
#         print(x)
#     func2()
#
# func1()

# 3.GLobal
# def func1():
#     print(x)
# def func2():
#     print(x)
# x = 3
# func1()
# func2()

# 4.Built-in
from math import e

def func1():
    print(e)

e =3
func1()